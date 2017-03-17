#! /usr/bin/env python

import unittest

from lxml import etree

from esgf.wps_lib import xml

class ChildXML(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self, **kwargs):
        super(ChildXML, self).__init__()

        self.test_child_element = kwargs.get('name')

    @xml.Element()
    def test_child_element(self):
        pass

class ChildXML2(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self, **kwargs):
        super(ChildXML2, self).__init__()

        self.test_child_element = kwargs.get('name')

    @xml.Element()
    def test_child_element(self):
        pass

class XMLTest(xml.XMLDocument):
    __metaclass__ = xml.XMLDocumentMarkupType

    def __init__(self):
        super(XMLTest, self).__init__()

    @xml.Attribute()
    def test_attribute(self):
        pass

    @xml.Attribute(value_type=float)
    def attribute_float(self):
        pass

    @xml.Attribute(value_type=bool)
    def attribute_bool(self):
        pass

    @xml.Attribute(value_type=int)
    def attribute_int(self):
        pass

    @xml.Attribute(value_type=long)
    def attribute_long(self):
        pass

    @xml.Attribute(attach='step2')
    def attribute_attach(self):
        pass

    @xml.Element()
    def test_element(self):
        pass

    @xml.Element(path='/step1/step2/step3/')
    def path_element(self):
        pass

    @xml.Element(output_list=True)
    def item_element(self):
        pass

    @xml.Element(child_tag='item', output_list=True)
    def list_child_tag(self):
        pass

    @xml.Element(child_tag='item')
    def child_tag(self):
        pass

    @xml.Element(attr='test')
    def attribute_element(self):
        pass

    @xml.Element(value_type=float)
    def element_float(self):
        pass

    @xml.Element(value_type=bool)
    def element_bool(self):
        pass

    @xml.Element(value_type=int)
    def element_int(self):
        pass

    @xml.Element(value_type=long)
    def element_long(self):
        pass

    @xml.Element(value_type=ChildXML)
    def child_xml(self):
        pass

    @xml.Element(value_type=ChildXML2, output_list=True)
    def child_xml_list(self):
        pass

class XMLDocumentTest(unittest.TestCase):

    def setUp(self):
        test_doc = XMLTest()
        test_doc.test_element = 'ELEMENT'
        test_doc.test_attribute = 'ATTRIBUTE'
        test_doc.path_element = 'PATH'
        test_doc.item_element = [1, 2, 3, 4]
        test_doc.list_child_tag = [5, 6, 7, 8]
        test_doc.child_tag = 'CHILD'
        test_doc.attribute_element = 'VALUE_AS_ATTRIBUTE'
        test_doc.element_float = 3.12
        test_doc.element_bool = True
        test_doc.element_int = 3
        test_doc.element_long = 4L
        test_doc.attribute_float = 3.12
        test_doc.attribute_bool = True
        test_doc.attribute_int = 3
        test_doc.attribute_long = 4L
        test_doc.attribute_attach = 'ATTACH'
        test_doc.child_xml = ChildXML(name = 'test1')
        test_doc.child_xml_list = [ChildXML2(name = 'test2'), ChildXML2(name = 'test3')]

        self.doc = test_doc.xml()

    def test_translator(self):
        class TestTranslator(xml.Translator):
            def property_to_element(self, name):
                return name.upper()

            def element_to_property(self, name):
                return name.lower()

            def property_to_attribute(self, name):
                return name.upper()

            def attribute_to_property(self, name):
                return name.lower()

        class Child(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Child, self).__init__()

            @xml.Attribute()
            def child_1(self):
                pass

            @xml.Element()
            def child_2(self):
                pass

        class Parent(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Parent, self).__init__(translator=TestTranslator())

            @xml.Attribute()
            def parent_1(self):
                pass

            @xml.Element(value_type=Child)
            def child_test(self):
                pass

        p = Parent()
        p.parent_1 = 'attribute'
        p.child_test = Child()
        p.child_test.child_1 = 'ATTRIBUTE'
        p.child_test.child_2 = 'ELEMENT'

        doc = p.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Parent/@PARENT_1')), 1)
        self.assertEqual(len(tree.xpath('/Parent/Child/@CHILD_1')), 1)
        self.assertEqual(len(tree.xpath('/Parent/Child/CHILD_2')), 1)

        d = Parent.from_xml(doc)

        self.assertEqual(d.parent_1, 'attribute')

        self.assertIsInstance(d.child_test, Child)
        self.assertEqual(d.child_test.child_1, 'ATTRIBUTE')
        self.assertEqual(d.child_test.child_2, 'ELEMENT')

    def test_child_xml_list(self):
        tree = etree.fromstring(self.doc)

        self.assertEqual(len(tree.xpath('/XMLTest/ChildXML2')), 2)

        d = XMLTest.from_xml(self.doc)

        self.assertIsInstance(d.child_xml_list, list)
        self.assertEqual(len(d.child_xml_list), 2)

        self.assertTrue(reduce(lambda x, y: x == y,
            [isinstance(x, ChildXML) for x in d.child_xml_list]))

        self.assertItemsEqual(['test2', 'test3'], [x.test_child_element for x in d.child_xml_list])

    def test_child_xml(self):
        tree = etree.fromstring(self.doc)
        
        self.assertEqual(len(tree.xpath('/XMLTest/ChildXML')), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertIsInstance(d.child_xml, ChildXML)
        self.assertEqual(d.child_xml.test_child_element, 'test1')

    def test_namespace(self):
        NSMAP = {
                'a': 'http://a',
                'b': 'http://b',
                'c': 'http://c',
                }

        class Namespace(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Namespace, self).__init__(namespace='a', nsmap=NSMAP)

            @xml.Attribute(namespace='b')
            def bspace(self):
                pass

            @xml.Element(namespace='c')
            def cspace(self):
                pass

            @xml.Element(path='path1/path2', nsmap={'path1':'a','path2':'b'})
            def path(self):
                pass

        c = Namespace()
        c.bspace = 'B'
        c.cspace = 'C'
        c.path = 'AAA'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/a:Namespace', namespaces=NSMAP)), 1)
        self.assertEqual(len(tree.xpath('/a:Namespace/@b:bspace', namespaces=NSMAP)), 1)
        self.assertEqual(len(tree.xpath('/a:Namespace/c:cspace', namespaces=NSMAP)), 1)
        self.assertEqual(len(tree.xpath('/a:Namespace/a:path1/b:path2/path', namespaces=NSMAP)), 1)

        d = Namespace.from_xml(doc)

        self.assertEqual(d.bspace, 'B')
        self.assertEqual(d.cspace, 'C')

        self.assertEqual(d.path, 'AAA')

    def test_tag_override(self):
        class TagOverride(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(TagOverride, self).__init__(tag='Car')

        c = TagOverride()

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car')), 1)

    def test_attribute_attach(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/step1/step2/@attribute_attach')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.attribute_attach, 'ATTACH')

    def test_store_value(self):
        class StoreValue(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(StoreValue, self).__init__()

            @xml.Element(store_value=True)
            def data(self):
                pass

            @xml.Attribute()
            def read(self):
                pass

        c = StoreValue()
        c.data = 'This could be XML or something'
        c.read = 'NO'

        doc = c.xml()

        tree = etree.fromstring(doc)

        result = tree.xpath('/StoreValue')

        self.assertEqual(result[0].getchildren(), [])
        self.assertEqual(len(tree.xpath('/StoreValue/@read')), 1)

    def test_value_type(self):
        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.element_float, 3.12)
        self.assertEqual(d.element_bool, True)
        self.assertEqual(d.element_int, 3)
        self.assertEqual(d.element_long, 4L)

        self.assertEqual(d.attribute_float, 3.12)
        self.assertEqual(d.attribute_bool, True)
        self.assertEqual(d.attribute_int, 3)
        self.assertEqual(d.attribute_long, 4L)

    def test_value_as_attribute(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/attribute_element/@test')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.attribute_element, 'VALUE_AS_ATTRIBUTE')

    def test_list_child_tag(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/list_child_tag/item')

        self.assertEqual(len(result), 4)

        d = XMLTest.from_xml(self.doc)

        self.assertItemsEqual(['5', '6', '7', '8'], d.list_child_tag)

    def test_child_tag(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/child_tag/item')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.child_tag, 'CHILD')

    def test_output_list(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/item_element')

        self.assertEqual(len(result), 4)

        d = XMLTest.from_xml(self.doc)

        self.assertItemsEqual(['1', '2', '3', '4'], d.item_element)

    def test_path(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/step1/step2/step3/path_element')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.path_element, 'PATH')

    def test_attribute(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/@test_attribute')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.test_attribute, 'ATTRIBUTE')

    def test_element(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest/test_element')

        self.assertEqual(len(result), 1)

        d = XMLTest.from_xml(self.doc)

        self.assertEqual(d.test_element, 'ELEMENT')

    def test_root(self):
        tree = etree.fromstring(self.doc)

        result = tree.xpath('/XMLTest')

        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
