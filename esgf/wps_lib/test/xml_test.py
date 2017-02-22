#! /usr/bin/env python

import unittest
from lxml import etree

from esgf.wps_lib import xml

class XMLDocumentTest(unittest.TestCase):

    def test_element_list_maximum(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(minimum=0)
            def passengers(self):
                pass

            @xml.Element(maximum=4, output_list=True)
            def snacks(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.snacks = [0, 1, 2, 3, 4]

        with self.assertRaises(xml.ValidationError):
            c.xml()

    def test_element_list_minimum(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(output_list=True)
            def passengers(self):
                pass

            @xml.Element(minimum=0, output_list=True)
            def luggage(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.passengers = 'test'

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.passengers = []

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.passengers = [0]

        self.assertIsNotNone(c.xml())

    def test_element_minimum(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element()
            def driver(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.driver = []

        with self.assertRaises(xml.ValidationError):
            c.xml()

        c.driver = 'tom'

        self.assertIsNotNone(c.xml())

    def test_attribute_required(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute(required=True)
            def color(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError):
            c.xml()

    def test_tranlator(self):
        class UpCaseDownCase(xml.Translator):
            def property_to_element(self, name):
                return name.upper()

            def element_to_property(self, name):
                return name.lower()

            def property_to_attribute(self, name):
                return name.upper()

            def attribute_to_property(self, name):
                return name.lower()

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(translator=UpCaseDownCase())

            @xml.Attribute()
            def color(self):
                pass

            @xml.Element()
            def name(self):
                pass

        c = Car()
        c.color = 'blue'
        c.name = 'tom'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/CAR/@COLOR')), 1)
        self.assertEqual(len(tree.xpath('/CAR/NAME')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.color, 'blue')
        self.assertEqual(c.name, 'tom')

    def test_override_tag(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(tag='Ford')

        c = Car()
        
        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Ford')), 1)

    def test_multiple_type(self):
        class V8(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(V8, self).__init__()

            @xml.Attribute()
            def cylinders(self):
                pass

        class V6(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(V6, self).__init__()

            @xml.Attribute()
            def cylinders(self):
                pass

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(value_type=(V6, V8))
            def engine(self):
                pass

        c = Car()
        c.engine = V8()
        c.engine.cylinders = 8

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/engine/V8')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.engine, V8)

    def test_store_value(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(store_value=True)
            def data(self):
                pass

        c = Car()
        c.data = 'test'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/data')), 0)
        
        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.data, 'test')

    def test_value_type_xml_document(self):
        class Person(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Person, self).__init__()

            @xml.Attribute()
            def name(self):
                pass

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(value_type=Person)
            def driver(self):
                pass

            @xml.Element(value_type=Person, output_list=True)
            def passengers(self):
                pass

        c = Car()
        c.driver = Person()
        c.driver.name = 'tom'
        c.passengers = [Person(), Person()]
        c.passengers[0].name = 'larry'
        c.passengers[1].name = 'jerry'

        doc = c.xml()

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.driver, Person)
        self.assertEqual(c.driver.name, 'tom')
        self.assertIsInstance(c.passengers, list)
        self.assertIsInstance(c.passengers[0], Person)
        self.assertEqual(len(c.passengers), 2)

    def test_value_type(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute(value_type=bool)
            def driving(self):
                pass

            @xml.Element(value_type=int)
            def speed(self):
                pass

        c = Car()
        c.driving = True
        c.speed = 56

        doc = c.xml()

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.driving, True)
        self.assertEqual(c.speed, 56)

    def test_path_shared(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(path='people')
            def driver(self):
                pass

            @xml.Element(path='people')
            def passenger(self):
                pass

        c = Car()
        c.driver = 'tom'
        c.passenger = 'larry'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/people')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.driver, 'tom')
        self.assertEqual(c.passenger, 'larry')

    def test_path_namespace(self):
        nsmap = {
                'ns1': 'http://ns1',
                'ns2': 'http://ns2',
                }
        
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(nsmap=nsmap)

            @xml.Element(path='outside', nsmap={'outside':'ns1'})
            def color(self):
                pass

            @xml.Element(path='engine/oil', nsmap={'engine':'ns2','oil':'ns1'})
            def level(self):
                pass

        c = Car()
        c.color = 'blue'
        c.level = 'low'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/ns1:outside/color',
            namespaces=nsmap)), 1)
        self.assertEqual(len(tree.xpath('/Car/ns2:engine/ns1:oil/level',
            namespaces=nsmap)), 1)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.color, 'blue')
        self.assertEqual(c.level, 'low')

    def test_path(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(path='outside')
            def color(self):
                pass

            @xml.Element(path='engine/oil')
            def level(self):
                pass

            @xml.Element(path='collection', output_list=True)
            def passenger(self):
                pass

        c = Car()
        c.color = 'blue'
        c.level = 'low'
        c.passenger = ['tom', 'larry']

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/outside/color')), 1)
        self.assertEqual(len(tree.xpath('/Car/engine/oil/level')), 1)
        self.assertEqual(len(tree.xpath('/Car/collection/passenger')), 2)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.color, 'blue')
        self.assertEqual(c.level, 'low')
        self.assertIsInstance(c.passenger, list)
        self.assertIn('tom', c.passenger)
        self.assertIn('larry', c.passenger)

    def test_element_attr(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(attr='color')
            def outside(self):
                pass

        c = Car()
        c.outside = 'blue'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/outside/@color')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.outside, 'blue')

    def test_child_tag_combine(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(child_tag='item', combine=True, output_list=True)
            def multiple(self):
                pass

        c = Car()
        c.multiple = [0, 1, 2, 3]

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/multiple')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.multiple, list)
        self.assertEqual(len(c.multiple), 4)
    
    def test_child_tag_namespace(self):
        nsmap = {
                'ns1': 'http://ns1',
                'ns2': 'http://ns2',
                }

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(nsmap=nsmap)

            @xml.Element(child_tag='item', child_namespace='ns1', output_list=True)
            def multiple(self):
                pass

            @xml.Element(child_tag='item', child_namespace='ns2')
            def single(self):
                pass

        c = Car()
        c.multiple = [0, 1, 2, 3]
        c.single = 0

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/multiple/ns1:item',
            namespaces=nsmap)), 4)
        self.assertEqual(len(tree.xpath('/Car/single/ns2:item',
            namespaces=nsmap)), 1)

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.multiple, list)
        self.assertEqual(len(c.multiple), 4)
        self.assertIsInstance(c.single, str)

    def test_child_tag(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(child_tag='item', output_list=True)
            def multiple(self):
                pass

            @xml.Element(child_tag='item')
            def single(self):
                pass

        c = Car()
        c.multiple = [0, 1, 2, 3]
        c.single = 0

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/multiple/item')), 4)
        self.assertEqual(len(tree.xpath('/Car/single/item')), 1)

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.multiple, list)
        self.assertEqual(len(c.multiple), 4)
        self.assertIsInstance(c.single, str)

    def test_element_output_list(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()
            
            @xml.Element(output_list=True)
            def passengers(self):
                pass

        c = Car()
        c.passengers = ['tom', 'larry']

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car/passengers')), 2)

        del c

        c = Car.from_xml(doc)

        self.assertIsInstance(c.passengers, list)
        self.assertEqual(len(c.passengers), 2)

    def test_namespace_missing(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(nsmap={})

            @xml.Element(namespace='ns1')
            def driver(self):
                pass

        class Car2(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car2, self).__init__()

            @xml.Element(namespace='ns1')
            def driver(self):
                pass

        c = Car()
        c.driver = 'tom'

        with self.assertRaises(xml.MissingNamespaceError):
            c.xml()

        c = Car2()
        c.driver = 'tom'

        with self.assertRaises(xml.MissingNamespaceError):
            c.xml()

    def test_namespace(self):
        nsmap = {
                'desc': 'description',
                'state': 'state',
                }

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(namespace='state', nsmap=nsmap)

            @xml.Attribute(namespace='state')
            def state(self):
                pass

            @xml.Element(namespace='desc')
            def color(self):
                pass

        c = Car()
        c.state = 'driving'
        c.color = 'blue'

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/state:Car/@state:state',
            namespaces=nsmap)), 1)
        self.assertEqual(len(tree.xpath('/state:Car/desc:color',
            namespaces=nsmap)), 1)

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.color, 'blue')
        self.assertEqual(c.state, 'driving')

    def test_attribute(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()
            
            @xml.Attribute()
            def driver(self):
                pass

        c = Car()
        c.driver = 'tom'

        doc = c.xml()

        tree = etree.fromstring(doc)

        xpath_result = tree.xpath('/Car/@driver')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0], 'tom')

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.driver, 'tom')

    def test_element(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()
            
            @xml.Element()
            def driver(self):
                pass
       
        c = Car()
        c.driver = 'tom'

        doc = c.xml()

        tree = etree.fromstring(doc)

        xpath_result = tree.xpath('/Car/driver')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0].text, 'tom')

        del c

        c = Car.from_xml(doc)

        self.assertEqual(c.driver, 'tom')

    def test_document(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

        c = Car()

        doc = c.xml()

        tree = etree.fromstring(doc)

        self.assertEqual(len(tree.xpath('/Car')), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
