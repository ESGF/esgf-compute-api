#! /usr/bin/env python

from lxml import etree
import re
import sys
import types

CONVERSION_TYPES = {
        types.BooleanType: bool,
        types.FloatType: float,
        types.IntType: int,
        types.LongType: long,
        types.StringType: str,
        }

class Attribute(object):
    def __init__(self, namespace=None, value_type=None):
        self.namespace = namespace
        self.value_type = value_type

    def __call__(self, f):
        f.attribute = self

        return f

class Element(object):
    def __init__(self, namespace=None, path=None, value_type=None, output_list=False):
        self.namespace = namespace
        self.path = path
        self.value_type = value_type
        self.output_list = output_list

    def __call__(self, f):
        f.element = self

        return f

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

        for key, value in dct.iteritems():
            if hasattr(value, 'attribute'):
                attributes[key] = value

                dct[key] = property(fget(key), fset(key))
            elif hasattr(value, 'element'):
                elements[key] = value

                dct[key] = property(fget(key), fset(key))

        cls = type.__new__(mcs, name, bases, dct)

        cls.attributes = attributes

        cls.elements = elements

        return cls

class MissingNamespaceMapError(Exception):
    pass

class MissMatchedTypeError(Exception):
    pass

class NonConvertableTypeError(Exception):
    pass

class XMLDocument(object):
    def __init__(self, namespace=None, nsmap=None):
        self.namespace = namespace
        self.nsmap = nsmap

    @classmethod
    def from_xml(cls, xml):
        xml_doc = cls()

        tree = etree.fromstring(xml)

        xml_doc.parse_xml(tree)

        return xml_doc
    
    @classmethod
    def from_element(cls, element):
        xml_doc = cls()

        xml_doc.parse_xml(element)

        return xml_doc

    @property
    def xml(self):
        tree = self.create_tree()

        return etree.tostring(tree)

    def __create_sub_element(self, name, parent, namespace):
        tag = self.__create_tag(name, namespace)

        return etree.SubElement(parent, tag)

    def __convert_name(self, name):
        matches = re.findall('[A-Z][a-z0-9]*', name[0].upper()+name[1:])

        return '_'.join(x.lower() for x in matches)

    def __create_tag(self, tag, namespace, lower_case=False):
        if lower_case:
            parts = tag.split('_')

            tag = ''.join([parts[0].lower()] + [x.title() for x in parts[1:]])
        else:
            tag = ''.join([x.title() for x in tag.split('_')])

        if namespace is not None:
            if self.nsmap is None:
                raise MissingNamespaceMapError

            return '{%s}%s' % (self.nsmap[namespace], tag)
        else:
            return tag

    def __set_property(self, metadata, name, element=None, value=None):
        if metadata.value_type is not None:
            if isinstance(metadata, Element) and metadata.output_list:
                values = []

                for child in element.getchildren():
                    child_value = metadata.value_type.from_element(child)

                    values.append(child_value)

                setattr(self, name, values)
            else:
                if issubclass(metadata.value_type, XMLDocument):
                    value = metadata.value_type.from_element(element)

                    setattr(self, name, value)
                else:
                    if metadata.value_type in CONVERSION_TYPES:
                        if value is None:
                            value = CONVERSION_TYPES[metadata.value_type](element.text)
                        else:
                            value = CONVERSION_TYPES[metadata.value_type](value)

                        setattr(self, name, value)
                    else:
                        raise NonConvertableTypeError('Could not convert type %s' % (metadata.value_type,))
        else:
            if value is None and element is not None:
                setattr(self, name, element.text)
            else:
                setattr(self, name, value)

    def __create_path(self, metadata, parent, cache):
        parts = [x for x in metadata.path.split('/') if x != '']

        current = ''

        for p in parts:
            current += '/%s' % (p,)

            if current in cache:
                parent = cache[current]
            else:
                tag = self.__create_tag(p, metadata.namespace)

                parent = etree.SubElement(parent, tag)

            cache[current] = parent

        return parent

    def parse_xml(self, tree):
        if tree.tag != self.__class__.__name__:
            raise MissMatchedTypeError('XML type %s, decoding type %s' %
                    (tree.tag, self.__class__.__name__))

        for attr, value in tree.attrib.iteritems():
            name = self.__convert_name(attr)

            attribute = self.attributes[name].attribute

            self.__set_property(attribute, name, value=value)

        current = ''
        stack = tree.getchildren()

        while len(stack):
            item = stack.pop()

            name = self.__convert_name(item.tag)

            if hasattr(self, name):
                element = self.elements[name].element

                self.__set_property(element, name, element=item)
            else:
                children = item.getchildren()

                if len(children) > 0:
                    for child in children:
                        stack.append(child)

    def create_tree(self, element=None):
        path_cache = {}

        if element is None:
            tree = etree.Element(
                    self.__create_tag(self.__class__.__name__, self.namespace),
                    nsmap=self.nsmap)
        else:
            tree = etree.SubElement(
                    element,
                    self.__create_tag(self.__class__.__name__, self.namespace),
                    nsmap=self.nsmap)

        for name, attr in self.attributes.iteritems():
            value = getattr(self, name)

            name = self.__create_tag(name, attr.attribute.namespace, lower_case=True)

            tree.set(name, str(value))

        for name, elem in self.elements.iteritems():
            value = getattr(self, name)

            parent = tree

            if elem.element.path is not None:
                parent = self.__create_path(elem.element, parent, path_cache)

            if issubclass(value.__class__, XMLDocument):
                value.create_tree(parent)
            elif isinstance(value, list):
                new_elem = self.__create_sub_element(name,
                        parent,
                        elem.element.namespace)

                for item in value:
                    if issubclass(item.__class__, XMLDocument):
                        item.create_tree(new_elem)
            else:
                new_elem = self.__create_sub_element(name,
                        parent,
                        elem.element.namespace)

                new_elem.text = str(value) 

        return tree
