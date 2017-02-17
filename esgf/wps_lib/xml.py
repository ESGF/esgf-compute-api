#! /usr/bin/env python

from lxml import etree
import logging
import re
import sys
import types

logger = logging.getLogger(__name__)

CONVERSION_TYPES = {
        types.BooleanType: bool,
        types.FloatType: float,
        types.IntType: int,
        types.LongType: long,
        types.StringType: str,
        }

class Attribute(object):
    def __init__(self, **kwargs):
        self.namespace = kwargs.get('namespace')
        self.value_type = kwargs.get('value_type', str)
        self.required = kwargs.get('required', False)
        self.default = kwargs.get('default')
        self.attach_element = kwargs.get('attach_element')

    def __call__(self, f):
        f.metadata = self

        return f

    def __str__(self):
        return ', '.join('%s=%s' % (x, y) for x, y in self.__dict__.iteritems())

class Element(object):
    def __init__(self, **kwargs):
        self.namespace = kwargs.get('namespace')
        self.nsmap = kwargs.get('nsmap')
        self.child_tag = kwargs.get('child_tag')
        self.child_namespace = kwargs.get('child_namespace')
        self.value_type = kwargs.get('value_type', str)
        self.store_attr = kwargs.get('store_attr', False)
        self.name = kwargs.get('name')
        self.attr_namespace = kwargs.get('attr_namespace')
        self.path = kwargs.get('path')
        self.output_list = kwargs.get('output_list', False)
        self.minimum = kwargs.get('minimum', 1)
        self.maximum = kwargs.get('maximum', 1)
        self.store_value = kwargs.get('store_value', False)
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
        multiple = {}

        store_value = None 

        for key, value in dct.iteritems():
            if (hasattr(value, 'metadata') and
                    isinstance(value.metadata, Element)):
                metadata = value.metadata
                
                elements[key] = metadata

                if metadata.store_value and store_value is None:
                    store_value = key

                if isinstance(metadata.value_type, (list, tuple)):
                    multiple[key] = metadata

                dct[key] = property(fget(key), fset(key))

        for key, value in dct.iteritems():
            if (hasattr(value, 'metadata') and
                    isinstance(value.metadata, Attribute)):
                metadata = value.metadata

                if metadata.attach_element is not None:
                    if metadata.attach_element not in elements:
                        raise ValidationError('Element %s does not exist for '
                                'binding Attribute %s' %
                                (metadata.attach_element, key))

                    target = elements[metadata.attach_element]

                    target.attributes[key] = metadata
                else:
                    attributes[key] = metadata

                dct[key] = property(fget(key), fset(key))

        cls = super(XMLDocumentMarkupType, mcs).__new__(mcs, name, bases, dct)

        cls.store_value = store_value
        cls.attributes = attributes
        cls.elements = elements
        cls.multiple = multiple

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
    def __init__(self, tag=None, namespace=None, nsmap=None, translator=None):
        self.tag = tag
        self.namespace = namespace
        self.nsmap = nsmap
        self.translator = translator

    @classmethod
    def from_xml(cls, data):
        obj = cls()

        tree = etree.fromstring(data)

        obj.parse_xml(tree)

        return obj

    @classmethod
    def from_element(cls, element, translator):
        obj = cls(translator=translator)

        obj.parse_xml(element)

        return obj

    def __generate_name(self, name, namespace=None):
        if namespace is not None and self.nsmap is None:
            raise MissingNamespaceError('Namespace %s was provided but was '
                    'not included in the map' % (namespace,))
        elif namespace is not None and self.nsmap is not None:
            try:
                return '{%s}%s' % (self.nsmap[namespace], name)
            except KeyError:
                raise MissingNamespaceError('Namespace %s is not present in '
                        'the map' % (namespace,))
        elif self.nsmap is not None:
            try:
                return '{%s}%s' % (self.nsmap[name], name)
            except KeyError:
                pass
    
        return name

    def __parse_namespace(self, name):
        return re.sub('{.*}', '', name)

    def validate(self):
        for name, metadata in self.attributes.iteritems():
            value = getattr(self, name)

            if metadata.required and value is None:
                raise ValidationError('Required attribute %s does not have a '
                        'value' % (name,))

        for name, metadata in self.elements.iteritems():
            value = getattr(self, name)

            if metadata.minimum >= 1 and value is None:

                raise ValidationError('Element %s is required and does not '
                        'have a value' % (name,))
            elif isinstance(value, (list, tuple)):
                if not metadata.output_list:
                    raise ValidationError('Element %s was not expecting a '
                            'list' % (name,))

                value_len = len(value)

                if value_len < metadata.minimum:
                    raise ValidationError('Element %s has less values than is '
                            'required' % (name,)) 
                elif metadata.maximum is not None and value_len > metadata.maximum:
                    raise ValidationError('Element %s has more values than is '
                            'required' % (name,))

    def parse_xml(self, root):
        for name, value in root.attrib.iteritems():
            name = self.__parse_namespace(name)

            if self.translator is not None:
                name = self.translator.attribute_to_property(name)

            if hasattr(self, name) and name in self.attributes:
                metadata = self.attributes[name]

                try:
                    value = CONVERSION_TYPES[metadata.value_type](value)
                except KeyError:
                    raise ValueConversionError('Could not convert to '
                            'type %s' % (metadata.value_type,))

                setattr(self, name, value)

        stack = [root]
        parent = None
        parent_values = []

        while len(stack):
            element = stack[-1]

            name = element.tag

            name = self.__parse_namespace(name)

            logger.info('ELEMENT %s', name)

            if self.translator is not None:
                name = self.translator.element_to_property(name)

            if hasattr(self, name.lower()):
                metadata = self.elements[name.lower()]

                logger.info(metadata.attributes)

                if parent is not None and metadata == parent:
                    stack.pop()

                    parent = None

                    if metadata.output_list:
                        setattr(self, name, parent_values)
                    else:
                        setattr(self, name, parent_values[0])

                    parent_values = []
                elif metadata.store_attr:
                    stack.pop()

                    for n, value in element.attrib.iteritems():
                        bare_name = self.__parse_namespace(n)

                        if metadata.name == bare_name:
                            value = element.attrib[n]

                            break

                    setattr(self, name, value)
                elif metadata.output_list or metadata.child_tag:
                    if (issubclass(metadata.value_type, XMLDocument) and
                            not metadata.output_list):
                        stack.pop()

                        value = metadata.value_type.from_element(element,
                                translator=self.translator)

                        values = getattr(self, name)

                        if values is None:
                            values = []

                        values.append(value)

                        setattr(self, name, values)
                    else:
                        children = element.getchildren()

                        if len(children) == 0:
                            stack.pop()

                            values = getattr(self, name)

                            if values is None:
                                values = []

                            values.append(element.text)

                            setattr(self, name, values)
                        else:
                            #type_name = metadata.value_type.__name__

                            #if self.translator is not None:
                            #    type_name = self.translator.element_to_property(type_name)


                            if issubclass(metadata.value_type, XMLDocument):
                            #if (issubclass(metadata.value_type, XMLDocument) and
                            #        name == type_name):
                                stack.pop()

                                value = getattr(self, name)

                                if value is None:
                                    value = []
        
                                new_value = metadata.value_type.from_element(element, 
                                        translator=self.translator)

                                value.append(new_value)

                                setattr(self, name, value)
                            else:
                                for c in element.getchildren():
                                    stack.append(c)

                                parent = metadata
                else:
                    stack.pop()

                    if isinstance(metadata.value_type, (list, tuple)):
                        stack.append(*element.getchildren())

                        continue
                    elif issubclass(metadata.value_type, XMLDocument):
                        value = metadata.value_type.from_element(element,
                                self.translator)
                    else:
                        value = element.text

                        try:
                            value = CONVERSION_TYPES[metadata.value_type](value)
                        except KeyError:
                            raise ValueConversionError('Could not convert to '
                                    'type %s' % (metadata.value_type,))

                    setattr(self, name.lower(), value)
            elif parent is not None:
                stack.pop()

                if issubclass(parent.value_type, XMLDocument):
                    value = parent.value_type.from_element(element,
                            translator=self.translator)    
                else:
                    value = parent.value_type(element.text)

                parent_values.append(value)
            elif self.store_value is not None:
                stack.pop()

                logger.info('STORED_VALUE')

                value = getattr(self, self.store_value)

                if value is None:
                    value = []

                for c in element.getchildren():
                    value.append(str(c))

                setattr(self, self.store_value, value)
            else:
                logger.info('No property for tag %s', element.tag)

                stack.pop()

                logger.info('Checking properties that support multiple values')

                processed = False

                for name, metadata in self.multiple.iteritems():
                    cls_dict = dict((x.__name__, x) for x in metadata.value_type)

                    logger.info('Class dictionary %s for tag %s', cls_dict, element.tag)

                    element_tag = self.__parse_namespace(element.tag)

                    if element_tag in cls_dict.keys():
                        cls = cls_dict[element_tag]

                        logger.info('Creating object from class %s' , cls)

                        value = cls.from_element(element,
                                translator=self.translator)

                        logger.info('Done creating object %s', value)

                        setattr(self, name, value)

                        processed = True

                        break

                if not processed:
                    for c in element.getchildren():
                        stack.append(c)

        logger.info('Done parsing current node')

    def __create_node(self, name, namespace, parent=None):
        tag = self.__generate_name(name, namespace)

        if parent is None:
            node = etree.Element(tag, nsmap=self.nsmap)
        else:
            node = etree.SubElement(parent, tag, nsmap=self.nsmap)

        return node
        
    def __set_attributes(self, node, attrs):
        for name, metadata in attrs.iteritems():
            if metadata.attach_element is not None:
                continue

            value = getattr(self, name)

            if value is None:
                value = metadata.default

            if value is None:
                continue

            if self.translator is not None:
                name = self.translator.property_to_attribute(name)

            attr_name = self.__generate_name(name, metadata.namespace)

            node.set(attr_name, str(value))

    def __generate_path(self, node, path, nsmap, cache):
        parts = [x for x in path.split('/') if x != '']

        current_path = ''

        parent = node

        for p in parts:
            current_path = '%s/%s' % (current_path, p)

            try:
                namespace = nsmap[p]
            except (KeyError, TypeError):
                namespace = None

            tag = self.__generate_name(p, namespace)

            parent = etree.SubElement(parent, tag)

            cache[current_path] = parent

        return parent

    def __create_child_list_node(self, parent, name, metadata, values):
        # Check that all list/tuple valuess are the same. Having mixed
        # types would cause a parsing headache, since the source type
        # is not explicitly store but implicitly derived from the class
        if not all(values[0].__class__ == x.__class__ for x in values[1:]):
            raise MismatchedTypeError('All valuess in a list/tuple are '
                    'required to be of the same type: %s' %
                    ([x.__class__ for x in values]))

        tag = self.__generate_name(name, metadata.namespace)

        # Already know values is a valid list/tuple
        if issubclass(values[0].__class__, XMLDocument):
            parent = etree.SubElement(parent, tag)

            for v in values:
                element = v.generate_xml()

                parent.append(element)
        else:
            if metadata.child_tag is not None:
                parent = etree.SubElement(parent, tag)

                for v in values:
                    new_element = self.__create_node(
                            metadata.child_tag,
                            metadata.child_namespace,
                            parent=parent)

                    new_element.text = str(v)

            else:
                for v in values:
                    new_element = etree.SubElement(parent, tag)

                    new_element.text = str(v)

    def __create_child_node(self, parent, name, metadata, value):
        tag = self.__generate_name(name, metadata.namespace)

        if metadata.child_tag is not None:
            parent = etree.SubElement(parent, tag)

            new_element = self.__create_node(metadata.child_tag,
                    metadata.child_namespace,
                    parent=parent)

        if metadata.store_attr:
            name = self.__generate_name(name,
                    metadata.attr_namespace)

            if metadata.name is None:
                parent.set(name, str(value))
            else:
                new_element = etree.SubElement(parent, tag)

                new_element.set(metadata.name, str(value))
        else:
            if metadata.store_value:
                parent.text = str(value)
            else:
                new_element = etree.SubElement(parent, tag)

                new_element.text = str(value)

                for name, _ in metadata.attributes.iteritems():
                    value = getattr(self, name)

                    if self.translator is not None:
                        name = self.translator.property_to_attribute(name)

                    new_element.set(name, str(value))

    def generate_xml(self, element=None):
        self.validate()

        cls_name = self.__class__.__name__

        if self.tag:
            cls_name = self.tag

        root = self.__create_node(cls_name, self.namespace)

        self.__set_attributes(root, self.attributes)

        path_cache = {}

        for name, metadata in self.elements.iteritems():
            value = getattr(self, name)

            if value is None:
                continue

            if self.translator is not None:
                name = self.translator.propertry_to_element(name)

            # Reset the parent node to the root
            parent = root

            # Modify parent if we need to create a path
            if metadata.path is not None:
                parent = self.__generate_path(parent,
                        metadata.path,
                        metadata.nsmap,
                        path_cache)

            if issubclass(value.__class__, XMLDocument):
                element = value.generate_xml()

                parent.append(element)
            elif isinstance(value, (list, tuple)):
                self.__create_child_list_node(parent, name, metadata, value)
            else:
                self.__create_child_node(parent, name, metadata, value)

        return root

    def xml(self, pretty_print=False):
        return etree.tostring(self.generate_xml(), pretty_print=True)
