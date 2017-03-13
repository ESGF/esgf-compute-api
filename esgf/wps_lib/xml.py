#! /usr/bin/env python

from __future__ import absolute_import

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

    def __append_value(self, name, node, metadata):
        values = getattr(self, name)

        if values is None:
            values = []

        if issubclass(metadata.value_type, XMLDocument):
            value = metadata.value_type.from_element(node, self.translator)
        else:
            try:
                value = metadata.value_type(node.text)
            except ValueError:
                raise ValueConversionError('Could not convert from %s to %s' %
                        (value.__class__, metadata.value_type.__class__))

        values.append(value)

        setattr(self, name, values)

    def __store_value(self, name, node, metadata):
        if metadata.output_list:
            self.__append_value(name, node, metadata)
        else:
            if (inspect.isclass(metadata.value_type) and
                    issubclass(metadata.value_type, XMLDocument)):
                value = metadata.value_type.from_element(node, self.translator)
            else:
                value = None
                candidates = metadata.value_type

                if not isinstance(candidates, (list, tuple)):
                    candidates = [candidates]

                for c in candidates:
                    try:
                        if issubclass(c, XMLDocument):
                            value = c.from_xml(node.text)
                        else:
                            value = c(node.text)
                    except ValueError:
                        pass

                if value is None:
                    raise ValueConversionError('Could not convert from %s to %s' %
                            (value.__class__, metadata.value_type.__class__))

            setattr(self, name, value)

    def __match_parent(self, node):
        parent = node
        parent_element = None
        parent_metadata = None

        while True:
            parent = parent.getparent()

            if parent is None:
                break

            if parent.tag in self.elements:
                metadata = self.elements[parent.tag]

                if (metadata.child_tag is not None and
                        metadata.child_tag == node.tag):
                    parent_element = parent
                    
                    parent_metadata = metadata

                    break

        return parent_element, parent_metadata

    def __set_property(self, name, value, metadata):
        try:
            value = metadata.value_type(value)
        except ValueError:
            raise ValueConversionError('Could not convert from %s to %s' %
                    (value.__class__, metadata.value_type.__class__))

        setattr(self, name, value)

    def __match_element_value_type(self, tag):
        for name, metadata in self.elements.iteritems():
            if (not isinstance(metadata.value_type, (list, tuple)) and
                    tag == metadata.value_type.__name__):
                return name, metadata

        return None, None

    def parse_xml(self, root):
        logger.debug('%s BEGIN PARSING "%s" %s', '#'*6, re.sub('^{.*}', '', root.tag), '#'*6)
        logger.debug(etree.tostring(root, pretty_print=True))
        logger.debug('Translator %s', self.translator)
        logger.debug('Known elements %s', self.elements.keys())

        for name, value in root.attrib.iteritems():
            name = re.sub('^{.*}', '', name)

            if self.translator is not None:
                name = self.translator.attribute_to_property(name)

            if name in self.attributes:
                metadata = self.attributes[name]

                self.__set_property(name, value, metadata)

        stack = [root]

        while len(stack):
            node = stack.pop()

            tag = node.tag

            name = re.sub('^{.*}', '', tag)
                
            if self.translator is not None:
                trans_name = self.translator.element_to_property(name)
            else:
                trans_name = name
            
            logger.debug('Processing element "%s" (%s)', trans_name, name)

            # Check each non-root element for attached attributes
            if node != root:
                for atrans_name, value in node.attrib.iteritems():
                    if self.translator is not None:
                        atrans_name = self.translator.attribute_to_property(atrans_name)

                    if atrans_name in self.attributes:
                        metadata = self.attributes[atrans_name]

                        self.__set_property(atrans_name, value, metadata)

            if trans_name in self.elements:
                metadata = self.elements[trans_name]

                logger.debug('Element "%s" is a known property %s', trans_name, metadata)

                if metadata.attr is not None:
                    if metadata.attr in node.attrib:
                        value = node.attrib[metadata.attr]

                        self.__set_property(node.tag, value, metadata)
                elif (metadata.child_tag is not None or
                        (metadata.output_list and
                            issubclass(metadata.value_type, XMLDocument)) or
                        metadata.path is not None):
                    for c in node.getchildren():
                        stack.append(c)
                else:
                    self.__store_value(trans_name, node, metadata)
            else:
                logger.debug('Handling unknown element "%s"', name)

                match_trans_name, match_metadata = self.__match_element_value_type(name)

                if match_trans_name is not None:
                    self.__store_value(match_trans_name, node, match_metadata)
                else:
                    parent_element, parent_metadata = self.__match_parent(node)

                    if parent_element is not None:
                        self.__store_value(parent_element.tag, node, parent_metadata)
                    else:
                        for c in node.getchildren():
                            stack.append(c)

        logger.debug('%s END PARSING "%s" %s', '#'*6, re.sub('^{.*}', '', root.tag), '#'*6)

    def __generate_name(self, name, namespace, metadata=None):
        new_name = name

        if metadata is not None and self.translator is not None:
            if isinstance(metadata, Element):
                new_name = self.translator.property_to_element(name)
            else:
                new_name = self.translator.property_to_attribute(name)

        if namespace is None:
            return new_name

        try:
            return '{%s}%s' % (self.nsmap[namespace], new_name)
        except TypeError:
            return new_name
        except KeyError:
            raise MissingNamespaceError('Namespace %s was not found in the namespace map' %
                    (namespace,))

    def __generate_element(self, parent, name, value, metadata, cache):
        if value is None:
            return None

        if isinstance(value, XMLDocument):
            if self.translator is not None:
                value.translator = self.translator

            child_element = value.generate_xml()

            parent.append(child_element)
        else:
            new_name = self.__generate_name(name, metadata.namespace, metadata)

            new_element = etree.SubElement(parent, new_name)

            if metadata.attr is not None:
                new_element.set(metadata.attr, value)
            else:
                new_element.text = str(value)

            cache[name] = new_element

    def generate_xml(self):
        self.validate()

        cls_name = self.__class__.__name__

        if self.tag is not None:
            cls_name = self.tag

        cls_name = self.__generate_name(cls_name, self.namespace)

        root = etree.Element(cls_name, nsmap=self.nsmap)

        cache = {}

        for name, metadata in self.elements.iteritems():
            parent = root

            if metadata.store_value:
                value = getattr(self, name)

                root.text = value

                break

            if metadata.path is not None:
                for s in metadata.path.split('/'):
                    if s != '':
                        new_s = s

                        if (metadata.nsmap is not None and
                                s in metadata.nsmap):
                            new_s = self.__generate_name(s, metadata.nsmap[s], metadata)

                        parent = etree.SubElement(parent, new_s)

                        cache[s] = parent

            if metadata.attr is not None:
                value = getattr(self, name)

                self.__generate_element(parent, name, value, metadata, cache)
            elif metadata.child_tag is not None:
                value = getattr(self, name)
    
                new_name = self.__generate_name(name, metadata.namespace, metadata)

                new_element = etree.SubElement(parent, new_name)

                cache[name] = new_element

                if not metadata.output_list:
                    value = [value]
    
                if value is not None:
                    for v in value:
                        self.__generate_element(new_element, metadata.child_tag, v, metadata, cache)
            elif metadata.output_list:
                value = getattr(self, name)

                if value is not None:
                    for v in value:
                        self.__generate_element(parent, name, v, metadata, cache)
            else:
                value = getattr(self, name)

                self.__generate_element(parent, name, value, metadata, cache)

        for name, metadata in self.attributes.iteritems():
            value = getattr(self, name)

            if value is None:
                continue

            name = self.__generate_name(name, metadata.namespace, metadata)

            if metadata.attach is not None:
                if metadata.attach in cache:
                    cache[metadata.attach].set(name, str(value))
            else:
                root.set(name, str(value))

        return root

    def xml(self, pretty_print=False):
        return etree.tostring(self.generate_xml(), pretty_print=True)
