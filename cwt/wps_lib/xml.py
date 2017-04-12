#! /usr/bin/env python

from __future__ import absolute_import

from lxml import etree
import inspect
import logging
import re
import sys

logger = logging.getLogger(__name__)

SUPPORTED_CONVERSION = (str, float, bool, int, long)

class XMLError(Exception):
    pass

class Translator(object):
    """ Base translator class.

    This class can be use to control how property names are transformed
    to xml element/attribute names and vica-versa.
    """
    def property_to_element(self, name):
        raise NotImplmenetedError()

    def property_to_attribute(self, name):
        raise NotImplmenetedError()

    def element_to_property(self, name):
        raise NotImplmenetedError()

    def element_to_attribute(self, name):
        raise NotImplmenetedError()

class Attribute(object):
    """ Attribute decorator.

    This decorator represents an xml attribute. If attach is not specified then
    the attribute will be created on the root element.

    Attributes:
        namespace: A str namespace identifier.
        value_type: A type that the attribute will hold. Default: str
        required: A bool flag denoting whether the attribute is required. Default: False
        attach: A str name of the element to set the attribute on.
    """
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
    """ Element decorator.

    This decorator represents an xml element.

    Examples of options.

        @Element(namespace='ns')
        def test(self): pass

        <ns:test />

        @Element(output_list=True)
        def test(self): pass

        <test>1</test>
        <test>2</test>

        @Element(child_tag='item', child_namespace='ns')
        def test(self): pass

        <test>
            <ns:item>1</ns:item>
        </test>

        @Element(attr='value')
        def test(self): pass

        <test value="1" />

        @Element(path='/hello/once/only', nsmap={'once': 'ns'})
        def test(self): pass

        <hello>
            <ns:once>
                <only>
                    <test>1</test>
                </only>
            </ns:once>
        </hello>

        # NOTE: if store_value is present it will be the only property used
        class Test(xml.XMLDocument):
            @Element(store_value=True)
            def test(self): pass

        <Test>1</Test>

    Attributes:
        namespace: A str namesapce identifier.
        output_list: A bool flag denoting wether the element has multiple children. Default: False
        child_tag: A str value to create an element to wrap the value in.
        child_namespace: A str namespace identifier for child_tag.
        attr: A str value to name the attribute to hold the value.
        path: A str path to nest the element under.
        nsmap: A dict namespace map for the path.
        value_type: A type that the element will hold. Default: str
        store_value: A bool flag denoting that the elements contents will be the value.
        minimum: An int setting the minimum number of items.
        maximum: An int setting the maximum number of items.
    """
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
    """ XMLDocumentMarkupType.

    This type must be used with XMLDocument class to create xml documents. 
    This metaclass will collected the elements and attribute from properties
    and attach them to the class.
    """
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
            if hasattr(value, 'metadata'):
                metadata = value.metadata

                if isinstance(metadata, Element):
                    if metadata.store_value and store_value is None:
                        store_value = key
                    
                    elements[key] = metadata
                else:
                    attributes[key] = metadata

                dct[key] = property(fget(key), fset(key))

        cls = super(XMLDocumentMarkupType, mcs).__new__(mcs, name, bases, dct)

        # Set default values for the properties
        for key, value in dct.iteritems():
            if hasattr(value, 'metadata'):
                metadata = value.metadata

                if metadata.output_list:
                    setattr(cls, key, [])
                else:
                    setattr(cls, key, None)

        cls.attributes = attributes
        cls.elements = elements
        cls.store_value = store_value

        return cls

# Error definitions
class XMLParseError(Exception):
    pass

class ValueConversionError(Exception):
    pass

class MissingNamespaceError(Exception):
    pass

class MismatchedTypeError(Exception):
    pass

class ValidationError(Exception):
    pass

class XMLDocument(object):
    """ XMLDocument class.
        
    This class must be inherited by as subclass. This works in conjunction with
    XMLDocumentMarkupType. Element and attribute decorators can be added to 
    method definitions to create a pseudo XML schema.

    class Car(XMLDocument):
        __metaclass__ = XMLDocumentMarkupType

        def __init__(self, **kwargs):
            super(Car, self).__init__(**kwargs)

        @Attribute()
        def color(self): pass

        @Element()
        def engine(self): pass

    c = Car(color='blue', engine='V8')

    print c.xml()

    <Car color="blue">
        <engine>V8</engine>
    </Car>

    Attributes:
        namespace: A str namespace identifier for the root element.
        nsmap: A dict mapping namespace identifiers to namespace urls.
        tag: A str value to be substituted for the class name as the root element name.
        translatpor: A Translator to be use in converting names.
        **kwargs: A dict of default property values.
    """
    def __init__(self, namespace=None, nsmap=None, tag=None, translator=None, **kwargs):
        self.namespace = namespace
        self.nsmap = nsmap
        self.tag = tag
        self.translator = translator

        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def from_xml(cls, data):
        doc = cls()

        try:
            tree = etree.fromstring(data)
        except Exception:
            raise XMLError('Failed to parse xml')

        doc.parse_xml(tree)

        return doc

    @classmethod
    def from_element(cls, element, translator):
        doc = cls()

        doc.translator = translator

        doc.parse_xml(element)

        return doc

    def validate(self):
        """ Validates the property values against their definitions.

        Elements bounds are validated as well as attribute requirements.

        Raise:
            ValidationError: An error occurred validating one of the properties.
        """
        for name, metadata in self.attributes.iteritems():
            if metadata.required:
                value = getattr(self, name)

                if value is None:
                    raise ValidationError('%s Attribute %s is required' %
                            (self.__class__.__name__, name,))

        for name, metadata in self.elements.iteritems():
            # Check property that stores a list
            if metadata.output_list:
                value = getattr(self, name)

                # Check the minimum
                if metadata.minimum > 0:
                    if not isinstance(value, (list, tuple)):
                        raise ValidationError('%s Element %s was expecting a '
                                'list or tuple of values' % (self.__class__.__name__, name,))
                    elif value is None or len(value) < metadata.minimum:
                        raise ValidationError('%s Element %s requires a minimum '
                                'of %s values' % (self.__class__.__name__, name, metadata.minimum))

                # Check the maximum
                if metadata.maximum is not None:
                    if len(value) > metadata.maximum:
                        raise ValidationError('%s Element %s requires max %s'
                                ' values, %s were provided' %
                                (self.__class__.__name__, name, metadata.maximum, len(value)))
            else:
                # Check if a single value is required
                if metadata.minimum > 0:
                    value = getattr(self, name)

                    if value is None:
                        raise ValidationError('%s Element %s requires atleast '
                                'one value' % (self.__class__.__name__, name,))
                    elif isinstance(value, (list, tuple)):
                        raise ValidationError('%s Element %s was expecting a '
                                'single value' % (self.__class__.__name__, name,))

    def __append_value(self, name, node, metadata):
        """ Appends a value to a property that stores a list.
        
        Args:
            name: A str name of the property.
            node: A etree.Element whose value will be converted and stored.
            metadata: A Element/Attribute of the property being stored.
        """
        # Check for an existing list or create a new one
        values = getattr(self, name)

        if values is None:
            values = []

        # Convert etree.Element to XMLDocument
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

    def __store_value(self, raw_name, name, node, metadata):
        """ Stores a node in a property.

        Args:
            raw_name: A str unformatted name for the node.
            name: A str formatted name for the node.
            node: A etree.Element whose value will be store.
            metadata: An Element/Attribute associatd with the property.
        """
        logger.debug('Storing value "%s", "%s", "%s"', name, node.tag, metadata)

        # Process a list or single value
        if metadata.output_list:
            self.__append_value(name, node, metadata)
        else:
            # Check if a variable typed value is being stored.
            if isinstance(metadata.value_type, (list, tuple)):
                try:
                    target = [x for x in metadata.value_type if x.__name__ == raw_name][0]
                except IndexError:
                    raise XMLParseError('Failed to find value_type for {0}'.format(raw_name))

                value = target.from_element(node, self.translator)
            elif issubclass(metadata.value_type, XMLDocument):
                value = metadata.value_type.from_element(node, self.translator)
            else:
                value = metadata.value_type(node.text)

            setattr(self, name, value)

    def __match_parent(self, node):
        """ Processes up the XML tree to find a parent who is a known property.

        Args:
            node: A etree.Element that is the starting node.

        Return:
            A tuple containing the etree.Element and Element of the parent.
        """
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
        """ Converts and stores a value in a property.

        Args:
            name: A str name of the property.
            value: A str value to be stored.
            metadata: An Element/Attribute that belongs to the property.
        """
        try:
            value = metadata.value_type(value)
        except ValueError:
            raise ValueConversionError('Could not convert from %s to %s' %
                    (value.__class__, metadata.value_type.__class__))

        setattr(self, name, value)

    def __match_element_value_type(self, tag):
        """ Find element by its value_type.

        Args:
            tag: A str name of the element name.

        Return:
            A tuple including the name of the property and its related metadata.
        """
        for name, metadata in self.elements.iteritems():
            candidates = metadata.value_type

            if not isinstance(candidates, (list, tuple)):
                candidates = [candidates]

            for c in candidates:
                if c.__name__ == tag:
                    return name, metadata

        return None, None

    def parse_xml(self, root):
        """ Parses an XML document according to the class definition.

        Args:
            root: An etree.Element being the root of the document.
        """
        # Remove the namespace
        cls_name = re.sub('^{.*}', '', root.tag)

        # Validate that we're parsing the correct class
        if not (cls_name == self.__class__.__name__ or
                (self.tag is not None and cls_name == self.tag)):
            raise ValidationError('XML does not match class definition: {} {} {}'.format(cls_name, self.tag, self.__class__.__name__))

        logger.debug('%s BEGIN PARSING "%s" %s', '#'*6, re.sub('^{.*}', '', root.tag), '#'*6)
        logger.debug(etree.tostring(root, pretty_print=True))
        logger.debug('Translator %s', self.translator)
        logger.debug('Known elements %s', self.elements.keys())

        # Process all the root attributes
        for name, value in root.attrib.iteritems():
            name = re.sub('^{.*}', '', name)

            if self.translator is not None:
                name = self.translator.attribute_to_property(name)

            if name in self.attributes:
                metadata = self.attributes[name]

                self.__set_property(name, value, metadata)

        # Process the XML tree using depth first search
        stack = [root]

        while len(stack):
            node = stack.pop()

            tag = node.tag

            name = re.sub('^{.*}', '', tag)
                
            # Translate the name if needed
            if self.translator is not None:
                trans_name = self.translator.element_to_property(name)
            else:
                trans_name = name
            
            logger.debug('Processing element "%s" (%s)', trans_name, name)

            # On non-root nodes check for attributes and store their values.
            if node != root:
                for atrans_name, value in node.attrib.iteritems():
                    if self.translator is not None:
                        atrans_name = self.translator.attribute_to_property(atrans_name)

                    if atrans_name in self.attributes:
                        metadata = self.attributes[atrans_name]

                        self.__set_property(atrans_name, value, metadata)

            # Check if the current node is defined in the class
            if trans_name in self.elements:
                metadata = self.elements[trans_name]

                logger.debug('Element "%s" is a known property %s', trans_name, metadata)

                # Process a property value that is stored as an attribute.
                if metadata.attr is not None:
                    if metadata.attr in node.attrib:
                        value = node.attrib[metadata.attr]

                        self.__set_property(node.tag, value, metadata)
                elif (metadata.child_tag is not None or
                    # Process child tags or multiple child tags
                        (metadata.output_list and
                            issubclass(metadata.value_type, XMLDocument) and
                            metadata.path is not None) or
                        isinstance(metadata.value_type, (list, tuple))):
                    for c in node.getchildren():
                        stack.append(c)
                else:
                    self.__store_value(name, trans_name, node, metadata)
            else:
                # Node is not a known property we try to process it according
                # to the rules or we just add it's children to the stack.
                logger.debug('Handling unknown element "%s"', name)

                match_trans_name, match_metadata = self.__match_element_value_type(name)

                logger.debug('Match element by value_type "%s": "%s"', match_trans_name, match_metadata)

                # Search for a defined element whos value_type matches the nodes
                # name. This is a case where value_type may accept multiple types.
                if match_trans_name is not None:
                    self.__store_value(name, match_trans_name, node, match_metadata)
                else:
                    handled = False

                    # Check to see if the an Element with store_value has been
                    # defined, and the value of the node should be stored.
                    for ename, emeta in self.elements.iteritems():
                        if emeta.store_value:
                            children = node.getchildren()

                            # Special case where the stored value is XML
                            if len(children) > 0:
                                value = '\n'.join(etree.tostring(x, pretty_print=True) for x in children)

                                setattr(self, ename, value)
                            else:
                                setattr(self, ename, node.text)

                            handled = True

                            break

                    if not handled:
                        # Last resort, run up the tree searching for a parent
                        # who can store the value
                        parent_element, parent_metadata = self.__match_parent(node)

                        if parent_element is not None:
                            self.__store_value(name, parent_element.tag, node, parent_metadata)
                        else:
                            # End of the line just append the child nodes to the
                            # stack
                            for c in node.getchildren():
                                stack.append(c)

        logger.debug('%s END PARSING "%s" %s', '#'*6, re.sub('^{.*}', '', root.tag), '#'*6)

    def __generate_name(self, name, namespace, metadata=None):
        """ Generate an Element/Attribute name.

        If a namespace is provided make sure it is present in the classes nsmap.

        Args:
            name: A str base name.
            namespace: A str namespace identifier.
            metadata: A Element/Attribute associated to the property

        Return:
             A str formatted Element/Attribute name

        Raises:
            MissingNamespaceError: The namespace is not present in the classes nsmap.
        """
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
        """ Creates a new element.
        
        Args:
            parent: An etree.Element that will be the parent of the new node.
            name: A str name of the new node.
            value: An object whos value will be stored.
            metadata: An Element/Attribute associated with the property.
            cache: A dict that will contain all the new nodes.

        Return:
            A new etree.Element.
        """
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
        """ Generate XML from class definition.

        Process the classes elements and attributes that have been declard to
        create an XML document.

        """
        # Validate all the document constraints
        self.validate()

        # Generate our root nodes name
        cls_name = self.__class__.__name__

        if self.tag is not None:
            cls_name = self.tag

        cls_name = self.__generate_name(cls_name, self.namespace)

        root = etree.Element(cls_name, nsmap=self.nsmap)

        cache = {}

        # Process all of the declared elements
        for name, metadata in self.elements.iteritems():
            parent = root

            # Contents of the root node will be only this value
            if metadata.store_value:
                value = getattr(self, name)

                root.text = value

                break

            # Create a path if declared
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

        # Process the attributes last since they may be attached to nodes
        # created by Elements that declared path values.
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
        """ Generate str XML document from etree.Element. """
        return etree.tostring(self.generate_xml(), pretty_print=True)
