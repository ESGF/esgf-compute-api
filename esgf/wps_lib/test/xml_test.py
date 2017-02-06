#! /usr/bin/env python

import unittest
from lxml import etree

from esgf.wps_lib import xml

class XMLDocumentTest(unittest.TestCase):

    def test_list_value_type(self):
        class Person(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def name(self):
                pass

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element(value_type=Person, output_list=True)
            def seats(self):
                pass

        p1 = Person()
        p1.name = 'Tom'

        p2 = Person()
        p2.name = 'Larry'

        c = Car()
        c.seats = [p1, p2]

        tree = etree.fromstring(c.xml)

        self.assertEqual(len(tree.xpath('/Car/Seats/Person')), 2)

        tree = c.xml

        del c

        c = Car.from_xml(tree)

        self.assertEqual(len(c.seats), 2)

    def test_invalid_type_attribute(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute(value_type=dict)
            def test1(self):
                pass

        c = Car()
        c.test1 = {}

        tree = c.xml

        del c

        with self.assertRaises(xml.NonConvertableTypeError):
            c = Car.from_xml(tree)

    def test_invalid_type_element(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element(value_type=dict)
            def test1(self):
                pass

        c = Car()
        c.test1 = {}

        tree = c.xml

        del c

        with self.assertRaises(xml.NonConvertableTypeError):
            c = Car.from_xml(tree)

    def test_value_type(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute(value_type=bool)
            def test6(self):
                pass

            @xml.Element(value_type=bool)
            def test1(self):
                pass

            @xml.Element(value_type=float)
            def test2(self):
                pass

            @xml.Element(value_type=int)
            def test3(self):
                pass

            @xml.Element(value_type=long)
            def test4(self):
                pass

            @xml.Element(value_type=str)
            def test5(self):
                pass
        
        c = Car()
        c.test1 = True
        c.test2 = 3.14
        c.test3 = 3
        c.test4 = 3L
        c.test5 = 'Test'

        c.test6 = True

        tree = c.xml

        del c

        c = Car.from_xml(tree)

        self.assertEqual(c.test1, True)
        self.assertEqual(c.test2, 3.14)
        self.assertEqual(c.test3, 3)
        self.assertEqual(c.test4, 3L)
        self.assertEqual(c.test5, 'Test')
        self.assertEqual(c.test6, True)

    def test_mismatched_types(self):
        xml_str = """
            <Truck />
        """
        
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

        with self.assertRaises(xml.MissMatchedTypeError) as e:
            c = Car.from_xml(xml_str)

        self.assertEqual(e.exception.message, 'XML type Truck, decoding type Car')

    def test_parse_xml(self):
        class Engine(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def cylinders(self):
                pass

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def serial_number(self):
                pass

            @xml.Element(path='/interior')
            def color(self):
                pass

            @xml.Element()
            def state(self):
                pass

            @xml.Element(value_type=Engine)
            def engine(self):
                pass

        c = Car()
        c.serial_number = '123234'
        c.color = 'blue'
        c.state = 'driving'
        c.engine = Engine()
        c.engine.cylinders = 8

        tree = c.xml

        del c

        c = Car.from_xml(tree)

        self.assertEqual(c.serial_number, '123234')
        self.assertEqual(c.color, 'blue')
        self.assertEqual(c.state, 'driving')
        self.assertIsInstance(c.engine, Engine)
        self.assertEqual(c.engine.cylinders, '8')

    def test_element_class(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element()
            def engine(self):
                pass

        class Engine(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def cylinders(self):
                pass

        c = Car()
        c.engine = Engine()
        c.engine.cylinders = 8

        tree = etree.fromstring(c.xml)

        paths = [
                '/Car',
                '/Car/Engine',
                '/Car/Engine/@cylinders',
                ]
        
        results = []

        for p in paths:
            xpath_result = tree.xpath(p)

            self.assertEqual(len(xpath_result), 1)

            results.append(xpath_result)

        self.assertEqual(results[-1][0], '8')

    def test_elements_same_path(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element(path='/interior')
            def leather(self):
                pass

            @xml.Element(path='/interior')
            def star_roof(self):
                pass

        c = Car()
        c.leather = False
        c.star_roof = True

        tree = etree.fromstring(c.xml)
        
        paths = [
                '/Car/Interior/Leather',
                '/Car/Interior/StarRoof',
                ]

        for p in paths:
            self.assertEqual(len(tree.xpath(p)), 1)

    def test_name_element_separator(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def car_version(self):
                pass

            @xml.Element()
            def star_roof(self):
                pass

            @xml.Element(path='/front_seat')
            def warmer(self):
                pass

        c = Car()

        tree = etree.fromstring(c.xml)

        paths = [
                '/Car/@carVersion',
                '/Car/StarRoof',
                '/Car/FrontSeat/Warmer',
                ]

        for p in paths:
            self.assertEqual(len(tree.xpath(p)), 1)

    def test_path(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element(path='/interior')
            def leather(self):
                pass

        c = Car()
        c.leather = True

        tree = etree.fromstring(c.xml)
        xpath_result = tree.xpath('/Car/Interior/Leather')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0].text, 'True')

    def test_missing_nsmap(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(namespace='ford')

        c = Car()

        with self.assertRaises(xml.MissingNamespaceMapError):
            c.xml

    def test_namespace(self):
        nsmap = {
                'mercedes': 'http://mercedes.com',
                'xlink': 'http://w3.org/xlink',
                }

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(namespace='mercedes', nsmap=nsmap)

            @xml.Attribute(namespace='xlink')
            def color(self):
                pass

            @xml.Element(namespace='mercedes')
            def state(self):
                pass

        c = Car()

        tree = etree.fromstring(c.xml)

        paths = [
                '/mercedes:Car',
                '/mercedes:Car/@xlink:color',
                '/mercedes:Car/mercedes:State'
                ]

        for p in paths:
            self.assertEqual(len(tree.xpath(p, namespaces=nsmap)), 1)
    
    def test_add_element(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Element()
            def state(self):
                pass
        
        c = Car()
        
        # Check attribute was created and has settr/gettr
        self.assertTrue(hasattr(c, 'state'))
        c.state = 'driving'
        self.assertEqual(c.state, 'driving')

        tree = etree.fromstring(c.xml)
        xpath_result = tree.xpath('/Car/State')

        # check element was created and contains correct value
        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0].text, 'driving')
    
    def test_add_attribute(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            @xml.Attribute()
            def wheels(self):
                pass

        c = Car()

        # Check attribute was created and has settr/gettr
        self.assertTrue(hasattr(c, 'wheels'))
        c.wheels = 4
        self.assertEqual(c.wheels, 4)

        tree = etree.fromstring(c.xml)
        xpath_result = tree.xpath('/Car/@wheels')

        # check attribute was added and contains correct value
        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0], '4')

    def test_create_tree(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

        c = Car()

        tree = etree.fromstring(c.xml) 

        self.assertEqual(len(tree.xpath('/Car')), 1)

if __name__ == '__main__':
    unittest.main()
