#! /usr/bin/env python

from lxml import etree
import inspect
import logging
import re
import sys

logger = logging.getLogger(__name__)

SUPPORTED_CONVERSION = (str, float, bool, int, long)

class Translator(object):
    def property_to_element(self, name):
        raise NotImplmenetedError()

    def property_to_attribute(self, name):
        raise NotImplmenetedError()

    def element_to_property(self, name):
        raise NotImplmenetedError()

    def element_to_attribute(self, name):
        raise NotImplmenetedError()

class Attribute(object):
    def __init__(self, **kwargs):
        self.namespace = kwargs.get('namespace')
        self.value_type = kwargs.get('value_type', str)
        self.required = kwargs.get('required', False)
        self.attach = kwargs.get('attach')

    def __call__(self, f):
        f.metadata = self

        return f

    def __str__(self):
        return ', '.join('%s=%s' % (x, y) for x, y in self.__dict__.iteritems())

class Element(object):
    def __init__(self, **kwargs):
        self.namespace = kwargs.get('namespace')
        self.output_list = kwargs.get('output_list', False)
        self.child_tag = kwargs.get('child_tag')
        self.child_namespace = kwargs.get('child_namespace')
        self.combine = kwargs.get('combine', False)
        self.attr = kwargs.get('attr')
        self.path = kwargs.get('path')
        self.nsmap = kwargs.get('nsmap')
        self.value_type = kwargs.get('value_type', str)
        self.store_value = kwargs.get('store_value', False)
        self.minimum = kwargs.get('minimum', 1)
        self.maximum = kwargs.get('maximum')
        self.attributes = {}

    def __call__(self, f):
        f.metadata = self

        return f

    def __str__(self):
        return ', '.join('%s=%s' % (x, y) for x, y in self.__dict__.iteritems())

class XMLDocumentMarkupType(type):
    def __new__(mcs, name, bases, dct):
        def fget(key):
            def fget_wrapper(self):
                return getattr(self, '__%s' % (key,), None)

            return fget_wrapper

        def fset(key):
            def fset_wrapper(self, value):
                setattr(self, '__%s' % (key,), value)

            return fset_wrapper

        attributes = {}
        elements = {}
        store_value = None

        for key, value in dct.iteritems():
            if (hasattr(value, 'metadata') and
                    isinstance(value.metadata, Element)):
                metadata = value.metadata

                if metadata.store_value and store_value is None:
                    store_value = key
                
                elements[key] = metadata

                dct[key] = property(fget(key), fset(key))

        for key, value in dct.iteritems():
            if (hasattr(value, 'metadata') and
                    isinstance(value.metadata, Attribute)):
                metadata = value.metadata

                attributes[key] = metadata

                dct[key] = property(fget(key), fset(key))

        cls = super(XMLDocumentMarkupType, mcs).__new__(mcs, name, bases, dct)

        cls.attributes = attributes
        cls.elements = elements
        cls.store_value = store_value

        return cls

class ValueConversionError(Exception):
    pass

class MissingNamespaceError(Exception):
    pass

class MismatchedTypeError(Exception):
    pass

class ValidationError(Exception):
    pass

class XMLDocument(object):
    def __init__(self, namespace=None, nsmap=None, tag=None, translator=None):
        self.namespace = namespace
        self.nsmap = nsmap
        self.tag = tag
        self.translator = translator

    @classmethod
    def from_xml(cls, data):
        doc = cls()

        tree = etree.fromstring(data)

        doc.parse_xml(tree)

        return doc

    @classmethod
    def from_element(cls, element, translator):
        doc = cls()

        doc.translator = translator

        doc.parse_xml(element)

        return doc

    def __parse_attributes(self, node):
        for name, value in node.attrib.iteritems():
            parsed_name = self.__parse_name(name, Attribute)

            if parsed_name in self.attributes:
                metadata = self.attributes[parsed_name]

                setattr(self, parsed_name, metadata.value_type(value))

    def __parse_name(self, name, item_type):
        value = re.sub('^{.*}', '', name)

        if self.translator is not None:
            if item_type == Element:
                value = self.translator.element_to_property(value)
            else:
                value = self.translator.attribute_to_property(value)

        return value

    def __append_children_to_stack(self, node, stack):
        children = node.getchildren()

        if len(children) > 0:
            for c in children:
                stack.append(c)

    def __set_values(self, tag, node, metadata):
        values = getattr(self, tag)

        if values is None:
            values = []

        if issubclass(metadata.value_type, XMLDocument):
            value = metadata.value_type.from_element(node, self.translator)
        else:
            value = metadata.value_type(node.text)

        values.append(value)

        setattr(self, tag, values)

    def parse_xml(self, root):
        self.__parse_attributes(root)

        stack = [root]

        while len(stack):
            node = stack.pop()

            if len(node.attrib) > 0:
                for key, value in node.attrib.iteritems():
                    name = self.__parse_name(key, Attribute)

                    if name in self.attributes:
                        attr_metadata = self.attributes[name]

                        setattr(self, name, attr_metadata.value_type(value))

            tag = self.__parse_name(node.tag, Element)

            if tag in self.elements:
                metadata = self.elements[tag]

                if metadata.output_list:
                    if metadata.child_tag is not None:
                        self.__append_children_to_stack(node, stack)
                    else:
                        self.__set_values(tag, node, metadata)
                else:
                    if metadata.attr is not None:
                        value = metadata.value_type(node.attrib[metadata.attr])

                        setattr(self, tag, value)
                    else:
                        if metadata.value_type in SUPPORTED_CONVERSION:
                            value = metadata.value_type(node.text)

                            setattr(self, tag, value)
                        else:
                            children = node.getchildren()

                            if len(children) > 0:
                                self.__append_children_to_stack(node, stack)
                            else:
                                value = metadata.value_type.from_element(node,
                                        self.translator)

                                setattr(self, tag, value)
            else:
                if self.store_value is not None:
                    children = node.getchildren()

                    if len(children) > 0:
                        values = []

                        for c in children:
                            values.append(etree.tostring(c))

                        setattr(self, self.store_value, values)
                    else:
                        setattr(self, self.store_value, node.text)
                else:
                    parent = node.getparent()

                    if parent is not None:
                        parent_tag = self.__parse_name(parent.tag, Element)
                        
                        if parent_tag in self.elements:
                            parent_metadata = self.elements[parent_tag]

                            if parent_metadata.combine or parent_metadata.output_list:
                                self.__set_values(parent_tag, node, metadata)
                            else:
                                if isinstance(metadata.value_type, (list, tuple)):
                                    vt_names = dict((x.__name__, x)
                                            for x in metadata.value_type)
                                    
                                    name = tag

                                    if self.translator is not None:
                                        name = self.translator.property_to_element(name)


                                    value = vt_names[name].from_element(node,
                                            self.translator)
                                elif (inspect.isclass(metadata.value_type) and
                                        issubclass(metadata.value_type, XMLDocument)):
                                    value = metadata.value_type.from_element(node,
                                            self.translator)
                                else:
                                    value = metadata.value_type(node.text)

                                setattr(self, parent_tag, value)

                            continue

                    self.__append_children_to_stack(node, stack)

    def __generate_name(self, name, namespace, item_type):
        if self.translator is not None:
            if item_type == Element:
                name = self.translator.property_to_element(name)
            else:
                name = self.translator.property_to_attribute(name)

        if namespace is not None:
            try:
                name = '{%s}%s' % (self.nsmap[namespace], name)
            except TypeError:
                raise MissingNamespaceError('Namespace provided but map was not.')
            except KeyError:
                raise MissingNamespaceError('Namespace %s was not found in the '
                        'map.' % (namespace,))

        return name

    def __generate_node(self, root, node_name, metadata, value):
        child_node = root

        if metadata.child_tag is not None:
            child_node_name = self.__generate_name(metadata.child_tag,
                    metadata.child_namespace, Element)

            child_node = etree.SubElement(root, child_node_name)

        if metadata.attr is not None:
            child_node.set(metadata.attr, str(value))
        else:
            if issubclass(value.__class__, XMLDocument):
                value_node = value.generate_xml()

                child_node.append(value_node)
            else:
                child_node.text = str(value)

    def __generate_path(self, parent, path, local_nsmap, path_cache):
        if path in path_cache:
            return path_cache[path]

        parts = [x for x in path.split('/') if x != '']

        current = ''

        for p in parts:
            current = '%s%s' % (current, p)

            namespace = None

            if local_nsmap is not None and p in local_nsmap:
                namespace = local_nsmap[p]

            p_tag = self.__generate_name(p, namespace, Element)

            parent = etree.SubElement(parent, p_tag)

            path_cache[current] = parent

            current = '%s/' % (current,)

        return parent

    def validate(self):
        for name, metadata in self.attributes.iteritems():
            if metadata.required:
                value = getattr(self, name)

                if value is None:
                    raise ValidationError('%s Attribute %s is required' %
                            (self.__class__.__name__, name,))

        for name, metadata in self.elements.iteritems():
            if metadata.output_list:
                value = getattr(self, name)

                if metadata.minimum > 0:
                    if not isinstance(value, (list, tuple)):
                        raise ValidationError('%s Element %s was expecting a '
                                'list or tuple of values' % (self.__class__.__name__, name,))
                    elif value is None or len(value) < metadata.minimum:
                        raise ValidationError('%s Element %s requires a minimum '
                                'of %s values' % (self.__class__.__name__, name, metadata.minimum))

                if metadata.maximum is not None:
                    if len(value) > metadata.maximum:
                        raise ValidationError('%s Element %s requires max %s'
                                ' values, %s were provided' %
                                (self.__class__.__name__, name, metadata.maximum, len(value)))
            else:
                if metadata.minimum > 0:
                    value = getattr(self, name)

                    if value is None:
                        raise ValidationError('%s Element %s requires atleast '
                                'one value' % (self.__class__.__name__, name,))
                    elif isinstance(value, (list, tuple)):
                        raise ValidationError('%s Element %s was expecting a '
                                'single value' % (self.__class__.__name__, name,))

    def generate_xml(self):
        self.validate()

        cls_name = self.__class__.__name__

        if self.tag is not None:
            cls_name = self.tag

        tag = self.__generate_name(cls_name, self.namespace, Element)

        root = etree.Element(tag, nsmap=self.nsmap)

        if self.store_value is not None:
            value = getattr(self, self.store_value)

            root.text = str(value)
        else:
            path_cache = {}

            for name, metadata in self.elements.iteritems():
                parent = root

                if metadata.path is not None:
                    parent = self.__generate_path(parent, metadata.path,
                            metadata.nsmap, path_cache)

                value = getattr(self, name)

                node_name = self.__generate_name(name, metadata.namespace,
                        Element)

                if metadata.output_list:
                    if metadata.combine:
                        node = etree.SubElement(parent, node_name)

                    if value is not None:
                        for v in value:
                            if not metadata.combine:
                                node = etree.SubElement(parent, node_name)

                            self.__generate_node(node, node_name, metadata, v)
                else:
                    node = etree.SubElement(parent, node_name)

                    self.__generate_node(node, node_name, metadata, value)

        for name, metadata in self.attributes.iteritems():
            value = getattr(self, name)

            attr_name = self.__generate_name(name, metadata.namespace,
                    Attribute)

            if metadata.attach is not None:
                if metadata.attach in path_cache:
                    path_cache[metadata.attach].set(attr_name, str(value))
            else:
                root.set(attr_name, str(value))

        return root

    def xml(self, pretty_print=False):
        return etree.tostring(self.generate_xml(), pretty_print=True)
