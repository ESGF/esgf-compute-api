# ../../cwt/wps/raw/binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:76ad5258aae86a5ac0f3bea350c0ef82976f8647
# Generated 2018-04-13 19:53:04.788973 by PyXB version 1.2.6 using Python 2.7.14.final.0
# Namespace http://www.opengis.net/wps/1.0.0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f0a8799e-3f8e-11e8-b989-708bcda56936')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import cwt.wps.xlink as _ImportedBinding_cwt_wps_xlink
import pyxb.binding.datatypes
import cwt.wps.ows as _ImportedBinding_cwt_wps_ows
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/wps/1.0.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ows = _ImportedBinding_cwt_wps_ows.Namespace
_Namespace_ows.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding_cwt_wps_xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 303, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.GET = STD_ANON._CF_enumeration.addEnumeration(unicode_value='GET', tag='GET')
STD_ANON.POST = STD_ANON._CF_enumeration.addEnumeration(unicode_value='POST', tag='POST')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 198, 5)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.integer(0))
STD_ANON_._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.integer(99))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive,
   STD_ANON_._CF_maxInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Complex type {http://www.opengis.net/wps/1.0.0}DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Description of a WPS process or output object. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Title', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Abstract', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), 'Metadata', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    _ElementMap.update({
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescriptionType = DescriptionType
Namespace.addCategoryObject('typeBinding', 'DescriptionType', DescriptionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """List of the inputs to this process. In almost all cases, at least one process input is required. However, no process inputs may be identified when all the inputs are predetermined fixed resources.  In this case, those resources shall be identified in the ows:Abstract element that describes the process."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 55, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Input'), 'Input', '__httpwww_opengis_netwps1_0_0_CTD_ANON_Input', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 57, 8), )

    
    Input = property(__Input.value, __Input.set, None, 'Unordered list of one or more descriptions of the inputs that can be accepted by this process, including all required and optional inputs.  Where an input is optional because a default value exists, that default value must be identified in the "ows:Abstract" element for that input, except in the case of LiteralData, where the default must be indicated in the corresponding ows:DefaultValue element. Where an input is optional because it depends on the value(s) of other inputs, this must be indicated in the ows:Abstract element for that input. ')

    _ElementMap.update({
        __Input.name() : __Input
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """List of outputs which will or can result from executing the process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 69, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_CTD_ANON__Output', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 71, 8), )

    
    Output = property(__Output.value, __Output.set, None, 'Unordered list of one or more descriptions of all the outputs that can result from executing this process. At least one output is required from each process. ')

    _ElementMap.update({
        __Output.name() : __Output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.opengis.net/wps/1.0.0}ValuesReferenceType with content type EMPTY
class ValuesReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """References an externally defined finite set of values and ranges for this input. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValuesReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ows, 'reference'), 'reference', '__httpwww_opengis_netwps1_0_0_ValuesReferenceType_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 250, 1)
    __reference._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 193, 2)
    
    reference = property(__reference.value, __reference.set, None, 'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')

    
    # Attribute valuesForm uses Python identifier valuesForm
    __valuesForm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'valuesForm'), 'valuesForm', '__httpwww_opengis_netwps1_0_0_ValuesReferenceType_valuesForm', pyxb.binding.datatypes.anyURI)
    __valuesForm._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 194, 2)
    __valuesForm._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 194, 2)
    
    valuesForm = property(__valuesForm.value, __valuesForm.set, None, 'Reference to a description of the mimetype, encoding, and schema used for this set of values and ranges.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference.name() : __reference,
        __valuesForm.name() : __valuesForm
    })
_module_typeBindings.ValuesReferenceType = ValuesReferenceType
Namespace.addCategoryObject('typeBinding', 'ValuesReferenceType', ValuesReferenceType)


# Complex type {http://www.opengis.net/wps/1.0.0}SupportedUOMsType with content type ELEMENT_ONLY
class SupportedUOMsType (pyxb.binding.basis.complexTypeDefinition):
    """Listing of the Unit of Measure (U0M) support for this process input or output. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedUOMsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 217, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedUOMsType_Default', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 222, 3), )

    
    Default = property(__Default.value, __Default.set, None, 'Reference to the default UOM supported for this input or output, if UoM is applicable. The process shall expect input in or produce output in this UOM unless the Execute request specifies another supported UOM. ')

    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedUOMsType_Supported', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 236, 3), )

    
    Supported = property(__Supported.value, __Supported.set, None, 'Unordered list of references to all of the UOMs supported for this input or output, if UOM is applicable. The default UOM shall be included in this list. ')

    _ElementMap.update({
        __Default.name() : __Default,
        __Supported.name() : __Supported
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupportedUOMsType = SupportedUOMsType
Namespace.addCategoryObject('typeBinding', 'SupportedUOMsType', SupportedUOMsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Reference to the default UOM supported for this input or output, if UoM is applicable. The process shall expect input in or produce output in this UOM unless the Execute request specifies another supported UOM. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 226, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), 'UOM', '__httpwww_opengis_netwps1_0_0_CTD_ANON_2_httpwww_opengis_netows1_1UOM', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1), )

    
    UOM = property(__UOM.value, __UOM.set, None, 'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')

    _ElementMap.update({
        __UOM.name() : __UOM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.opengis.net/wps/1.0.0}UOMsType with content type ELEMENT_ONLY
class UOMsType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies a UOM supported for this input or output."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UOMsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 244, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), 'UOM', '__httpwww_opengis_netwps1_0_0_UOMsType_httpwww_opengis_netows1_1UOM', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1), )

    
    UOM = property(__UOM.value, __UOM.set, None, 'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')

    _ElementMap.update({
        __UOM.name() : __UOM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UOMsType = UOMsType
Namespace.addCategoryObject('typeBinding', 'UOMsType', UOMsType)


# Complex type {http://www.opengis.net/wps/1.0.0}SupportedCRSsType with content type ELEMENT_ONLY
class SupportedCRSsType (pyxb.binding.basis.complexTypeDefinition):
    """Listing of the Coordinate Reference System (CRS) support for this process input or output. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedCRSsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 257, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedCRSsType_Default', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 262, 3), )

    
    Default = property(__Default.value, __Default.set, None, 'Identifies the default CRS that will be used unless the Execute operation request specifies another supported CRS. ')

    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedCRSsType_Supported', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 276, 3), )

    
    Supported = property(__Supported.value, __Supported.set, None, 'Unordered list of references to all of the CRSs supported for this Input/Output. The default CRS shall be included in this list.')

    _ElementMap.update({
        __Default.name() : __Default,
        __Supported.name() : __Supported
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupportedCRSsType = SupportedCRSsType
Namespace.addCategoryObject('typeBinding', 'SupportedCRSsType', SupportedCRSsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Identifies the default CRS that will be used unless the Execute operation request specifies another supported CRS. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 266, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CRS'), 'CRS', '__httpwww_opengis_netwps1_0_0_CTD_ANON_3_CRS', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 268, 6), )

    
    CRS = property(__CRS.value, __CRS.set, None, 'Reference to the default CRS supported for this Input/Output')

    _ElementMap.update({
        __CRS.name() : __CRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.opengis.net/wps/1.0.0}CRSsType with content type ELEMENT_ONLY
class CRSsType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies a Coordinate Reference System (CRS) supported for this input or output."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CRSsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 284, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CRS'), 'CRS', '__httpwww_opengis_netwps1_0_0_CRSsType_CRS', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 289, 3), )

    
    CRS = property(__CRS.value, __CRS.set, None, 'Reference to a CRS supported for this Input/Output. ')

    _ElementMap.update({
        __CRS.name() : __CRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CRSsType = CRSsType
Namespace.addCategoryObject('typeBinding', 'CRSsType', CRSsType)


# Complex type {http://www.opengis.net/wps/1.0.0}SupportedComplexDataType with content type ELEMENT_ONLY
class SupportedComplexDataType (pyxb.binding.basis.complexTypeDefinition):
    """Formats, encodings, and schemas supported by a process input or output. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedComplexDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 297, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataType_Default', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 302, 3), )

    
    Default = property(__Default.value, __Default.set, None, 'Identifies the default combination of Format, Encoding, and Schema supported for this Input/Output. The process shall expect input in or produce output in this combination of MimeType/Encoding/Schema unless the Execute request specifies otherwise.  ')

    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataType_Supported', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 307, 3), )

    
    Supported = property(__Supported.value, __Supported.set, None, 'Unordered list of combinations of format, encoding, and schema supported for this Input/Output. This element shall be repeated for each combination of MimeType/Encoding/Schema that is supported for this Input/Output. This list shall include the default MimeType/Encoding/Schema. ')

    _ElementMap.update({
        __Default.name() : __Default,
        __Supported.name() : __Supported
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupportedComplexDataType = SupportedComplexDataType
Namespace.addCategoryObject('typeBinding', 'SupportedComplexDataType', SupportedComplexDataType)


# Complex type {http://www.opengis.net/wps/1.0.0}ComplexDataCombinationType with content type ELEMENT_ONLY
class ComplexDataCombinationType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies the default Format, Encoding, and Schema supported for this input or output. The process shall expect input in or produce output in this combination of Format/Encoding/Schema unless the Execute request specifies otherwise.. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexDataCombinationType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 315, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Format'), 'Format', '__httpwww_opengis_netwps1_0_0_ComplexDataCombinationType_Format', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 320, 3), )

    
    Format = property(__Format.value, __Format.set, None, 'The default combination of MimeType/Encoding/Schema supported for this Input/Output. ')

    _ElementMap.update({
        __Format.name() : __Format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComplexDataCombinationType = ComplexDataCombinationType
Namespace.addCategoryObject('typeBinding', 'ComplexDataCombinationType', ComplexDataCombinationType)


# Complex type {http://www.opengis.net/wps/1.0.0}ComplexDataCombinationsType with content type ELEMENT_ONLY
class ComplexDataCombinationsType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies valid combinations of Format, Encoding, and Schema supported for this input or output. The process shall expect input in or produce output in this combination of Format/Encoding/Schema unless the Execute request specifies otherwise.. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexDataCombinationsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 328, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Format'), 'Format', '__httpwww_opengis_netwps1_0_0_ComplexDataCombinationsType_Format', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 333, 3), )

    
    Format = property(__Format.value, __Format.set, None, 'A valid combination of MimeType/Encoding/Schema supported for this Input/Output. ')

    _ElementMap.update({
        __Format.name() : __Format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComplexDataCombinationsType = ComplexDataCombinationsType
Namespace.addCategoryObject('typeBinding', 'ComplexDataCombinationsType', ComplexDataCombinationsType)


# Complex type {http://www.opengis.net/wps/1.0.0}ComplexDataDescriptionType with content type ELEMENT_ONLY
class ComplexDataDescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """A combination of format, encoding, and/or schema supported by a process input or output. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexDataDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 341, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MimeType uses Python identifier MimeType
    __MimeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MimeType'), 'MimeType', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_MimeType', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 346, 3), )

    
    MimeType = property(__MimeType.value, __MimeType.set, None, 'Mime type supported for this input or output (e.g., text/xml). ')

    
    # Element Encoding uses Python identifier Encoding
    __Encoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Encoding'), 'Encoding', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_Encoding', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 351, 3), )

    
    Encoding = property(__Encoding.value, __Encoding.set, None, 'Reference to an encoding supported for this input or output (e.g., UTF-8).  This element shall be omitted if Encoding does not apply to this Input/Output. ')

    
    # Element Schema uses Python identifier Schema
    __Schema = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Schema'), 'Schema', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_Schema', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 356, 3), )

    
    Schema = property(__Schema.value, __Schema.set, None, 'Reference to a definition of XML elements or types supported for this Input/Output (e.g., GML 2.1 Application Schema). Each of these XML elements or types shall be defined in a separate XML Schema Document. This parameter shall be included when this input/output is XML encoded using an XML schema. When included, the input/output shall validate against the referenced XML Schema. This element shall be omitted if Schema does not apply to this Input/Output. Note: If the Input/Output uses a profile of a larger schema, the server administrator should provide that schema profile for validation purposes. ')

    _ElementMap.update({
        __MimeType.name() : __MimeType,
        __Encoding.name() : __Encoding,
        __Schema.name() : __Schema
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ComplexDataDescriptionType = ComplexDataDescriptionType
Namespace.addCategoryObject('typeBinding', 'ComplexDataDescriptionType', ComplexDataDescriptionType)


# Complex type {http://www.opengis.net/wps/1.0.0}LiteralOutputType with content type ELEMENT_ONLY
class LiteralOutputType (pyxb.binding.basis.complexTypeDefinition):
    """Description of a literal output (or input). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiteralOutputType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 403, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType'), 'DataType', '__httpwww_opengis_netwps1_0_0_LiteralOutputType_httpwww_opengis_netows1_1DataType', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 262, 1), )

    
    DataType = property(__DataType.value, __DataType.set, None, 'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')

    
    # Element UOMs uses Python identifier UOMs
    __UOMs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UOMs'), 'UOMs', '__httpwww_opengis_netwps1_0_0_LiteralOutputType_UOMs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3), )

    
    UOMs = property(__UOMs.value, __UOMs.set, None, 'List of supported units of measure for this input or output. This element should be included when this literal has a unit of measure (e.g., "meters", without a more complete reference system). Not necessary for a count, which has no units. ')

    _ElementMap.update({
        __DataType.name() : __DataType,
        __UOMs.name() : __UOMs
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LiteralOutputType = LiteralOutputType
Namespace.addCategoryObject('typeBinding', 'LiteralOutputType', LiteralOutputType)


# Complex type {http://www.opengis.net/wps/1.0.0}DataInputsType with content type ELEMENT_ONLY
class DataInputsType (pyxb.binding.basis.complexTypeDefinition):
    """List of the Inputs provided as part of the Execute Request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataInputsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 53, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Input'), 'Input', '__httpwww_opengis_netwps1_0_0_DataInputsType_httpwww_opengis_netwps1_0_0Input', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 58, 3), )

    
    Input = property(__Input.value, __Input.set, None, 'Unordered list of one or more inputs to be used by the process, including each of the Inputs needed to execute the process. ')

    _ElementMap.update({
        __Input.name() : __Input
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DataInputsType = DataInputsType
Namespace.addCategoryObject('typeBinding', 'DataInputsType', DataInputsType)


# Complex type {http://www.opengis.net/wps/1.0.0}ResponseFormType with content type ELEMENT_ONLY
class ResponseFormType (pyxb.binding.basis.complexTypeDefinition):
    """Defines the response type of the WPS, either raw data or XML document"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponseFormType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ResponseDocument uses Python identifier ResponseDocument
    __ResponseDocument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseDocument'), 'ResponseDocument', '__httpwww_opengis_netwps1_0_0_ResponseFormType_httpwww_opengis_netwps1_0_0ResponseDocument', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 71, 3), )

    
    ResponseDocument = property(__ResponseDocument.value, __ResponseDocument.set, None, 'Indicates that the outputs shall be returned as part of a WPS response document.')

    
    # Element {http://www.opengis.net/wps/1.0.0}RawDataOutput uses Python identifier RawDataOutput
    __RawDataOutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RawDataOutput'), 'RawDataOutput', '__httpwww_opengis_netwps1_0_0_ResponseFormType_httpwww_opengis_netwps1_0_0RawDataOutput', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 76, 3), )

    
    RawDataOutput = property(__RawDataOutput.value, __RawDataOutput.set, None, 'Indicates that the output shall be returned directly as raw data, without a WPS response document.')

    _ElementMap.update({
        __ResponseDocument.name() : __ResponseDocument,
        __RawDataOutput.name() : __RawDataOutput
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponseFormType = ResponseFormType
Namespace.addCategoryObject('typeBinding', 'ResponseFormType', ResponseFormType)


# Complex type {http://www.opengis.net/wps/1.0.0}ResponseDocumentType with content type ELEMENT_ONLY
class ResponseDocumentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/wps/1.0.0}ResponseDocumentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponseDocumentType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 84, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_httpwww_opengis_netwps1_0_0Output', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 86, 3), )

    
    Output = property(__Output.value, __Output.set, None, 'Unordered list of definitions of the outputs (or parameters) requested from the process. These outputs are not normally identified, unless the client is specifically requesting a limited subset of outputs, and/or is requesting output formats and/or schemas and/or encodings different from the defaults and selected from the alternatives identified in the process description, or wishes to customize the descriptive information about the output. ')

    
    # Attribute storeExecuteResponse uses Python identifier storeExecuteResponse
    __storeExecuteResponse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'storeExecuteResponse'), 'storeExecuteResponse', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_storeExecuteResponse', pyxb.binding.datatypes.boolean, unicode_default='false')
    __storeExecuteResponse._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 92, 2)
    __storeExecuteResponse._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 92, 2)
    
    storeExecuteResponse = property(__storeExecuteResponse.value, __storeExecuteResponse.set, None, 'Indicates if the execute response document shall be stored.  If "true" then the executeResponseLocation attribute in the execute response becomes mandatory, which will point to the location where the executeResponseDocument is stored.  The service shall respond immediately to the request and return an executeResponseDocument containing the executeResponseLocation and the status element which has five possible subelements (choice):ProcessAccepted, ProcessStarted, ProcessPaused, ProcessFailed and ProcessSucceeded, which are chosen and populated as follows:   1) If the process is completed when the initial executeResponseDocument is returned, the element ProcessSucceeded is populated with the process results.  2) If the process already failed when the initial executeResponseDocument is returned, the element ProcessFailed is populated with the Exception.  3) If the process has been paused when the initial executeResponseDocument is returned, the element ProcessPaused is populated.  4) If the process has been accepted when the initial executeResponseDocument is returned, the element ProcessAccepted is populated, including percentage information. 5) If the process execution is ongoing when the initial executeResponseDocument is returned, the element ProcessStarted is populated.  In case 3, 4, and 5, if status updating is requested, updates are made to the executeResponseDocument at the executeResponseLocation until either the process completes successfully or fails.  Regardless, once the process completes successfully, the ProcessSucceeded element is populated, and if it fails, the ProcessFailed element is populated.Specifies if the Execute operation response shall be returned quickly with status information, or not returned until process execution is complete. This parameter shall not be included unless the corresponding "statusSupported" parameter is included and is "true" in the ProcessDescription for this process. ')

    
    # Attribute lineage uses Python identifier lineage
    __lineage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lineage'), 'lineage', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_lineage', pyxb.binding.datatypes.boolean, unicode_default='false')
    __lineage._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 98, 2)
    __lineage._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 98, 2)
    
    lineage = property(__lineage.value, __lineage.set, None, 'Indicates if the Execute operation response shall include the DataInputs and OutputDefinitions elements.  If lineage is "true" the server shall include in the execute response a complete copy of the DataInputs and OutputDefinition elements as received in the execute request.  If lineage is "false" then these elements shall be omitted from the response.  ')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_status', pyxb.binding.datatypes.boolean, unicode_default='false')
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 103, 2)
    __status._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 103, 2)
    
    status = property(__status.value, __status.set, None, 'Indicates if the stored execute response document shall be updated to provide ongoing reports on the status of execution.  If status is "true" and storeExecuteResponse is "true" (and the server has indicated that both storeSupported and statusSupported are "true")  then the Status element of the execute response document stored at executeResponseLocation is kept up to date by the process.  While the execute response contains ProcessAccepted, ProcessStarted, or ProcessPaused, updates shall be made to the executeResponse document until either the process completes successfully (in which case ProcessSucceeded is populated), or the process fails (in which case ProcessFailed is populated).  If status is "false" then the Status element shall not be updated until the process either completes successfully or fails.  If status="true" and storeExecuteResponse is "false" then the service shall raise an exception.')

    _ElementMap.update({
        __Output.name() : __Output
    })
    _AttributeMap.update({
        __storeExecuteResponse.name() : __storeExecuteResponse,
        __lineage.name() : __lineage,
        __status.name() : __status
    })
_module_typeBindings.ResponseDocumentType = ResponseDocumentType
Namespace.addCategoryObject('typeBinding', 'ResponseDocumentType', ResponseDocumentType)


# Complex type {http://www.opengis.net/wps/1.0.0}InputType with content type ELEMENT_ONLY
class InputType (pyxb.binding.basis.complexTypeDefinition):
    """Value of one input to a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 182, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Title', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Abstract', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netwps1_0_0Reference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 215, 3), )

    
    Reference = property(__Reference.value, __Reference.set, None, 'Identifies this input value as a web accessible resource, and references that resource. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Data'), 'Data', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netwps1_0_0Data', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 220, 3), )

    
    Data = property(__Data.value, __Data.set, None, 'Identifies this input value as a data embedded in this request, and includes that data. ')

    _ElementMap.update({
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __Identifier.name() : __Identifier,
        __Reference.name() : __Reference,
        __Data.name() : __Data
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InputType = InputType
Namespace.addCategoryObject('typeBinding', 'InputType', InputType)


# Complex type {http://www.opengis.net/wps/1.0.0}DataType with content type ELEMENT_ONLY
class DataType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies the form of this input or output value, and provides supporting information. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 228, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ComplexData uses Python identifier ComplexData
    __ComplexData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComplexData'), 'ComplexData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0ComplexData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 233, 3), )

    
    ComplexData = property(__ComplexData.value, __ComplexData.set, None, 'Identifies this input or output value as a complex data structure encoded in XML (e.g., using GML), and provides that complex data structure. For an input, this element may be used by a client for any process input coded as ComplexData in the ProcessDescription. For an output, this element shall be used by a server when "store" in the Execute request is "false". ')

    
    # Element {http://www.opengis.net/wps/1.0.0}LiteralData uses Python identifier LiteralData
    __LiteralData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LiteralData'), 'LiteralData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0LiteralData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 238, 3), )

    
    LiteralData = property(__LiteralData.value, __LiteralData.set, None, 'Identifies this input or output data as literal data of a simple quantity (e.g., one number), and provides that data. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}BoundingBoxData uses Python identifier BoundingBoxData
    __BoundingBoxData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxData'), 'BoundingBoxData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0BoundingBoxData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 243, 3), )

    
    BoundingBoxData = property(__BoundingBoxData.value, __BoundingBoxData.set, None, 'Identifies this input or output data as an ows:BoundingBox data structure, and provides that ows:BoundingBox data. ')

    _ElementMap.update({
        __ComplexData.name() : __ComplexData,
        __LiteralData.name() : __LiteralData,
        __BoundingBoxData.name() : __BoundingBoxData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DataType = DataType
Namespace.addCategoryObject('typeBinding', 'DataType', DataType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Extra HTTP request headers needed by the service identified in ../Reference/@href.  For example, an HTTP SOAP request requires a SOAPAction header.  This permits the creation of a complete and valid POST request."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 261, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__httpwww_opengis_netwps1_0_0_CTD_ANON_4_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 262, 5)
    __key._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 262, 5)
    
    key = property(__key.value, __key.set, None, 'Key portion of the Key-Value pair in the HTTP request header.')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpwww_opengis_netwps1_0_0_CTD_ANON_4_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 267, 5)
    __value._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 267, 5)
    
    value_ = property(__value.value, __value.set, None, 'Value portion of the Key-Value pair in the HTTP request header.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __key.name() : __key,
        __value.name() : __value
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://www.opengis.net/wps/1.0.0}LiteralDataType with content type SIMPLE
class LiteralDataType (pyxb.binding.basis.complexTypeDefinition):
    """One simple literal value (such as an integer or real number) that is embedded in the Execute operation request or response. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiteralDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 324, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dataType'), 'dataType', '__httpwww_opengis_netwps1_0_0_LiteralDataType_dataType', pyxb.binding.datatypes.anyURI)
    __dataType._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 333, 4)
    __dataType._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 333, 4)
    
    dataType = property(__dataType.value, __dataType.set, None, 'Identifies the data type of this literal input or output. This dataType should be included for each quantity whose value is not a simple string. ')

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netwps1_0_0_LiteralDataType_uom', pyxb.binding.datatypes.anyURI)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 338, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 338, 4)
    
    uom = property(__uom.value, __uom.set, None, 'Identifies the unit of measure of this literal input or output. This unit of measure should be referenced for any numerical value that has units (e.g., "meters", but not a more complete reference system). Shall be a UOM identified in the Process description for this input or output. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __dataType.name() : __dataType,
        __uom.name() : __uom
    })
_module_typeBindings.LiteralDataType = LiteralDataType
Namespace.addCategoryObject('typeBinding', 'LiteralDataType', LiteralDataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """List of values of the Process output parameters. Normally there would be at least one output when the process has completed successfully. If the process has not finished executing, the implementer can choose to include whatever final results are ready at the time the Execute response is provided. If the reference locations of outputs are known in advance, these URLs may be provided before they are populated. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 59, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_CTD_ANON_5_httpwww_opengis_netwps1_0_0Output', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 61, 9), )

    
    Output = property(__Output.value, __Output.set, None, 'Unordered list of values of all the outputs produced by this process. It is not necessary to include an output until the Status is ProcessSucceeded. ')

    _ElementMap.update({
        __Output.name() : __Output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {http://www.opengis.net/wps/1.0.0}OutputDefinitionsType with content type ELEMENT_ONLY
class OutputDefinitionsType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of a format, encoding,  schema, and unit-of-measure for an output to be returned from a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputDefinitionsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 85, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_OutputDefinitionsType_httpwww_opengis_netwps1_0_0Output', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 90, 3), )

    
    Output = property(__Output.value, __Output.set, None, 'Output definition as provided in the execute request ')

    _ElementMap.update({
        __Output.name() : __Output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OutputDefinitionsType = OutputDefinitionsType
Namespace.addCategoryObject('typeBinding', 'OutputDefinitionsType', OutputDefinitionsType)


# Complex type {http://www.opengis.net/wps/1.0.0}StatusType with content type ELEMENT_ONLY
class StatusType (pyxb.binding.basis.complexTypeDefinition):
    """Description of the status of process execution. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatusType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 147, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessAccepted uses Python identifier ProcessAccepted
    __ProcessAccepted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessAccepted'), 'ProcessAccepted', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessAccepted', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 152, 3), )

    
    ProcessAccepted = property(__ProcessAccepted.value, __ProcessAccepted.set, None, 'Indicates that this process has been accepted by the server, but is in a queue and has not yet started to execute. The contents of this human-readable text string is left open to definition by each server implementation, but is expected to include any messages the server may wish to let the clients know. Such information could include how long the queue is, or any warning conditions that may have been encountered. The client may display this text to a human user. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessStarted uses Python identifier ProcessStarted
    __ProcessStarted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessStarted'), 'ProcessStarted', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessStarted', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 157, 3), )

    
    ProcessStarted = property(__ProcessStarted.value, __ProcessStarted.set, None, 'Indicates that this process has been accepted by the server, and processing has begun. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessPaused uses Python identifier ProcessPaused
    __ProcessPaused = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessPaused'), 'ProcessPaused', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessPaused', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 162, 3), )

    
    ProcessPaused = property(__ProcessPaused.value, __ProcessPaused.set, None, 'Indicates that this process has been  accepted by the server, and processing has started but subsequently been paused by the server.')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessSucceeded uses Python identifier ProcessSucceeded
    __ProcessSucceeded = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessSucceeded'), 'ProcessSucceeded', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessSucceeded', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 167, 3), )

    
    ProcessSucceeded = property(__ProcessSucceeded.value, __ProcessSucceeded.set, None, 'Indicates that this process has successfully completed execution. The contents of this human-readable text string is left open to definition by each server, but is expected to include any messages the server may wish to let the clients know, such as how long the process took to execute, or any warning conditions that may have been encountered. The client may display this text string to a human user. The client should make use of the presence of this element to trigger automated or manual access to the results of the process. If manual access is intended, the client should use the presence of this element to present the results as downloadable links to the user. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessFailed uses Python identifier ProcessFailed
    __ProcessFailed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessFailed'), 'ProcessFailed', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessFailed', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 172, 3), )

    
    ProcessFailed = property(__ProcessFailed.value, __ProcessFailed.set, None, 'Indicates that execution of this process has failed, and includes error information. ')

    
    # Attribute creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationTime'), 'creationTime', '__httpwww_opengis_netwps1_0_0_StatusType_creationTime', pyxb.binding.datatypes.dateTime, required=True)
    __creationTime._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 178, 2)
    __creationTime._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 178, 2)
    
    creationTime = property(__creationTime.value, __creationTime.set, None, 'The time (UTC) that the process finished.  If the process is still executing or awaiting execution, this element shall contain the creation time of this document.')

    _ElementMap.update({
        __ProcessAccepted.name() : __ProcessAccepted,
        __ProcessStarted.name() : __ProcessStarted,
        __ProcessPaused.name() : __ProcessPaused,
        __ProcessSucceeded.name() : __ProcessSucceeded,
        __ProcessFailed.name() : __ProcessFailed
    })
    _AttributeMap.update({
        __creationTime.name() : __creationTime
    })
_module_typeBindings.StatusType = StatusType
Namespace.addCategoryObject('typeBinding', 'StatusType', StatusType)


# Complex type {http://www.opengis.net/wps/1.0.0}ProcessFailedType with content type ELEMENT_ONLY
class ProcessFailedType (pyxb.binding.basis.complexTypeDefinition):
    """Indicator that the process has failed to execute successfully. The reason for failure is given in the exception report. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessFailedType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ExceptionReport uses Python identifier ExceptionReport
    __ExceptionReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'ExceptionReport'), 'ExceptionReport', '__httpwww_opengis_netwps1_0_0_ProcessFailedType_httpwww_opengis_netows1_1ExceptionReport', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 23, 1), )

    
    ExceptionReport = property(__ExceptionReport.value, __ExceptionReport.set, None, 'Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ')

    _ElementMap.update({
        __ExceptionReport.name() : __ExceptionReport
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessFailedType = ProcessFailedType
Namespace.addCategoryObject('typeBinding', 'ProcessFailedType', ProcessFailedType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Listing of the default and other languages supported by this service. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 58, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0Default', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 60, 4), )

    
    Default = property(__Default.value, __Default.set, None, 'Identifies the default language that will be used unless the operation request specifies another supported language. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0Supported', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 74, 4), )

    
    Supported = property(__Supported.value, __Supported.set, None, 'Unordered list of references to all of the languages supported by this service. The default language shall be included in this list.')

    _ElementMap.update({
        __Default.name() : __Default,
        __Supported.name() : __Supported
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Identifies the default language that will be used unless the operation request specifies another supported language. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 64, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language'), 'Language', '__httpwww_opengis_netwps1_0_0_CTD_ANON_7_httpwww_opengis_netows1_1Language', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 122, 1), )

    
    Language = property(__Language.value, __Language.set, None, 'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ')

    _ElementMap.update({
        __Language.name() : __Language
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type {http://www.opengis.net/wps/1.0.0}LanguagesType with content type ELEMENT_ONLY
class LanguagesType (pyxb.binding.basis.complexTypeDefinition):
    """Identifies a list of languages supported by this service."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguagesType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 83, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language'), 'Language', '__httpwww_opengis_netwps1_0_0_LanguagesType_httpwww_opengis_netows1_1Language', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 122, 1), )

    
    Language = property(__Language.value, __Language.set, None, 'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ')

    _ElementMap.update({
        __Language.name() : __Language
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LanguagesType = LanguagesType
Namespace.addCategoryObject('typeBinding', 'LanguagesType', LanguagesType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """List of brief descriptions of the processes offered by this WPS server. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Process uses Python identifier Process
    __Process = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Process'), 'Process', '__httpwww_opengis_netwps1_0_0_CTD_ANON_8_httpwww_opengis_netwps1_0_0Process', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 102, 4), )

    
    Process = property(__Process.value, __Process.set, None, 'Unordered list of one or more brief descriptions of all the processes offered by this WPS server. ')

    _ElementMap.update({
        __Process.name() : __Process
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {http://www.opengis.net/wps/1.0.0}ProcessBriefType with content type ELEMENT_ONLY
class ProcessBriefType (DescriptionType):
    """Complex type {http://www.opengis.net/wps/1.0.0}ProcessBriefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessBriefType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 24, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element {http://www.opengis.net/wps/1.0.0}Profile uses Python identifier Profile
    __Profile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Profile'), 'Profile', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0Profile', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5), )

    
    Profile = property(__Profile.value, __Profile.set, None, 'Optional unordered list of application profiles to which this process complies.')

    
    # Element {http://www.opengis.net/wps/1.0.0}WSDL uses Python identifier WSDL
    __WSDL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WSDL'), 'WSDL', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0WSDL', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 17, 1), )

    
    WSDL = property(__WSDL.value, __WSDL.set, None, 'Location of a WSDL document.')

    
    # Attribute {http://www.opengis.net/wps/1.0.0}processVersion uses Python identifier processVersion
    __processVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'processVersion'), 'processVersion', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0processVersion', pyxb.binding.datatypes.string, required=True)
    __processVersion._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessVersion.xsd', 20, 1)
    __processVersion._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 39, 4)
    
    processVersion = property(__processVersion.value, __processVersion.set, None, 'Release version of this Process, included when a process version needs to be included for clarification about the process to be used. It is possible that a WPS supports a process with different versions due to reasons such as modifications of process algorithms.  Notice that this is the version identifier for the process, not the version of the WPS interface. The processVersion is informative only.  Version negotiation for processVersion is not available.  Requests to Execute a process do not include a processVersion identifier.')

    _ElementMap.update({
        __Profile.name() : __Profile,
        __WSDL.name() : __WSDL
    })
    _AttributeMap.update({
        __processVersion.name() : __processVersion
    })
_module_typeBindings.ProcessBriefType = ProcessBriefType
Namespace.addCategoryObject('typeBinding', 'ProcessBriefType', ProcessBriefType)


# Complex type {http://www.opengis.net/wps/1.0.0}RequestBaseType with content type EMPTY
class RequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    """WPS operation request base, for all WPS operations except GetCapabilities. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwps1_0_0_RequestBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default='WPS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 25, 2)
    __service._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 25, 2)
    
    service = property(__service.value, __service.set, None, 'Service type identifier (WPS)')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netwps1_0_0_RequestBaseType_version', _ImportedBinding_cwt_wps_ows.VersionType, fixed=True, unicode_default='1.0.0', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 30, 2)
    __version._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 30, 2)
    
    version = property(__version.value, __version.set, None, 'Version of the WPS interface specification implemented by the server (1.0.0)')

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__httpwww_opengis_netwps1_0_0_RequestBaseType_language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 35, 2)
    __language._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/RequestBaseType.xsd', 35, 2)
    
    language = property(__language.value, __language.set, None, 'RFC 4646 language code of the human-readable text (e.g. "en-CA").')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version,
        __language.name() : __language
    })
_module_typeBindings.RequestBaseType = RequestBaseType
Namespace.addCategoryObject('typeBinding', 'RequestBaseType', RequestBaseType)


# Complex type {http://www.opengis.net/wps/1.0.0}ResponseBaseType with content type EMPTY
class ResponseBaseType (pyxb.binding.basis.complexTypeDefinition):
    """WPS operation response base, for all WPS operations except GetCapabilities. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponseBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 23, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 37, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default='WPS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 27, 2)
    __service._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 27, 2)
    
    service = property(__service.value, __service.set, None, 'Service type identifier (WPS)')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_version', _ImportedBinding_cwt_wps_ows.VersionType, fixed=True, unicode_default='1.0.0', required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 32, 2)
    __version._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ResponseBaseType.xsd', 32, 2)
    
    version = property(__version.value, __version.set, None, 'Version of the WPS interface specification implemented by the server (1.0.0)')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.ResponseBaseType = ResponseBaseType
Namespace.addCategoryObject('typeBinding', 'ResponseBaseType', ResponseBaseType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Location of a WSDL document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 21, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netwps1_0_0_CTD_ANON_9_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 22, 3)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.opengis.net/wps/1.0.0}InputDescriptionType with content type ELEMENT_ONLY
class InputDescriptionType (DescriptionType):
    """Description of an input to a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 95, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element ComplexData uses Python identifier ComplexData
    __ComplexData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplexData'), 'ComplexData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_ComplexData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 126, 3), )

    
    ComplexData = property(__ComplexData.value, __ComplexData.set, None, 'Indicates that this Input shall be a complex data structure (such as a GML document), and provides a list of Formats, Encodings, and Schemas supported for this Input. The value of this ComplexData structure can be input either embedded in the Execute request or remotely accessible to the server.  The client can select from among the identified combinations of Formats, Encodings, and Schemas to specify the form of the Input. This allows for complete specification of particular versions of GML, or image formats. ')

    
    # Element LiteralData uses Python identifier LiteralData
    __LiteralData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LiteralData'), 'LiteralData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_LiteralData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 131, 3), )

    
    LiteralData = property(__LiteralData.value, __LiteralData.set, None, 'Indicates that this Input shall be a simple numeric value or character string that is embedded in the execute request, and describes the possible values. ')

    
    # Element BoundingBoxData uses Python identifier BoundingBoxData
    __BoundingBoxData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BoundingBoxData'), 'BoundingBoxData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_BoundingBoxData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 136, 3), )

    
    BoundingBoxData = property(__BoundingBoxData.value, __BoundingBoxData.set, None, 'Indicates that this Input shall be a BoundingBox data structure that is embedded in the execute request, and provides a list of the Coordinate Reference System support for this Bounding Box. ')

    
    # Attribute minOccurs uses Python identifier minOccurs
    __minOccurs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minOccurs'), 'minOccurs', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_minOccurs', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __minOccurs._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 107, 4)
    __minOccurs._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 107, 4)
    
    minOccurs = property(__minOccurs.value, __minOccurs.set, None, 'The minimum number of times that values for this parameter are required in an Execute request.  If "0", this data input is optional. If greater than "0" then this process input is required. ')

    
    # Attribute maxOccurs uses Python identifier maxOccurs
    __maxOccurs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxOccurs'), 'maxOccurs', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_maxOccurs', pyxb.binding.datatypes.positiveInteger, required=True)
    __maxOccurs._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 112, 4)
    __maxOccurs._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 112, 4)
    
    maxOccurs = property(__maxOccurs.value, __maxOccurs.set, None, 'The maximum number of times that values for this parameter are permitted in an Execute request. If "1" then this parameter may appear only once in an Execute request.  If greater than "1", then this input parameter may appear that many times in an Execute request. ')

    _ElementMap.update({
        __ComplexData.name() : __ComplexData,
        __LiteralData.name() : __LiteralData,
        __BoundingBoxData.name() : __BoundingBoxData
    })
    _AttributeMap.update({
        __minOccurs.name() : __minOccurs,
        __maxOccurs.name() : __maxOccurs
    })
_module_typeBindings.InputDescriptionType = InputDescriptionType
Namespace.addCategoryObject('typeBinding', 'InputDescriptionType', InputDescriptionType)


# Complex type {http://www.opengis.net/wps/1.0.0}LiteralInputType with content type ELEMENT_ONLY
class LiteralInputType (LiteralOutputType):
    """Description of a process input that consists of a simple literal value (e.g., "2.1"). (Informative: This type is a subset of the ows:UnNamedDomainType defined in owsDomaintype.xsd.) """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LiteralInputType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 144, 1)
    _ElementMap = LiteralOutputType._ElementMap.copy()
    _AttributeMap = LiteralOutputType._AttributeMap.copy()
    # Base type is LiteralOutputType
    
    # Element {http://www.opengis.net/ows/1.1}AnyValue uses Python identifier AnyValue
    __AnyValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'AnyValue'), 'AnyValue', '__httpwww_opengis_netwps1_0_0_LiteralInputType_httpwww_opengis_netows1_1AnyValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 86, 1), )

    
    AnyValue = property(__AnyValue.value, __AnyValue.set, None, 'Specifies that any value is allowed for this parameter.')

    
    # Element {http://www.opengis.net/ows/1.1}AllowedValues uses Python identifier AllowedValues
    __AllowedValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'AllowedValues'), 'AllowedValues', '__httpwww_opengis_netwps1_0_0_LiteralInputType_httpwww_opengis_netows1_1AllowedValues', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 136, 1), )

    
    AllowedValues = property(__AllowedValues.value, __AllowedValues.set, None, 'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ')

    
    # Element DataType ({http://www.opengis.net/ows/1.1}DataType) inherited from {http://www.opengis.net/wps/1.0.0}LiteralOutputType
    
    # Element DefaultValue uses Python identifier DefaultValue
    __DefaultValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DefaultValue'), 'DefaultValue', '__httpwww_opengis_netwps1_0_0_LiteralInputType_DefaultValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 156, 5), )

    
    DefaultValue = property(__DefaultValue.value, __DefaultValue.set, None, 'Optional default value for this quantity, which should be included when this quantity has a default value.  The DefaultValue shall be understood to be consistent with the unit of measure selected in the Execute request. ')

    
    # Element ValuesReference uses Python identifier ValuesReference
    __ValuesReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValuesReference'), 'ValuesReference', '__httpwww_opengis_netwps1_0_0_LiteralInputType_ValuesReference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 181, 3), )

    
    ValuesReference = property(__ValuesReference.value, __ValuesReference.set, None, 'Indicates that there are a finite set of values and ranges allowed for this input, which are specified in the referenced list. ')

    
    # Element UOMs (UOMs) inherited from {http://www.opengis.net/wps/1.0.0}LiteralOutputType
    _ElementMap.update({
        __AnyValue.name() : __AnyValue,
        __AllowedValues.name() : __AllowedValues,
        __DefaultValue.name() : __DefaultValue,
        __ValuesReference.name() : __ValuesReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LiteralInputType = LiteralInputType
Namespace.addCategoryObject('typeBinding', 'LiteralInputType', LiteralInputType)


# Complex type {http://www.opengis.net/wps/1.0.0}SupportedComplexDataInputType with content type ELEMENT_ONLY
class SupportedComplexDataInputType (SupportedComplexDataType):
    """Complex type {http://www.opengis.net/wps/1.0.0}SupportedComplexDataInputType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedComplexDataInputType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 201, 1)
    _ElementMap = SupportedComplexDataType._ElementMap.copy()
    _AttributeMap = SupportedComplexDataType._AttributeMap.copy()
    # Base type is SupportedComplexDataType
    
    # Element Default (Default) inherited from {http://www.opengis.net/wps/1.0.0}SupportedComplexDataType
    
    # Element Supported (Supported) inherited from {http://www.opengis.net/wps/1.0.0}SupportedComplexDataType
    
    # Attribute maximumMegabytes uses Python identifier maximumMegabytes
    __maximumMegabytes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maximumMegabytes'), 'maximumMegabytes', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataInputType_maximumMegabytes', pyxb.binding.datatypes.integer)
    __maximumMegabytes._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 207, 4)
    __maximumMegabytes._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 207, 4)
    
    maximumMegabytes = property(__maximumMegabytes.value, __maximumMegabytes.set, None, 'The maximum file size, in megabytes, of this input.  If the input exceeds this size, the server will return an error instead of processing the inputs. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __maximumMegabytes.name() : __maximumMegabytes
    })
_module_typeBindings.SupportedComplexDataInputType = SupportedComplexDataInputType
Namespace.addCategoryObject('typeBinding', 'SupportedComplexDataInputType', SupportedComplexDataInputType)


# Complex type {http://www.opengis.net/wps/1.0.0}OutputDescriptionType with content type ELEMENT_ONLY
class OutputDescriptionType (DescriptionType):
    """Description of a process Output. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 365, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element ComplexOutput uses Python identifier ComplexOutput
    __ComplexOutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplexOutput'), 'ComplexOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_ComplexOutput', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 384, 3), )

    
    ComplexOutput = property(__ComplexOutput.value, __ComplexOutput.set, None, 'Indicates that this Output shall be a complex data structure (such as a GML fragment) that is returned by the execute operation response. The value of this complex data structure can be output either embedded in the execute operation response or remotely accessible to the client. When this output form is indicated, the process produces only a single output, and "store" is "false, the output shall be returned directly, without being embedded in the XML document that is otherwise provided by execute operation response. \n\t\t\t\t\tThis element also provides a list of format, encoding, and schema combinations supported for this output. The client can select from among the identified combinations of formats, encodings, and schemas to specify the form of the output. This allows for complete specification of particular versions of GML, or image formats. ')

    
    # Element LiteralOutput uses Python identifier LiteralOutput
    __LiteralOutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LiteralOutput'), 'LiteralOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_LiteralOutput', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 390, 3), )

    
    LiteralOutput = property(__LiteralOutput.value, __LiteralOutput.set, None, 'Indicates that this output shall be a simple literal value (such as an integer) that is embedded in the execute response, and describes that output. ')

    
    # Element BoundingBoxOutput uses Python identifier BoundingBoxOutput
    __BoundingBoxOutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BoundingBoxOutput'), 'BoundingBoxOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_BoundingBoxOutput', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 395, 3), )

    
    BoundingBoxOutput = property(__BoundingBoxOutput.value, __BoundingBoxOutput.set, None, 'Indicates that this output shall be a BoundingBox data structure, and provides a list of the CRSs supported in these Bounding Boxes. This element shall be included when this process output is an ows:BoundingBox element. ')

    _ElementMap.update({
        __ComplexOutput.name() : __ComplexOutput,
        __LiteralOutput.name() : __LiteralOutput,
        __BoundingBoxOutput.name() : __BoundingBoxOutput
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OutputDescriptionType = OutputDescriptionType
Namespace.addCategoryObject('typeBinding', 'OutputDescriptionType', OutputDescriptionType)


# Complex type {http://www.opengis.net/wps/1.0.0}OutputDefinitionType with content type ELEMENT_ONLY
class OutputDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    """Definition of a format, encoding,  schema, and unit-of-measure for an output to be returned from a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 140, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_uom', pyxb.binding.datatypes.anyURI)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 151, 2)
    __uom._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 151, 2)
    
    uom = property(__uom.value, __uom.set, None, 'Reference to the unit of measure (if any) requested for this output. A uom can be referenced when a client wants to specify one of the units of measure supported for this output. This uom shall be a unit of measure referenced for this output of this process in the Process full description. ')

    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_mimeType', _ImportedBinding_cwt_wps_ows.MimeType)
    __mimeType._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    __mimeType._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, 'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_encoding', pyxb.binding.datatypes.anyURI)
    __encoding._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    __encoding._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    
    encoding = property(__encoding.value, __encoding.set, None, 'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_schema', pyxb.binding.datatypes.anyURI)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    __schema._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    
    schema = property(__schema.value, __schema.set, None, 'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    _ElementMap.update({
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        __uom.name() : __uom,
        __mimeType.name() : __mimeType,
        __encoding.name() : __encoding,
        __schema.name() : __schema
    })
_module_typeBindings.OutputDefinitionType = OutputDefinitionType
Namespace.addCategoryObject('typeBinding', 'OutputDefinitionType', OutputDefinitionType)


# Complex type {http://www.opengis.net/wps/1.0.0}InputReferenceType with content type ELEMENT_ONLY
class InputReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference to an input or output value that is a web accessible resource. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 252, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0Header', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 257, 3), )

    
    Header = property(__Header.value, __Header.set, None, 'Extra HTTP request headers needed by the service identified in ../Reference/@href.  For example, an HTTP SOAP request requires a SOAPAction header.  This permits the creation of a complete and valid POST request.')

    
    # Element {http://www.opengis.net/wps/1.0.0}Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Body'), 'Body', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0Body', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 275, 4), )

    
    Body = property(__Body.value, __Body.set, None, 'The contents of this element to be used as the body of the HTTP request message to be sent to the service identified in ../Reference/@href.  For example, it could be an XML encoded WFS request using HTTP POST')

    
    # Element {http://www.opengis.net/wps/1.0.0}BodyReference uses Python identifier BodyReference
    __BodyReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BodyReference'), 'BodyReference', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0BodyReference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 280, 4), )

    
    BodyReference = property(__BodyReference.value, __BodyReference.set, None, 'Reference to a remote document to be used as the body of the an HTTP POST request message to the service identified in ../Reference/@href.')

    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_InputReferenceType_mimeType', _ImportedBinding_cwt_wps_ows.MimeType)
    __mimeType._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    __mimeType._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, 'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_InputReferenceType_encoding', pyxb.binding.datatypes.anyURI)
    __encoding._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    __encoding._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    
    encoding = property(__encoding.value, __encoding.set, None, 'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_InputReferenceType_schema', pyxb.binding.datatypes.anyURI)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    __schema._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    
    schema = property(__schema.value, __schema.set, None, 'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    
    # Attribute method uses Python identifier method
    __method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'method'), 'method', '__httpwww_opengis_netwps1_0_0_InputReferenceType_method', _module_typeBindings.STD_ANON, unicode_default='GET')
    __method._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 299, 2)
    __method._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 299, 2)
    
    method = property(__method.value, __method.set, None, 'Identifies the HTTP method.  Allows a choice of GET or POST.  Default is GET.')

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 294, 2)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header,
        __Body.name() : __Body,
        __BodyReference.name() : __BodyReference
    })
    _AttributeMap.update({
        __mimeType.name() : __mimeType,
        __encoding.name() : __encoding,
        __schema.name() : __schema,
        __method.name() : __method,
        __href.name() : __href
    })
_module_typeBindings.InputReferenceType = InputReferenceType
Namespace.addCategoryObject('typeBinding', 'InputReferenceType', InputReferenceType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Reference to a remote document to be used as the body of the an HTTP POST request message to the service identified in ../Reference/@href."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 284, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netwps1_0_0_CTD_ANON_10_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 285, 6)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type {http://www.opengis.net/wps/1.0.0}ComplexDataType with content type MIXED
class ComplexDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex data (such as an image), including a definition of the complex value data structure (i.e., schema, format, and encoding).  May be an ows:Manifest data structure."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 313, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_ComplexDataType_mimeType', _ImportedBinding_cwt_wps_ows.MimeType)
    __mimeType._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    __mimeType._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, 'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_ComplexDataType_encoding', pyxb.binding.datatypes.anyURI)
    __encoding._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    __encoding._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    
    encoding = property(__encoding.value, __encoding.set, None, 'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_ComplexDataType_schema', pyxb.binding.datatypes.anyURI)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    __schema._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    
    schema = property(__schema.value, __schema.set, None, 'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeType.name() : __mimeType,
        __encoding.name() : __encoding,
        __schema.name() : __schema
    })
_module_typeBindings.ComplexDataType = ComplexDataType
Namespace.addCategoryObject('typeBinding', 'ComplexDataType', ComplexDataType)


# Complex type {http://www.opengis.net/wps/1.0.0}OutputDataType with content type ELEMENT_ONLY
class OutputDataType (DescriptionType):
    """Value of one output from a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 98, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element {http://www.opengis.net/wps/1.0.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__httpwww_opengis_netwps1_0_0_OutputDataType_httpwww_opengis_netwps1_0_0Reference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 121, 3), )

    
    Reference = property(__Reference.value, __Reference.set, None, 'Identifies this output as a web accessible resource, and references that resource.  This element shall only be used for complex data. This element shall be used by a server when "store" in the Execute request is "true". ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Data'), 'Data', '__httpwww_opengis_netwps1_0_0_OutputDataType_httpwww_opengis_netwps1_0_0Data', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 126, 3), )

    
    Data = property(__Data.value, __Data.set, None, 'Identifies this output value as a data embedded in this response, and includes that data. This element shall be used by a server when "store" in the Execute request is "false". ')

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Data.name() : __Data
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OutputDataType = OutputDataType
Namespace.addCategoryObject('typeBinding', 'OutputDataType', OutputDataType)


# Complex type {http://www.opengis.net/wps/1.0.0}OutputReferenceType with content type EMPTY
class OutputReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference to an output value that is a web accessible resource. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OutputReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 134, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_mimeType', _ImportedBinding_cwt_wps_ows.MimeType)
    __mimeType._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    __mimeType._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 163, 2)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, 'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_encoding', pyxb.binding.datatypes.anyURI)
    __encoding._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    __encoding._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 168, 2)
    
    encoding = property(__encoding.value, __encoding.set, None, 'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_schema', pyxb.binding.datatypes.anyURI)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    __schema._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 173, 2)
    
    schema = property(__schema.value, __schema.set, None, 'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_href', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 138, 2)
    __href._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 138, 2)
    
    href = property(__href.value, __href.set, None, 'Reference to a web-accessible resource that is provided by the process as output. This attribute shall contain a URL from which this output can be electronically retrieved. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeType.name() : __mimeType,
        __encoding.name() : __encoding,
        __schema.name() : __schema,
        __href.name() : __href
    })
_module_typeBindings.OutputReferenceType = OutputReferenceType
Namespace.addCategoryObject('typeBinding', 'OutputReferenceType', OutputReferenceType)


# Complex type {http://www.opengis.net/wps/1.0.0}ProcessStartedType with content type SIMPLE
class ProcessStartedType (pyxb.binding.basis.complexTypeDefinition):
    """Indicates that this process has been has been accepted by the server, and processing has begun. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessStartedType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 185, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute percentCompleted uses Python identifier percentCompleted
    __percentCompleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'percentCompleted'), 'percentCompleted', '__httpwww_opengis_netwps1_0_0_ProcessStartedType_percentCompleted', _module_typeBindings.STD_ANON_)
    __percentCompleted._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 194, 4)
    __percentCompleted._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 194, 4)
    
    percentCompleted = property(__percentCompleted.value, __percentCompleted.set, None, 'Percentage of process that has been completed, where 0 means the process has just started, and 99 means the process is almost complete.  This value is expected to be accurate to within ten percent.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __percentCompleted.name() : __percentCompleted
    })
_module_typeBindings.ProcessStartedType = ProcessStartedType
Namespace.addCategoryObject('typeBinding', 'ProcessStartedType', ProcessStartedType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 23, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netwps1_0_0_CTD_ANON_11_httpwww_opengis_netwps1_0_0AcceptVersions', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 25, 4), )

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, 'When omitted, server shall return latest supported version. ')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwps1_0_0_CTD_ANON_11_service', _ImportedBinding_cwt_wps_ows.ServiceType, fixed=True, unicode_default='WPS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 31, 3)
    __service._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 31, 3)
    
    service = property(__service.value, __service.set, None, 'OGC service type identifier (WPS).')

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__httpwww_opengis_netwps1_0_0_CTD_ANON_11_language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 36, 3)
    __language._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 36, 3)
    
    language = property(__language.value, __language.set, None, 'RFC 4646 language code of the human-readable text (e.g. "en-CA").')

    _ElementMap.update({
        __AcceptVersions.name() : __AcceptVersions
    })
    _AttributeMap.update({
        __service.name() : __service,
        __language.name() : __language
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (RequestBaseType):
    """WPS DescribeProcess operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_request.xsd', 27, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_CTD_ANON_12_httpwww_opengis_netows1_1Identifier', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute language inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    _ElementMap.update({
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (ResponseBaseType):
    """WPS DescribeProcess operation response. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 29, 2)
    _ElementMap = ResponseBaseType._ElementMap.copy()
    _AttributeMap = ResponseBaseType._AttributeMap.copy()
    # Base type is ResponseBaseType
    
    # Element ProcessDescription uses Python identifier ProcessDescription
    __ProcessDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ProcessDescription'), 'ProcessDescription', '__httpwww_opengis_netwps1_0_0_CTD_ANON_13_ProcessDescription', True, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 33, 6), )

    
    ProcessDescription = property(__ProcessDescription.value, __ProcessDescription.set, None, 'Ordered list of one or more full Process descriptions, listed in the order in which they were requested in the DescribeProcess operation request. ')

    
    # Attribute lang inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    _ElementMap.update({
        __ProcessDescription.name() : __ProcessDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type {http://www.opengis.net/wps/1.0.0}ProcessDescriptionType with content type ELEMENT_ONLY
class ProcessDescriptionType (ProcessBriefType):
    """Full description of a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 44, 1)
    _ElementMap = ProcessBriefType._ElementMap.copy()
    _AttributeMap = ProcessBriefType._AttributeMap.copy()
    # Base type is ProcessBriefType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Profile ({http://www.opengis.net/wps/1.0.0}Profile) inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Element WSDL ({http://www.opengis.net/wps/1.0.0}WSDL) inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Element DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_DataInputs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 51, 5), )

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, 'List of the inputs to this process. In almost all cases, at least one process input is required. However, no process inputs may be identified when all the inputs are predetermined fixed resources.  In this case, those resources shall be identified in the ows:Abstract element that describes the process.')

    
    # Element ProcessOutputs uses Python identifier ProcessOutputs
    __ProcessOutputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ProcessOutputs'), 'ProcessOutputs', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_ProcessOutputs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 65, 5), )

    
    ProcessOutputs = property(__ProcessOutputs.value, __ProcessOutputs.set, None, 'List of outputs which will or can result from executing the process. ')

    
    # Attribute processVersion inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Attribute storeSupported uses Python identifier storeSupported
    __storeSupported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'storeSupported'), 'storeSupported', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_storeSupported', pyxb.binding.datatypes.boolean, unicode_default='false')
    __storeSupported._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 80, 4)
    __storeSupported._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 80, 4)
    
    storeSupported = property(__storeSupported.value, __storeSupported.set, None, 'Indicates if ComplexData outputs from this process can be stored by the WPS server as web-accessible resources. If "storeSupported" is "true", the Execute operation request may include "asReference" equals "true" for any complex output, directing that the output of the process be stored so that the client can retrieve it as required. By default for this process, storage is not supported and all outputs are returned encoded in the Execute response. ')

    
    # Attribute statusSupported uses Python identifier statusSupported
    __statusSupported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'statusSupported'), 'statusSupported', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_statusSupported', pyxb.binding.datatypes.boolean, unicode_default='false')
    __statusSupported._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 85, 4)
    __statusSupported._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 85, 4)
    
    statusSupported = property(__statusSupported.value, __statusSupported.set, None, 'Indicates if ongoing status information can be provided for this process.  If "true", the Status element of the stored Execute response document shall be kept up to date.  If "false" then the Status element shall not be updated until processing is complete. By default, status information is not provided for this process. ')

    _ElementMap.update({
        __DataInputs.name() : __DataInputs,
        __ProcessOutputs.name() : __ProcessOutputs
    })
    _AttributeMap.update({
        __storeSupported.name() : __storeSupported,
        __statusSupported.name() : __statusSupported
    })
_module_typeBindings.ProcessDescriptionType = ProcessDescriptionType
Namespace.addCategoryObject('typeBinding', 'ProcessDescriptionType', ProcessDescriptionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (RequestBaseType):
    """WPS Execute operation request, to execute one identified Process. If a process is to be run multiple times, each run shall be submitted as a separate Execute request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 28, 2)
    _ElementMap = RequestBaseType._ElementMap.copy()
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_CTD_ANON_14_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_14_httpwww_opengis_netwps1_0_0DataInputs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 37, 6), )

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, 'List of input (or parameter) values provided to the process, including each of the Inputs needed to execute the process. It is possible to have no inputs provided only when all the inputs are predetermined fixed resources. In all other cases, at least one input is required. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ResponseForm uses Python identifier ResponseForm
    __ResponseForm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseForm'), 'ResponseForm', '__httpwww_opengis_netwps1_0_0_CTD_ANON_14_httpwww_opengis_netwps1_0_0ResponseForm', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 42, 6), )

    
    ResponseForm = property(__ResponseForm.value, __ResponseForm.set, None, 'Defines the response type of the WPS, either raw data or XML document.  If absent, the response shall be a response document which includes all outputs encoded in the response.')

    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute language inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __DataInputs.name() : __DataInputs,
        __ResponseForm.name() : __ResponseForm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type {http://www.opengis.net/wps/1.0.0}DocumentOutputDefinitionType with content type ELEMENT_ONLY
class DocumentOutputDefinitionType (OutputDefinitionType):
    """Definition of a format, encoding,  schema, and unit-of-measure for an output to be returned from a process. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentOutputDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 110, 1)
    _ElementMap = OutputDefinitionType._ElementMap.copy()
    _AttributeMap = OutputDefinitionType._AttributeMap.copy()
    # Base type is OutputDefinitionType
    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_httpwww_opengis_netows1_1Title', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_httpwww_opengis_netows1_1Abstract', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute asReference uses Python identifier asReference
    __asReference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'asReference'), 'asReference', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_asReference', pyxb.binding.datatypes.boolean, unicode_default='false')
    __asReference._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 131, 4)
    __asReference._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 131, 4)
    
    asReference = property(__asReference.value, __asReference.set, None, 'Specifies if this output should be stored by the process as a web-accessible resource. If asReference is "true", the server shall store this output so that the client can retrieve it as required. If store is "false", all the output shall be encoded in the Execute operation response document. This parameter only applies to ComplexData outputs.  This parameter shall not be included unless the corresponding "storeSupported" parameter is included and is "true" in the ProcessDescription for this process. ')

    
    # Attribute uom inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute mimeType inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute encoding inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute schema inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    _ElementMap.update({
        __Title.name() : __Title,
        __Abstract.name() : __Abstract
    })
    _AttributeMap.update({
        __asReference.name() : __asReference
    })
_module_typeBindings.DocumentOutputDefinitionType = DocumentOutputDefinitionType
Namespace.addCategoryObject('typeBinding', 'DocumentOutputDefinitionType', DocumentOutputDefinitionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (ResponseBaseType):
    """WPS Execute operation response. By default, this XML document is delivered to the client in response to an Execute request. If "status" is "false" in the Execute operation request, this document is normally returned when process execution has been completed.
			If "status" in the Execute request is "true", this response shall be returned as soon as the Execute request has been accepted for processing. In this case, the same XML document is also made available as a web-accessible resource from the URL identified in the statusLocation, and the WPS server shall repopulate it once the process has completed. It may repopulate it on an ongoing basis while the process is executing.
			However, the response to an Execute request will not include this element in the special case where the output is a single complex value result and the Execute request indicates that "store" is "false". Instead, the server shall return the complex result (e.g., GIF image or GML) directly, without encoding it in the ExecuteResponse. If processing fails in this special case, the normal ExecuteResponse shall be sent, with the error condition indicated. This option is provided to simplify the programming required for simple clients and for service chaining. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 31, 2)
    _ElementMap = ResponseBaseType._ElementMap.copy()
    _AttributeMap = ResponseBaseType._AttributeMap.copy()
    # Base type is ResponseBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}Process uses Python identifier Process
    __Process = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Process'), 'Process', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0Process', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 35, 6), )

    
    Process = property(__Process.value, __Process.set, None, 'Process description from the ProcessOfferings section of the GetCapabilities response. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0Status', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 40, 6), )

    
    Status = property(__Status.value, __Status.set, None, 'Execution status of this process. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0DataInputs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 45, 6), )

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, 'Inputs that were provided as part of the execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".')

    
    # Element {http://www.opengis.net/wps/1.0.0}OutputDefinitions uses Python identifier OutputDefinitions
    __OutputDefinitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputDefinitions'), 'OutputDefinitions', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0OutputDefinitions', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 50, 6), )

    
    OutputDefinitions = property(__OutputDefinitions.value, __OutputDefinitions.set, None, 'Complete list of Output data types that were requested as part of the Execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessOutputs uses Python identifier ProcessOutputs
    __ProcessOutputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessOutputs'), 'ProcessOutputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0ProcessOutputs', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 55, 6), )

    
    ProcessOutputs = property(__ProcessOutputs.value, __ProcessOutputs.set, None, 'List of values of the Process output parameters. Normally there would be at least one output when the process has completed successfully. If the process has not finished executing, the implementer can choose to include whatever final results are ready at the time the Execute response is provided. If the reference locations of outputs are known in advance, these URLs may be provided before they are populated. ')

    
    # Attribute lang inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute serviceInstance uses Python identifier serviceInstance
    __serviceInstance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceInstance'), 'serviceInstance', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_serviceInstance', pyxb.binding.datatypes.anyURI, required=True)
    __serviceInstance._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 70, 5)
    __serviceInstance._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 70, 5)
    
    serviceInstance = property(__serviceInstance.value, __serviceInstance.set, None, 'This attribute shall contain the GetCapabilities URL of the WPS service which was invoked')

    
    # Attribute statusLocation uses Python identifier statusLocation
    __statusLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'statusLocation'), 'statusLocation', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_statusLocation', pyxb.binding.datatypes.anyURI)
    __statusLocation._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 75, 5)
    __statusLocation._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 75, 5)
    
    statusLocation = property(__statusLocation.value, __statusLocation.set, None, 'The URL referencing the location from which the ExecuteResponse can be retrieved. If "status" is "true" in the Execute request, the ExecuteResponse should also be found here as soon as the process returns the initial response to the client. It should persist at this location as long as the outputs are accessible from the server. The outputs may be stored for as long as the implementer of the server decides. If the process takes a long time, this URL can be repopulated on an ongoing basis in order to keep the client updated on progress. Before the process has succeeded, the ExecuteResponse contains information about the status of the process, including whether or not processing has started, and the percentage completed. It may also optionally contain the inputs and any ProcessStartedType interim results. When the process has succeeded, the ExecuteResponse found at this URL shall contain the output values or references to them. ')

    _ElementMap.update({
        __Process.name() : __Process,
        __Status.name() : __Status,
        __DataInputs.name() : __DataInputs,
        __OutputDefinitions.name() : __OutputDefinitions,
        __ProcessOutputs.name() : __ProcessOutputs
    })
    _AttributeMap.update({
        __serviceInstance.name() : __serviceInstance,
        __statusLocation.name() : __statusLocation
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type {http://www.opengis.net/wps/1.0.0}WPSCapabilitiesType with content type ELEMENT_ONLY
class WPSCapabilitiesType (_ImportedBinding_cwt_wps_ows.CapabilitiesBaseType):
    """Complex type {http://www.opengis.net/wps/1.0.0}WPSCapabilitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WPSCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 32, 1)
    _ElementMap = _ImportedBinding_cwt_wps_ows.CapabilitiesBaseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_cwt_wps_ows.CapabilitiesBaseType._AttributeMap.copy()
    # Base type is _ImportedBinding_cwt_wps_ows.CapabilitiesBaseType
    
    # Element OperationsMetadata ({http://www.opengis.net/ows/1.1}OperationsMetadata) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows/1.1}ServiceIdentification) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceProvider ({http://www.opengis.net/ows/1.1}ServiceProvider) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}WSDL uses Python identifier WSDL
    __WSDL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WSDL'), 'WSDL', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0WSDL', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 17, 1), )

    
    WSDL = property(__WSDL.value, __WSDL.set, None, 'Location of a WSDL document.')

    
    # Element {http://www.opengis.net/wps/1.0.0}Languages uses Python identifier Languages
    __Languages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Languages'), 'Languages', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0Languages', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 54, 1), )

    
    Languages = property(__Languages.value, __Languages.set, None, 'Listing of the default and other languages supported by this service. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessOfferings uses Python identifier ProcessOfferings
    __ProcessOfferings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProcessOfferings'), 'ProcessOfferings', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0ProcessOfferings', False, pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 96, 1), )

    
    ProcessOfferings = property(__ProcessOfferings.value, __ProcessOfferings.set, None, 'List of brief descriptions of the processes offered by this WPS server. ')

    
    # Attribute version inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 49, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_service', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='WPS', required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 48, 4)
    __service._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 48, 4)
    
    service = property(__service.value, __service.set, None, None)

    _ElementMap.update({
        __WSDL.name() : __WSDL,
        __Languages.name() : __Languages,
        __ProcessOfferings.name() : __ProcessOfferings
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __service.name() : __service
    })
_module_typeBindings.WPSCapabilitiesType = WPSCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'WPSCapabilitiesType', WPSCapabilitiesType)


Languages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Languages'), CTD_ANON_6, documentation='Listing of the default and other languages supported by this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 54, 1))
Namespace.addCategoryObject('elementBinding', Languages.name().localName(), Languages)

ProcessOfferings = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessOfferings'), CTD_ANON_8, documentation='List of brief descriptions of the processes offered by this WPS server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', ProcessOfferings.name().localName(), ProcessOfferings)

WSDL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WSDL'), CTD_ANON_9, documentation='Location of a WSDL document.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', WSDL.name().localName(), WSDL)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), CTD_ANON_11, location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 22, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

DescribeProcess = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescribeProcess'), CTD_ANON_12, documentation='WPS DescribeProcess operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_request.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', DescribeProcess.name().localName(), DescribeProcess)

ProcessDescriptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessDescriptions'), CTD_ANON_13, documentation='WPS DescribeProcess operation response. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', ProcessDescriptions.name().localName(), ProcessDescriptions)

Execute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Execute'), CTD_ANON_14, documentation='WPS Execute operation request, to execute one identified Process. If a process is to be run multiple times, each run shall be submitted as a separate Execute request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', Execute.name().localName(), Execute)

ExecuteResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExecuteResponse'), CTD_ANON_15, documentation='WPS Execute operation response. By default, this XML document is delivered to the client in response to an Execute request. If "status" is "false" in the Execute operation request, this document is normally returned when process execution has been completed.\n\t\t\tIf "status" in the Execute request is "true", this response shall be returned as soon as the Execute request has been accepted for processing. In this case, the same XML document is also made available as a web-accessible resource from the URL identified in the statusLocation, and the WPS server shall repopulate it once the process has completed. It may repopulate it on an ongoing basis while the process is executing.\n\t\t\tHowever, the response to an Execute request will not include this element in the special case where the output is a single complex value result and the Execute request indicates that "store" is "false". Instead, the server shall return the complex result (e.g., GIF image or GML) directly, without encoding it in the ExecuteResponse. If processing fails in this special case, the normal ExecuteResponse shall be sent, with the error condition indicated. This option is provided to simplify the programming required for simple clients and for service chaining. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', ExecuteResponse.name().localName(), ExecuteResponse)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Capabilities'), WPSCapabilitiesType, documentation='WPS GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, including metadata about the processes that can be executed. Since the server does not implement the updateSequence and Sections parameters, the server shall always return the complete Capabilities document, without the updateSequence parameter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)



DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=DescriptionType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=DescriptionType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata'), _ImportedBinding_cwt_wps_ows.MetadataType, scope=DescriptionType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), _ImportedBinding_cwt_wps_ows.CodeType, scope=DescriptionType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DescriptionType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Input'), InputDescriptionType, scope=CTD_ANON, documentation='Unordered list of one or more descriptions of the inputs that can be accepted by this process, including all required and optional inputs.  Where an input is optional because a default value exists, that default value must be identified in the "ows:Abstract" element for that input, except in the case of LiteralData, where the default must be indicated in the corresponding ows:DefaultValue element. Where an input is optional because it depends on the value(s) of other inputs, this must be indicated in the ows:Abstract element for that input. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 57, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Input')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 57, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Output'), OutputDescriptionType, scope=CTD_ANON_, documentation='Unordered list of one or more descriptions of all the outputs that can result from executing this process. At least one output is required from each process. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 71, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Output')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 71, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




SupportedUOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Default'), CTD_ANON_2, scope=SupportedUOMsType, documentation='Reference to the default UOM supported for this input or output, if UoM is applicable. The process shall expect input in or produce output in this UOM unless the Execute request specifies another supported UOM. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 222, 3)))

SupportedUOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Supported'), UOMsType, scope=SupportedUOMsType, documentation='Unordered list of references to all of the UOMs supported for this input or output, if UOM is applicable. The default UOM shall be included in this list. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 236, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupportedUOMsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Default')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 222, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupportedUOMsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Supported')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 236, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedUOMsType._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), _ImportedBinding_cwt_wps_ows.DomainMetadataType, scope=CTD_ANON_2, documentation='Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 228, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




UOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM'), _ImportedBinding_cwt_wps_ows.DomainMetadataType, scope=UOMsType, documentation='Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UOMsType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'UOM')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 249, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UOMsType._Automaton = _BuildAutomaton_5()




SupportedCRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Default'), CTD_ANON_3, scope=SupportedCRSsType, documentation='Identifies the default CRS that will be used unless the Execute operation request specifies another supported CRS. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 262, 3)))

SupportedCRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Supported'), CRSsType, scope=SupportedCRSsType, documentation='Unordered list of references to all of the CRSs supported for this Input/Output. The default CRS shall be included in this list.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 276, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupportedCRSsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Default')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 262, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupportedCRSsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Supported')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 276, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedCRSsType._Automaton = _BuildAutomaton_6()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CRS'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_3, documentation='Reference to the default CRS supported for this Input/Output', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 268, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'CRS')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 268, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_7()




CRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CRS'), pyxb.binding.datatypes.anyURI, scope=CRSsType, documentation='Reference to a CRS supported for this Input/Output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 289, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CRSsType._UseForTag(pyxb.namespace.ExpandedName(None, 'CRS')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 289, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CRSsType._Automaton = _BuildAutomaton_8()




SupportedComplexDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Default'), ComplexDataCombinationType, scope=SupportedComplexDataType, documentation='Identifies the default combination of Format, Encoding, and Schema supported for this Input/Output. The process shall expect input in or produce output in this combination of MimeType/Encoding/Schema unless the Execute request specifies otherwise.  ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 302, 3)))

SupportedComplexDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Supported'), ComplexDataCombinationsType, scope=SupportedComplexDataType, documentation='Unordered list of combinations of format, encoding, and schema supported for this Input/Output. This element shall be repeated for each combination of MimeType/Encoding/Schema that is supported for this Input/Output. This list shall include the default MimeType/Encoding/Schema. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 307, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupportedComplexDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'Default')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupportedComplexDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'Supported')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 307, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedComplexDataType._Automaton = _BuildAutomaton_9()




ComplexDataCombinationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Format'), ComplexDataDescriptionType, scope=ComplexDataCombinationType, documentation='The default combination of MimeType/Encoding/Schema supported for this Input/Output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 320, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexDataCombinationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Format')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 320, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComplexDataCombinationType._Automaton = _BuildAutomaton_10()




ComplexDataCombinationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Format'), ComplexDataDescriptionType, scope=ComplexDataCombinationsType, documentation='A valid combination of MimeType/Encoding/Schema supported for this Input/Output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 333, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexDataCombinationsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Format')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 333, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComplexDataCombinationsType._Automaton = _BuildAutomaton_11()




ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MimeType'), _ImportedBinding_cwt_wps_ows.MimeType, scope=ComplexDataDescriptionType, documentation='Mime type supported for this input or output (e.g., text/xml). ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 346, 3)))

ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Encoding'), pyxb.binding.datatypes.anyURI, scope=ComplexDataDescriptionType, documentation='Reference to an encoding supported for this input or output (e.g., UTF-8).  This element shall be omitted if Encoding does not apply to this Input/Output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 351, 3)))

ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Schema'), pyxb.binding.datatypes.anyURI, scope=ComplexDataDescriptionType, documentation='Reference to a definition of XML elements or types supported for this Input/Output (e.g., GML 2.1 Application Schema). Each of these XML elements or types shall be defined in a separate XML Schema Document. This parameter shall be included when this input/output is XML encoded using an XML schema. When included, the input/output shall validate against the referenced XML Schema. This element shall be omitted if Schema does not apply to this Input/Output. Note: If the Input/Output uses a profile of a larger schema, the server administrator should provide that schema profile for validation purposes. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 356, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 351, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 356, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'MimeType')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 346, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'Encoding')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 351, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'Schema')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 356, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComplexDataDescriptionType._Automaton = _BuildAutomaton_12()




LiteralOutputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType'), _ImportedBinding_cwt_wps_ows.DomainMetadataType, scope=LiteralOutputType, documentation='Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 262, 1)))

LiteralOutputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UOMs'), SupportedUOMsType, scope=LiteralOutputType, documentation='List of supported units of measure for this input or output. This element should be included when this literal has a unit of measure (e.g., "meters", without a more complete reference system). Not necessary for a count, which has no units. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 408, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LiteralOutputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 408, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LiteralOutputType._UseForTag(pyxb.namespace.ExpandedName(None, 'UOMs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LiteralOutputType._Automaton = _BuildAutomaton_13()




DataInputsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Input'), InputType, scope=DataInputsType, documentation='Unordered list of one or more inputs to be used by the process, including each of the Inputs needed to execute the process. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 58, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataInputsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Input')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 58, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataInputsType._Automaton = _BuildAutomaton_14()




ResponseFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseDocument'), ResponseDocumentType, scope=ResponseFormType, documentation='Indicates that the outputs shall be returned as part of a WPS response document.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 71, 3)))

ResponseFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RawDataOutput'), OutputDefinitionType, scope=ResponseFormType, documentation='Indicates that the output shall be returned directly as raw data, without a WPS response document.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 76, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponseFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseDocument')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponseFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RawDataOutput')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 76, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponseFormType._Automaton = _BuildAutomaton_15()




ResponseDocumentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), DocumentOutputDefinitionType, scope=ResponseDocumentType, documentation='Unordered list of definitions of the outputs (or parameters) requested from the process. These outputs are not normally identified, unless the client is specifically requesting a limited subset of outputs, and/or is requesting output formats and/or schemas and/or encodings different from the defaults and selected from the alternatives identified in the process description, or wishes to customize the descriptive information about the output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 86, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponseDocumentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponseDocumentType._Automaton = _BuildAutomaton_16()




InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=InputType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1)))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=InputType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1)))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), _ImportedBinding_cwt_wps_ows.CodeType, scope=InputType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), InputReferenceType, scope=InputType, documentation='Identifies this input value as a web accessible resource, and references that resource. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 215, 3)))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Data'), DataType, scope=InputType, documentation='Identifies this input value as a data embedded in this request, and includes that data. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 220, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 192, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 197, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 187, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 197, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 215, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Data')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 220, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InputType._Automaton = _BuildAutomaton_17()




DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexData'), ComplexDataType, scope=DataType, documentation='Identifies this input or output value as a complex data structure encoded in XML (e.g., using GML), and provides that complex data structure. For an input, this element may be used by a client for any process input coded as ComplexData in the ProcessDescription. For an output, this element shall be used by a server when "store" in the Execute request is "false". ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 233, 3)))

DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LiteralData'), LiteralDataType, scope=DataType, documentation='Identifies this input or output data as literal data of a simple quantity (e.g., one number), and provides that data. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 238, 3)))

DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxData'), _ImportedBinding_cwt_wps_ows.BoundingBoxType, scope=DataType, documentation='Identifies this input or output data as an ows:BoundingBox data structure, and provides that ows:BoundingBox data. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 243, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComplexData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LiteralData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 238, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 243, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataType._Automaton = _BuildAutomaton_18()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), OutputDataType, scope=CTD_ANON_5, documentation='Unordered list of values of all the outputs produced by this process. It is not necessary to include an output until the Status is ProcessSucceeded. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 61, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 61, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_19()




OutputDefinitionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), DocumentOutputDefinitionType, scope=OutputDefinitionsType, documentation='Output definition as provided in the execute request ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 90, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDefinitionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 90, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutputDefinitionsType._Automaton = _BuildAutomaton_20()




StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessAccepted'), pyxb.binding.datatypes.string, scope=StatusType, documentation='Indicates that this process has been accepted by the server, but is in a queue and has not yet started to execute. The contents of this human-readable text string is left open to definition by each server implementation, but is expected to include any messages the server may wish to let the clients know. Such information could include how long the queue is, or any warning conditions that may have been encountered. The client may display this text to a human user. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 152, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessStarted'), ProcessStartedType, scope=StatusType, documentation='Indicates that this process has been accepted by the server, and processing has begun. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 157, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessPaused'), ProcessStartedType, scope=StatusType, documentation='Indicates that this process has been  accepted by the server, and processing has started but subsequently been paused by the server.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 162, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessSucceeded'), pyxb.binding.datatypes.string, scope=StatusType, documentation='Indicates that this process has successfully completed execution. The contents of this human-readable text string is left open to definition by each server, but is expected to include any messages the server may wish to let the clients know, such as how long the process took to execute, or any warning conditions that may have been encountered. The client may display this text string to a human user. The client should make use of the presence of this element to trigger automated or manual access to the results of the process. If manual access is intended, the client should use the presence of this element to present the results as downloadable links to the user. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 167, 3)))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessFailed'), ProcessFailedType, scope=StatusType, documentation='Indicates that execution of this process has failed, and includes error information. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 172, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessAccepted')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 152, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessStarted')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 157, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessPaused')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 162, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessSucceeded')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 167, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessFailed')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 172, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatusType._Automaton = _BuildAutomaton_21()




ProcessFailedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'ExceptionReport'), _ImportedBinding_cwt_wps_ows.CTD_ANON_9, scope=ProcessFailedType, documentation='Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 23, 1)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProcessFailedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ExceptionReport')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 214, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProcessFailedType._Automaton = _BuildAutomaton_22()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Default'), CTD_ANON_7, scope=CTD_ANON_6, documentation='Identifies the default language that will be used unless the operation request specifies another supported language. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 60, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Supported'), LanguagesType, scope=CTD_ANON_6, documentation='Unordered list of references to all of the languages supported by this service. The default language shall be included in this list.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 74, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Default')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 60, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Supported')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 74, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_23()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language'), pyxb.binding.datatypes.language, scope=CTD_ANON_7, documentation='Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 122, 1)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 66, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_24()




LanguagesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language'), pyxb.binding.datatypes.language, scope=LanguagesType, documentation='Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 122, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LanguagesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Language')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LanguagesType._Automaton = _BuildAutomaton_25()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Process'), ProcessBriefType, scope=CTD_ANON_8, documentation='Unordered list of one or more brief descriptions of all the processes offered by this WPS server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 102, 4)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Process')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 102, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_26()




ProcessBriefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Profile'), pyxb.binding.datatypes.anyURI, scope=ProcessBriefType, documentation='Optional unordered list of application profiles to which this process complies.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5)))

ProcessBriefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WSDL'), CTD_ANON_9, scope=ProcessBriefType, documentation='Location of a WSDL document.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 17, 1)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 33, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Profile')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WSDL')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 33, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProcessBriefType._Automaton = _BuildAutomaton_27()




InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplexData'), SupportedComplexDataInputType, scope=InputDescriptionType, documentation='Indicates that this Input shall be a complex data structure (such as a GML document), and provides a list of Formats, Encodings, and Schemas supported for this Input. The value of this ComplexData structure can be input either embedded in the Execute request or remotely accessible to the server.  The client can select from among the identified combinations of Formats, Encodings, and Schemas to specify the form of the Input. This allows for complete specification of particular versions of GML, or image formats. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 126, 3)))

InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LiteralData'), LiteralInputType, scope=InputDescriptionType, documentation='Indicates that this Input shall be a simple numeric value or character string that is embedded in the execute request, and describes the possible values. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 131, 3)))

InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BoundingBoxData'), SupportedCRSsType, scope=InputDescriptionType, documentation='Indicates that this Input shall be a BoundingBox data structure that is embedded in the execute request, and provides a list of the Coordinate Reference System support for this Bounding Box. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 136, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplexData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 126, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'LiteralData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 131, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'BoundingBoxData')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 136, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InputDescriptionType._Automaton = _BuildAutomaton_28()




LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'AnyValue'), _ImportedBinding_cwt_wps_ows.CTD_ANON, scope=LiteralInputType, documentation='Specifies that any value is allowed for this parameter.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 86, 1)))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'AllowedValues'), _ImportedBinding_cwt_wps_ows.CTD_ANON_3, scope=LiteralInputType, documentation='List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 136, 1)))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DefaultValue'), pyxb.binding.datatypes.string, scope=LiteralInputType, documentation='Optional default value for this quantity, which should be included when this quantity has a default value.  The DefaultValue shall be understood to be consistent with the unit of measure selected in the Execute request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 156, 5)))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValuesReference'), ValuesReferenceType, scope=LiteralInputType, documentation='Indicates that there are a finite set of values and ranges allowed for this input, which are specified in the referenced list. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 181, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 408, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 156, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'DataType')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 408, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, 'UOMs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 413, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AllowedValues')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 171, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'AnyValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 176, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, 'ValuesReference')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 181, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, 'DefaultValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 156, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LiteralInputType._Automaton = _BuildAutomaton_29()




def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SupportedComplexDataInputType._UseForTag(pyxb.namespace.ExpandedName(None, 'Default')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SupportedComplexDataInputType._UseForTag(pyxb.namespace.ExpandedName(None, 'Supported')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 307, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedComplexDataInputType._Automaton = _BuildAutomaton_30()




OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplexOutput'), SupportedComplexDataType, scope=OutputDescriptionType, documentation='Indicates that this Output shall be a complex data structure (such as a GML fragment) that is returned by the execute operation response. The value of this complex data structure can be output either embedded in the execute operation response or remotely accessible to the client. When this output form is indicated, the process produces only a single output, and "store" is "false, the output shall be returned directly, without being embedded in the XML document that is otherwise provided by execute operation response. \n\t\t\t\t\tThis element also provides a list of format, encoding, and schema combinations supported for this output. The client can select from among the identified combinations of formats, encodings, and schemas to specify the form of the output. This allows for complete specification of particular versions of GML, or image formats. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 384, 3)))

OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LiteralOutput'), LiteralOutputType, scope=OutputDescriptionType, documentation='Indicates that this output shall be a simple literal value (such as an integer) that is embedded in the execute response, and describes that output. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 390, 3)))

OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BoundingBoxOutput'), SupportedCRSsType, scope=OutputDescriptionType, documentation='Indicates that this output shall be a BoundingBox data structure, and provides a list of the CRSs supported in these Bounding Boxes. This element shall be included when this process output is an ows:BoundingBox element. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 395, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplexOutput')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 384, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'LiteralOutput')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 390, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'BoundingBoxOutput')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 395, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutputDescriptionType._Automaton = _BuildAutomaton_31()




OutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), _ImportedBinding_cwt_wps_ows.CodeType, scope=OutputDefinitionType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 145, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutputDefinitionType._Automaton = _BuildAutomaton_32()




InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), CTD_ANON_4, scope=InputReferenceType, documentation='Extra HTTP request headers needed by the service identified in ../Reference/@href.  For example, an HTTP SOAP request requires a SOAPAction header.  This permits the creation of a complete and valid POST request.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 257, 3)))

InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Body'), pyxb.binding.datatypes.anyType, scope=InputReferenceType, documentation='The contents of this element to be used as the body of the HTTP request message to be sent to the service identified in ../Reference/@href.  For example, it could be an XML encoded WFS request using HTTP POST', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 275, 4)))

InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BodyReference'), CTD_ANON_10, scope=InputReferenceType, documentation='Reference to a remote document to be used as the body of the an HTTP POST request message to the service identified in ../Reference/@href.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 280, 4)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 256, 2))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 257, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 274, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 257, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Body')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 275, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BodyReference')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 280, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InputReferenceType._Automaton = _BuildAutomaton_33()




def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=None)
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), None)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ComplexDataType._Automaton = _BuildAutomaton_34()




OutputDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), OutputReferenceType, scope=OutputDataType, documentation='Identifies this output as a web accessible resource, and references that resource.  This element shall only be used for complex data. This element shall be used by a server when "store" in the Execute request is "true". ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 121, 3)))

OutputDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Data'), DataType, scope=OutputDataType, documentation='Identifies this output value as a data embedded in this response, and includes that data. This element shall be used by a server when "store" in the Execute request is "false". ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 126, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 121, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Data')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 126, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OutputDataType._Automaton = _BuildAutomaton_35()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), _ImportedBinding_cwt_wps_ows.AcceptVersionsType, scope=CTD_ANON_11, documentation='When omitted, server shall return latest supported version. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 25, 4)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 25, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_request.xsd', 25, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_36()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), _ImportedBinding_cwt_wps_ows.CodeType, scope=CTD_ANON_12, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_request.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_37()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ProcessDescription'), ProcessDescriptionType, scope=CTD_ANON_13, documentation='Ordered list of one or more full Process descriptions, listed in the order in which they were requested in the DescribeProcess operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 33, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'ProcessDescription')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 33, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_38()




ProcessDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataInputs'), CTD_ANON, scope=ProcessDescriptionType, documentation='List of the inputs to this process. In almost all cases, at least one process input is required. However, no process inputs may be identified when all the inputs are predetermined fixed resources.  In this case, those resources shall be identified in the ows:Abstract element that describes the process.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 51, 5)))

ProcessDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ProcessOutputs'), CTD_ANON_, scope=ProcessDescriptionType, documentation='List of outputs which will or can result from executing the process. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 65, 5)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 33, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 51, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/DescriptionType.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Profile')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 28, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WSDL')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/ProcessBriefType.xsd', 33, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'DataInputs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 51, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ProcessOutputs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsDescribeProcess_response.xsd', 65, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProcessDescriptionType._Automaton = _BuildAutomaton_39()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier'), _ImportedBinding_cwt_wps_ows.CodeType, scope=CTD_ANON_14, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataInputs'), DataInputsType, scope=CTD_ANON_14, documentation='List of input (or parameter) values provided to the process, including each of the Inputs needed to execute the process. It is possible to have no inputs provided only when all the inputs are predetermined fixed resources. In all other cases, at least one input is required. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 37, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseForm'), ResponseFormType, scope=CTD_ANON_14, documentation='Defines the response type of the WPS, either raw data or XML document.  If absent, the response shall be a response document which includes all outputs encoded in the response.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 42, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 37, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 42, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataInputs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 37, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseForm')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 42, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_40()




DocumentOutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=DocumentOutputDefinitionType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1)))

DocumentOutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract'), _ImportedBinding_cwt_wps_ows.LanguageStringType, scope=DocumentOutputDefinitionType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 120, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 125, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 145, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 120, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd', 125, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentOutputDefinitionType._Automaton = _BuildAutomaton_41()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Process'), ProcessBriefType, scope=CTD_ANON_15, documentation='Process description from the ProcessOfferings section of the GetCapabilities response. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 35, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), StatusType, scope=CTD_ANON_15, documentation='Execution status of this process. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 40, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataInputs'), DataInputsType, scope=CTD_ANON_15, documentation='Inputs that were provided as part of the execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 45, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputDefinitions'), OutputDefinitionsType, scope=CTD_ANON_15, documentation='Complete list of Output data types that were requested as part of the Execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 50, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessOutputs'), CTD_ANON_5, scope=CTD_ANON_15, documentation='List of values of the Process output parameters. Normally there would be at least one output when the process has completed successfully. If the process has not finished executing, the implementer can choose to include whatever final results are ready at the time the Execute response is provided. If the reference locations of outputs are known in advance, these URLs may be provided before they are populated. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 55, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 45, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 50, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 55, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Process')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 40, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataInputs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 45, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputDefinitions')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessOutputs')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsExecute_response.xsd', 55, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_42()




WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WSDL'), CTD_ANON_9, scope=WPSCapabilitiesType, documentation='Location of a WSDL document.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/common/WSDL.xsd', 17, 1)))

WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Languages'), CTD_ANON_6, scope=WPSCapabilitiesType, documentation='Listing of the default and other languages supported by this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 54, 1)))

WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProcessOfferings'), CTD_ANON_8, scope=WPSCapabilitiesType, documentation='List of brief descriptions of the processes offered by this WPS server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 96, 1)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 42, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceIdentification')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'ServiceProvider')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ows, 'OperationsMetadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProcessOfferings')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 36, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Languages')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 37, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WSDL')), pyxb.utils.utility.Location('http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd', 42, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WPSCapabilitiesType._Automaton = _BuildAutomaton_43()

