#! /usr/bin/env python

import unittest
from lxml import etree

from esgf.wps_lib import xml

class XMLDocumentTest(unittest.TestCase):

    def test_multiple_value_type(self):
        class V8(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self, **kwargs):
                super(V8, self).__init__()

        class V6(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self, **kwargs):
                super(V6, self).__init__()

        class InlineV6(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self, **kwargs):
                super(InlineV6, self).__init__()
        
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self, **kwargs):
                super(Car, self).__init__()

            @xml.Element(value_type=(V8, V6))
            def engine(self):
                pass

        c = Car()
        c.engine = V8()

        document = c.xml()

        del c

        c = Car.from_xml(document)

        self.assertIsInstance(c.engine, V8)

        c.engine = InlineV6()

        document = c.xml()

        del c

        c = Car.from_xml(document)

        self.assertIsNone(c.engine)

    def test_element_boundaries(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element()
            def driver(self):
                pass

            @xml.Element(minimum=0, maximum=4, output_list=True, value_type=int)
            def passengers(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError) as e:
            c.xml()

        c.driver = ['tom', 'larry']

        with self.assertRaises(xml.ValidationError) as e:
            c.xml()

        c.driver = 'tom'

        c.passengers = [0, 1, 2, 3, 4]

        with self.assertRaises(xml.ValidationError) as e:
            c.xml()

        c.passengers = [0, 1, 2, 3]

        self.assertIsNotNone(c.xml())

    def test_attribute_required(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute(required=True)
            def speed(self):
                pass

        c = Car()

        with self.assertRaises(xml.ValidationError) as e:
            c.xml()

    def test_mismatch_types(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(value_type=int, output_list=True, maximum=3)
            def test(self):
                pass

        c = Car()
        c.test = [0, 'test', 3.3]

        with self.assertRaises(xml.MismatchedTypeError) as e:
            c.xml()

    def test_path_namespace(self):
        NSMAP = {'NS1': 'http://NS1'}

        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(nsmap=NSMAP)

            @xml.Element(path='driver', nsmap={'driver':'NS1'})
            def person(self):
                pass

        c = Car()
        c.person = 'larry'

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertEqual(len(tree.xpath('/Car/NS1:driver/person',
            namespaces=NSMAP)), 1)

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.person, 'larry')

    def test_path(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(path='driver')
            def person(self):
                pass

        c = Car()
        c.person = 'larry'

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertEqual(len(tree.xpath('/Car/driver/person')), 1)

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.person, 'larry')

    def test_store_attr(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(store_attr=True, name='href')
            def brochure(self):
                pass

        c = Car()
        c.brochure = 'http://test_brochure.com'

        document = c.xml()

        tree = etree.fromstring(document)

        xpath_result = tree.xpath('/Car/brochure/@href')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0], 'http://test_brochure.com')

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.brochure, 'http://test_brochure.com')

    def test_output_type_bad(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute(value_type=list)
            def speed(self):
                pass

        c = Car()
        c.speed = 45

        tree = c.xml()

        del c

        with self.assertRaises(xml.ValueConversionError) as e:
            c = Car.from_xml(tree)

    def test_output_type_attribute(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute(value_type=int)
            def speed(self):
                pass

            @xml.Attribute(value_type=float)
            def temperature(self):
                pass

            @xml.Attribute(value_type=long)
            def miles(self):
                pass

            @xml.Attribute(value_type=bool)
            def driving(self):
                pass

        c = Car()
        c.speed = 56
        c.temperature = 105.6
        c.miles = 121343234232
        c.driving = True

        tree = c.xml()

        del c

        c = Car.from_xml(tree)

        self.assertEqual(c.speed, 56)
        self.assertEqual(c.temperature, 105.6)
        self.assertEqual(c.miles, 121343234232)
        self.assertEqual(c.driving, True)

    def test_value_type_element(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(value_type=int)
            def speed(self):
                pass

            @xml.Element(value_type=float)
            def temperature(self):
                pass

            @xml.Element(value_type=long)
            def miles(self):
                pass

            @xml.Element(value_type=bool)
            def driving(self):
                pass

        c = Car()
        c.speed = 56
        c.temperature = 105.6
        c.miles = 121343234232
        c.driving = True

        tree = c.xml()

        del c

        c = Car.from_xml(tree)

        self.assertEqual(c.speed, 56)
        self.assertEqual(c.temperature, 105.6)
        self.assertEqual(c.miles, 121343234232)
        self.assertEqual(c.driving, True)

    def test_element_dict(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()
            
            @xml.Element()
            def random(self):
                pass

        c = Car()
        c.random = {
                'color': 'blue',
                'state': 'driving',
                'speed': 89,
                'new': True,
                }

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertEqual(len(tree.xpath('/Car/random/color')), 1)
        self.assertEqual(len(tree.xpath('/Car/random/state')), 1)
        self.assertEqual(len(tree.xpath('/Car/random/speed')), 1)
        self.assertEqual(len(tree.xpath('/Car/random/new')), 1)

        del c

        c = Car.from_xml(document)

    def test_element_list(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element(output_list=True, maximum=2)
            def years(self):
                pass

        c = Car()
        c.years = [1987, 1988]

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertEqual(len(tree.xpath('/Car/years')), 2)

        del c

        c = Car.from_xml(document)

        self.assertIsInstance(c.years, list)
        self.assertIn('1987', c.years)
        self.assertIn('1988', c.years)

    def test_missing_namespace_entry(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(namespace='car', nsmap={})

            @xml.Element(namespace='car', minimum=0)
            def state(self):
                pass

        c = Car()

        with self.assertRaises(xml.MissingNamespaceError) as e:
            c.xml()

    def test_missing_namespace_map(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(namespace='car')

            @xml.Element(namespace='car', minimum=0)
            def state(self):
                pass

        c = Car()

        with self.assertRaises(xml.MissingNamespaceError) as e:
            c.xml()

    def test_namespace(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            NSMAP = {
                    'car':'http://car',
                    'engine': 'http://engine',
                    'state': 'http://state',
                    }

            def __init__(self):
                super(Car, self).__init__(namespace='car', nsmap=Car.NSMAP)

            @xml.Attribute(namespace='state')
            def state(self):
                pass

            @xml.Element(namespace='engine')
            def engine(self):
                pass

        c = Car()
        c.engine = 'v8'
        c.state = 'driving'

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertEqual(len(tree.xpath('/car:Car/@state:state',
            namespaces=c.NSMAP)), 1)
        self.assertEqual(len(tree.xpath('/car:Car/engine:engine',
            namespaces=c.NSMAP)), 1)

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.state, 'driving')
        self.assertEqual(c.engine, 'v8')

    def test_attribute(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Attribute()
            def state(self):
                pass

        c = Car()
        c.state = 'Driving'

        document = c.xml()

        tree = etree.fromstring(document)

        xpath_result = tree.xpath('/Car/@state')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0], 'Driving')

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.state, 'Driving')

    def test_element(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

            @xml.Element()
            def engine(self):
                pass

        c = Car()
        c.engine = 'v8'

        document = c.xml()

        tree = etree.fromstring(document)

        xpath_result = tree.xpath('/Car/engine')

        self.assertEqual(len(xpath_result), 1)
        self.assertEqual(xpath_result[0].text, 'v8')

        del c

        c = Car.from_xml(document)

        self.assertEqual(c.engine, 'v8')

    def test_nsmap(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__(nsmap={'car':'http://car.com'})

        c = Car()

        document = c.xml()

        tree = etree.fromstring(document)

        self.assertIn('car', tree.nsmap)
        self.assertEqual(tree.nsmap['car'], 'http://car.com')

        del c

        c = Car.from_xml(document)

        self.assertIsInstance(c, Car)

    def test_base_tag(self):
        class Car(xml.XMLDocument):
            __metaclass__ = xml.XMLDocumentMarkupType

            def __init__(self):
                super(Car, self).__init__()

        c = Car()

        tree = etree.fromstring(c.xml())
        
        self.assertEqual(len(tree.xpath('/Car')), 1)

if __name__ == '__main__':
    unittest.main()
    #unittest.main(verbosity=10)
