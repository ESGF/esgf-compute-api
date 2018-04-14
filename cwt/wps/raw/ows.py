# ../../cwt/wps/raw/ows.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:30267ec97faf153699f3ab2e8f18d125f769245d
# Generated 2018-04-13 20:08:17.421392 by PyXB version 1.2.6 using Python 2.7.14.final.0
# Namespace http://www.opengis.net/ows/1.1 [xmlns:ows]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:10b4e914-3f91-11e8-9b32-708bcda56936')

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
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/ows/1.1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
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


# Atomic simple type: {http://www.opengis.net/ows/1.1}MimeType
class MimeType (pyxb.binding.datatypes.string):

    """XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MimeType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 24, 1)
    _Documentation = 'XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. '
MimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
MimeType._CF_pattern.addPattern(pattern='(application|audio|image|text|video|message|multipart|model)/.+(;\\s*.+=.+)*')
MimeType._InitializeFacetMap(MimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MimeType', MimeType)
_module_typeBindings.MimeType = MimeType

# Atomic simple type: {http://www.opengis.net/ows/1.1}VersionType
class VersionType (pyxb.binding.datatypes.string):

    """Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VersionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 33, 1)
    _Documentation = 'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. '
VersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
VersionType._CF_pattern.addPattern(pattern='\\d+\\.\\d?\\d\\.\\d?\\d')
VersionType._InitializeFacetMap(VersionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VersionType', VersionType)
_module_typeBindings.VersionType = VersionType

# List simple type: {http://www.opengis.net/ows/1.1}PositionType
# superclasses pyxb.binding.datatypes.anySimpleType
class PositionType (pyxb.binding.basis.STD_list):

    """Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:
a)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 103, 1)
    _Documentation = 'Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:\na)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. '

    _ItemType = pyxb.binding.datatypes.double
PositionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PositionType', PositionType)
_module_typeBindings.PositionType = PositionType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.NMTOKENS, pyxb.binding.basis.enumeration_mixin
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 209, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='closed', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='open', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='open-closed', tag=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='closed-open', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 39, 4)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='\\d+\\.\\d?\\d\\.\\d?\\d')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.opengis.net/ows/1.1}ServiceType
class ServiceType (pyxb.binding.datatypes.string):

    """Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 73, 1)
    _Documentation = 'Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". '
ServiceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ServiceType', ServiceType)
_module_typeBindings.ServiceType = ServiceType

# Atomic simple type: {http://www.opengis.net/ows/1.1}UpdateSequenceType
class UpdateSequenceType (pyxb.binding.datatypes.string):

    """Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 98, 1)
    _Documentation = 'Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. '
UpdateSequenceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UpdateSequenceType', UpdateSequenceType)
_module_typeBindings.UpdateSequenceType = UpdateSequenceType

# List simple type: {http://www.opengis.net/ows/1.1}PositionType2D
# superclasses PositionType
class PositionType2D (pyxb.binding.basis.STD_list):

    """Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:
a)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionType2D')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 148, 1)
    _Documentation = 'Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:\na)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. '

    _ItemType = pyxb.binding.datatypes.double
PositionType2D._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
PositionType2D._InitializeFacetMap(PositionType2D._CF_length)
Namespace.addCategoryObject('typeBinding', 'PositionType2D', PositionType2D)
_module_typeBindings.PositionType2D = PositionType2D

# Complex type {http://www.opengis.net/ows/1.1}LanguageStringType with content type SIMPLE
class LanguageStringType (pyxb.binding.basis.complexTypeDefinition):
    """Text string with the language of the string identified as recommended in the XML 1.0 W3C Recommendation, section 2.12. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageStringType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows1_1_LanguageStringType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 31, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.LanguageStringType = LanguageStringType
Namespace.addCategoryObject('typeBinding', 'LanguageStringType', LanguageStringType)


# Complex type {http://www.opengis.net/ows/1.1}KeywordsType with content type ELEMENT_ONLY
class KeywordsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of one or more commonly used or formalised word(s) or phrase(s) used to describe the subject. When needed, the optional "type" can name the type of the associated list of keywords that shall all have the same type. Also when needed, the codeSpace attribute of that "type" can reference the type name authority and/or thesaurus.
			If the xml:lang attribute is not included in a Keyword element, then no language is specified for that element unless specified by another means.  All Keyword elements in the same Keywords element that share the same xml:lang attribute value represent different keywords in that language. For OWS use, the optional thesaurusName element was omitted as being complex information that could be referenced by the codeSpace attribute of the Type element. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeywordsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 50, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Keyword uses Python identifier Keyword
    __Keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), 'Keyword', '__httpwww_opengis_netows1_1_KeywordsType_httpwww_opengis_netows1_1Keyword', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 57, 3), )

    
    Keyword = property(__Keyword.value, __Keyword.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__httpwww_opengis_netows1_1_KeywordsType_httpwww_opengis_netows1_1Type', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 58, 3), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Keyword.name() : __Keyword,
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.KeywordsType = KeywordsType
Namespace.addCategoryObject('typeBinding', 'KeywordsType', KeywordsType)


# Complex type {http://www.opengis.net/ows/1.1}CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    """Name or code with an (optional) authority. If the codeSpace attribute is present, its value shall reference a dictionary, thesaurus, or authority for the name or code, such as the organisation who assigned the value, or the dictionary from which it is taken. Type copied from basicTypes.xsd of GML 3 with documentation edited, for possible use outside the ServiceIdentification section of a service metadata document. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 62, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_opengis_netows1_1_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 69, 4)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 69, 4)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {http://www.opengis.net/ows/1.1}ResponsiblePartyType with content type ELEMENT_ONLY
class ResponsiblePartyType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with, person responsible for the server. At least one of IndividualName, OrganisationName, or PositionName shall be included. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartyType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 81, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1IndividualName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 108, 1), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name, title separated by a delimiter. ')

    
    # Element {http://www.opengis.net/ows/1.1}OrganisationName uses Python identifier OrganisationName
    __OrganisationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), 'OrganisationName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1OrganisationName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 114, 1), )

    
    OrganisationName = property(__OrganisationName.value, __OrganisationName.set, None, 'Name of the responsible organization. ')

    
    # Element {http://www.opengis.net/ows/1.1}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1PositionName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 120, 1), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows/1.1}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1Role', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 126, 1), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows/1.1}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1ContactInfo', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 132, 1), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party. ')

    _ElementMap.update({
        __IndividualName.name() : __IndividualName,
        __OrganisationName.name() : __OrganisationName,
        __PositionName.name() : __PositionName,
        __Role.name() : __Role,
        __ContactInfo.name() : __ContactInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponsiblePartyType = ResponsiblePartyType
Namespace.addCategoryObject('typeBinding', 'ResponsiblePartyType', ResponsiblePartyType)


# Complex type {http://www.opengis.net/ows/1.1}ResponsiblePartySubsetType with content type ELEMENT_ONLY
class ResponsiblePartySubsetType (pyxb.binding.basis.complexTypeDefinition):
    """Identification of, and means of communication with, person responsible for the server. For OWS use in the ServiceProvider section of a service metadata document, the optional organizationName element was removed, since this type is always used with the ProviderName element which provides that information. The mandatory "role" element was changed to optional, since no clear use of this information is known in the ServiceProvider section. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponsiblePartySubsetType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 95, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), 'IndividualName', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1IndividualName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 108, 1), )

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, 'Name of the responsible person: surname, given name, title separated by a delimiter. ')

    
    # Element {http://www.opengis.net/ows/1.1}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), 'PositionName', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1PositionName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 120, 1), )

    
    PositionName = property(__PositionName.value, __PositionName.set, None, 'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows/1.1}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Role'), 'Role', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1Role', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 126, 1), )

    
    Role = property(__Role.value, __Role.set, None, 'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows/1.1}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1ContactInfo', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 132, 1), )

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, 'Address of the responsible party. ')

    _ElementMap.update({
        __IndividualName.name() : __IndividualName,
        __PositionName.name() : __PositionName,
        __Role.name() : __Role,
        __ContactInfo.name() : __ContactInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponsiblePartySubsetType = ResponsiblePartySubsetType
Namespace.addCategoryObject('typeBinding', 'ResponsiblePartySubsetType', ResponsiblePartySubsetType)


# Complex type {http://www.opengis.net/ows/1.1}ContactType with content type ELEMENT_ONLY
class ContactType (pyxb.binding.basis.complexTypeDefinition):
    """Information required to enable contact with the responsible person and/or organization. For OWS use in the service metadata document, the optional hoursOfService and contactInstructions elements were retained, as possibly being useful in the ServiceProvider section. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 138, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Phone uses Python identifier Phone
    __Phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Phone'), 'Phone', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1Phone', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 144, 3), )

    
    Phone = property(__Phone.value, __Phone.set, None, 'Telephone numbers at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows/1.1}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1Address', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 149, 3), )

    
    Address = property(__Address.value, __Address.set, None, 'Physical and email address at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows/1.1}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1OnlineResource', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 154, 3), )

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, 'On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleAttrs attribute group should not be used. ')

    
    # Element {http://www.opengis.net/ows/1.1}HoursOfService uses Python identifier HoursOfService
    __HoursOfService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), 'HoursOfService', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1HoursOfService', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 159, 3), )

    
    HoursOfService = property(__HoursOfService.value, __HoursOfService.set, None, 'Time period (including time zone) when individuals can contact the organization or individual. ')

    
    # Element {http://www.opengis.net/ows/1.1}ContactInstructions uses Python identifier ContactInstructions
    __ContactInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), 'ContactInstructions', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1ContactInstructions', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 164, 3), )

    
    ContactInstructions = property(__ContactInstructions.value, __ContactInstructions.set, None, 'Supplemental instructions on how or when to contact the individual or organization. ')

    _ElementMap.update({
        __Phone.name() : __Phone,
        __Address.name() : __Address,
        __OnlineResource.name() : __OnlineResource,
        __HoursOfService.name() : __HoursOfService,
        __ContactInstructions.name() : __ContactInstructions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContactType = ContactType
Namespace.addCategoryObject('typeBinding', 'ContactType', ContactType)


# Complex type {http://www.opengis.net/ows/1.1}TelephoneType with content type ELEMENT_ONLY
class TelephoneType (pyxb.binding.basis.complexTypeDefinition):
    """Telephone numbers for contacting the responsible individual or organization. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TelephoneType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Voice uses Python identifier Voice
    __Voice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Voice'), 'Voice', '__httpwww_opengis_netows1_1_TelephoneType_httpwww_opengis_netows1_1Voice', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 185, 3), )

    
    Voice = property(__Voice.value, __Voice.set, None, 'Telephone number by which individuals can speak to the responsible organization or individual. ')

    
    # Element {http://www.opengis.net/ows/1.1}Facsimile uses Python identifier Facsimile
    __Facsimile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), 'Facsimile', '__httpwww_opengis_netows1_1_TelephoneType_httpwww_opengis_netows1_1Facsimile', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 190, 3), )

    
    Facsimile = property(__Facsimile.value, __Facsimile.set, None, 'Telephone number of a facsimile machine for the responsible\norganization or individual. ')

    _ElementMap.update({
        __Voice.name() : __Voice,
        __Facsimile.name() : __Facsimile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TelephoneType = TelephoneType
Namespace.addCategoryObject('typeBinding', 'TelephoneType', TelephoneType)


# Complex type {http://www.opengis.net/ows/1.1}AddressType with content type ELEMENT_ONLY
class AddressType (pyxb.binding.basis.complexTypeDefinition):
    """Location of the responsible individual or organization. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 199, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}DeliveryPoint uses Python identifier DeliveryPoint
    __DeliveryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), 'DeliveryPoint', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1DeliveryPoint', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 204, 3), )

    
    DeliveryPoint = property(__DeliveryPoint.value, __DeliveryPoint.set, None, 'Address line for the location. ')

    
    # Element {http://www.opengis.net/ows/1.1}City uses Python identifier City
    __City = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'City'), 'City', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1City', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 209, 3), )

    
    City = property(__City.value, __City.set, None, 'City of the location. ')

    
    # Element {http://www.opengis.net/ows/1.1}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), 'AdministrativeArea', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1AdministrativeArea', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 214, 3), )

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, 'State or province of the location. ')

    
    # Element {http://www.opengis.net/ows/1.1}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1PostalCode', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 219, 3), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'ZIP or other postal code. ')

    
    # Element {http://www.opengis.net/ows/1.1}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1Country', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 224, 3), )

    
    Country = property(__Country.value, __Country.set, None, 'Country of the physical address. ')

    
    # Element {http://www.opengis.net/ows/1.1}ElectronicMailAddress uses Python identifier ElectronicMailAddress
    __ElectronicMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), 'ElectronicMailAddress', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1ElectronicMailAddress', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 229, 3), )

    
    ElectronicMailAddress = property(__ElectronicMailAddress.value, __ElectronicMailAddress.set, None, 'Address of the electronic mailbox of the responsible organization or individual. ')

    _ElementMap.update({
        __DeliveryPoint.name() : __DeliveryPoint,
        __City.name() : __City,
        __AdministrativeArea.name() : __AdministrativeArea,
        __PostalCode.name() : __PostalCode,
        __Country.name() : __Country,
        __ElectronicMailAddress.name() : __ElectronicMailAddress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressType = AddressType
Namespace.addCategoryObject('typeBinding', 'AddressType', AddressType)


# Complex type {http://www.opengis.net/ows/1.1}BoundingBoxType with content type ELEMENT_ONLY
class BoundingBoxType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded minimum rectangular bounding box (or region) parameter, surrounding all the associated data. This type is adapted from the EnvelopeType of GML 3.1, with modified contents and documentation for encoding a MINIMUM size box SURROUNDING all associated data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 72, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}LowerCorner uses Python identifier LowerCorner
    __LowerCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), 'LowerCorner', '__httpwww_opengis_netows1_1_BoundingBoxType_httpwww_opengis_netows1_1LowerCorner', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 78, 3), )

    
    LowerCorner = property(__LowerCorner.value, __LowerCorner.set, None, 'Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Element {http://www.opengis.net/ows/1.1}UpperCorner uses Python identifier UpperCorner
    __UpperCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), 'UpperCorner', '__httpwww_opengis_netows1_1_BoundingBoxType_httpwww_opengis_netows1_1UpperCorner', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 83, 3), )

    
    UpperCorner = property(__UpperCorner.value, __UpperCorner.set, None, 'Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows1_1_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI)
    __crs._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 89, 2)
    __crs._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 89, 2)
    
    crs = property(__crs.value, __crs.set, None, 'Usually references the definition of a CRS, as specified in [OGC Topic 2]. Such a CRS definition can be XML encoded using the gml:CoordinateReferenceSystemType in [GML 3.1]. For well known references, it is not required that a CRS definition exist at the location the URI points to. If no anyURI value is included, the applicable CRS must be either:\na)\tSpecified outside the bounding box, but inside a data structure that includes this bounding box, as specified for a specific OWS use of this bounding box type.\nb)\tFixed and specified in the Implementation Specification for a specific OWS use of the bounding box type. ')

    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows1_1_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger)
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 96, 2)
    __dimensions._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 96, 2)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

    _ElementMap.update({
        __LowerCorner.name() : __LowerCorner,
        __UpperCorner.name() : __UpperCorner
    })
    _AttributeMap.update({
        __crs.name() : __crs,
        __dimensions.name() : __dimensions
    })
_module_typeBindings.BoundingBoxType = BoundingBoxType
Namespace.addCategoryObject('typeBinding', 'BoundingBoxType', BoundingBoxType)


# Complex type {http://www.opengis.net/ows/1.1}ContentsBaseType with content type ELEMENT_ONLY
class ContentsBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Contents of typical Contents section of an OWS service metadata (Capabilities) document. This type shall be extended and/or restricted if needed for specific OWS use to include the specific metadata needed. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContentsBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 24, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OtherSource uses Python identifier OtherSource
    __OtherSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), 'OtherSource', '__httpwww_opengis_netows1_1_ContentsBaseType_httpwww_opengis_netows1_1OtherSource', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 42, 1), )

    
    OtherSource = property(__OtherSource.value, __OtherSource.set, None, 'Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. ')

    
    # Element {http://www.opengis.net/ows/1.1}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows1_1_ContentsBaseType_httpwww_opengis_netows1_1DatasetDescriptionSummary', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 48, 1), )

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)

    _ElementMap.update({
        __OtherSource.name() : __OtherSource,
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContentsBaseType = ContentsBaseType
Namespace.addCategoryObject('typeBinding', 'ContentsBaseType', ContentsBaseType)


# Complex type {http://www.opengis.net/ows/1.1}DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Human-readable descriptive information for the object it is included within.
This type shall be extended if needed for specific OWS use to include additional metadata for each type of information. This type shall not be restricted for a specific OWS to change the multiplicity (or optionality) of some elements.
			If the xml:lang attribute is not included in a Title, Abstract or Keyword element, then no language is specified for that element unless specified by another means.  All Title, Abstract and Keyword elements in the same Description that share the same xml:lang attribute value represent the description of the parent object in that language. Multiple Title or Abstract elements shall not exist in the same Description with the same xml:lang attribute value unless otherwise specified. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Title', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1), )

    
    Title = property(__Title.value, __Title.set, None, 'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Abstract', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), 'Keywords', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Keywords', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 48, 1), )

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    _ElementMap.update({
        __Title.name() : __Title,
        __Abstract.name() : __Abstract,
        __Keywords.name() : __Keywords
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DescriptionType = DescriptionType
Namespace.addCategoryObject('typeBinding', 'DescriptionType', DescriptionType)


# Complex type {http://www.opengis.net/ows/1.1}UnNamedDomainType with content type ELEMENT_ONLY
class UnNamedDomainType (pyxb.binding.basis.complexTypeDefinition):
    """Valid domain (or allowed set of values) of one quantity, with needed metadata but without a quantity name or identifier. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnNamedDomainType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 40, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}AnyValue uses Python identifier AnyValue
    __AnyValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), 'AnyValue', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1AnyValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 86, 1), )

    
    AnyValue = property(__AnyValue.value, __AnyValue.set, None, 'Specifies that any value is allowed for this parameter.')

    
    # Element {http://www.opengis.net/ows/1.1}NoValues uses Python identifier NoValues
    __NoValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), 'NoValues', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1NoValues', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 93, 1), )

    
    NoValues = property(__NoValues.value, __NoValues.set, None, 'Specifies that no values are allowed for this parameter or quantity.')

    
    # Element {http://www.opengis.net/ows/1.1}ValuesReference uses Python identifier ValuesReference
    __ValuesReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), 'ValuesReference', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1ValuesReference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 100, 1), )

    
    ValuesReference = property(__ValuesReference.value, __ValuesReference.set, None, 'Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) ')

    
    # Element {http://www.opengis.net/ows/1.1}AllowedValues uses Python identifier AllowedValues
    __AllowedValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), 'AllowedValues', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1AllowedValues', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 136, 1), )

    
    AllowedValues = property(__AllowedValues.value, __AllowedValues.set, None, 'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ')

    
    # Element {http://www.opengis.net/ows/1.1}DefaultValue uses Python identifier DefaultValue
    __DefaultValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), 'DefaultValue', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1DefaultValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 159, 1), )

    
    DefaultValue = property(__DefaultValue.value, __DefaultValue.set, None, 'The default value for a quantity for which multiple values are allowed. ')

    
    # Element {http://www.opengis.net/ows/1.1}Meaning uses Python identifier Meaning
    __Meaning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), 'Meaning', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1Meaning', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 256, 1), )

    
    Meaning = property(__Meaning.value, __Meaning.set, None, 'Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ')

    
    # Element {http://www.opengis.net/ows/1.1}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataType'), 'DataType', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1DataType', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 262, 1), )

    
    DataType = property(__DataType.value, __DataType.set, None, 'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}ReferenceSystem uses Python identifier ReferenceSystem
    __ReferenceSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), 'ReferenceSystem', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1ReferenceSystem', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 268, 1), )

    
    ReferenceSystem = property(__ReferenceSystem.value, __ReferenceSystem.set, None, 'Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UOM'), 'UOM', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1UOM', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1), )

    
    UOM = property(__UOM.value, __UOM.set, None, 'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __AnyValue.name() : __AnyValue,
        __NoValues.name() : __NoValues,
        __ValuesReference.name() : __ValuesReference,
        __AllowedValues.name() : __AllowedValues,
        __DefaultValue.name() : __DefaultValue,
        __Meaning.name() : __Meaning,
        __DataType.name() : __DataType,
        __ReferenceSystem.name() : __ReferenceSystem,
        __UOM.name() : __UOM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UnNamedDomainType = UnNamedDomainType
Namespace.addCategoryObject('typeBinding', 'UnNamedDomainType', UnNamedDomainType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Specifies that any value is allowed for this parameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Specifies that no values are allowed for this parameter or quantity."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 104, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpwww_opengis_netows1_1_CTD_ANON_2_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI, required=True)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 250, 1)
    __reference._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 110, 5)
    
    reference = property(__reference.value, __reference.set, None, 'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference.name() : __reference
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 140, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1Value', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 148, 1), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Range uses Python identifier Range
    __Range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Range'), 'Range', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1Range', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 165, 1), )

    
    Range = property(__Range.value, __Range.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value,
        __Range.name() : __Range
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.opengis.net/ows/1.1}ValueType with content type SIMPLE
class ValueType (pyxb.binding.basis.complexTypeDefinition):
    """A single value, encoded as a string. This type can be used for one value, for a spacing between allowed values, or for the default value of a parameter. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 150, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ValueType = ValueType
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)


# Complex type {http://www.opengis.net/ows/1.1}DomainMetadataType with content type SIMPLE
class DomainMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """References metadata about a quantity, and provides a name for this metadata. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 236, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpwww_opengis_netows1_1_DomainMetadataType_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 250, 1)
    __reference._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 245, 4)
    
    reference = property(__reference.value, __reference.set, None, 'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference.name() : __reference
    })
_module_typeBindings.DomainMetadataType = DomainMetadataType
Namespace.addCategoryObject('typeBinding', 'DomainMetadataType', DomainMetadataType)


# Complex type {http://www.opengis.net/ows/1.1}ExceptionType with content type ELEMENT_ONLY
class ExceptionType (pyxb.binding.basis.complexTypeDefinition):
    """An Exception element describes one detected error that a server chooses to convey to the client. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExceptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ExceptionText uses Python identifier ExceptionText
    __ExceptionText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), 'ExceptionText', '__httpwww_opengis_netows1_1_ExceptionType_httpwww_opengis_netows1_1ExceptionText', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 60, 3), )

    
    ExceptionText = property(__ExceptionText.value, __ExceptionText.set, None, 'Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. ')

    
    # Attribute exceptionCode uses Python identifier exceptionCode
    __exceptionCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exceptionCode'), 'exceptionCode', '__httpwww_opengis_netows1_1_ExceptionType_exceptionCode', pyxb.binding.datatypes.string, required=True)
    __exceptionCode._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 66, 2)
    __exceptionCode._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 66, 2)
    
    exceptionCode = property(__exceptionCode.value, __exceptionCode.set, None, 'A code representing the type of this exception, which shall be selected from a set of exceptionCode values specified for the specific service operation and server. ')

    
    # Attribute locator uses Python identifier locator
    __locator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locator'), 'locator', '__httpwww_opengis_netows1_1_ExceptionType_locator', pyxb.binding.datatypes.string)
    __locator._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 71, 2)
    __locator._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 71, 2)
    
    locator = property(__locator.value, __locator.set, None, "When included, this locator shall indicate to the client where an exception was encountered in servicing the client's operation request. This locator should be included whenever meaningful information can be provided by the server. The contents of this locator will depend on the specific exceptionCode and OWS service, and shall be specified in the OWS Implementation Specification. ")

    _ElementMap.update({
        __ExceptionText.name() : __ExceptionText
    })
    _AttributeMap.update({
        __exceptionCode.name() : __exceptionCode,
        __locator.name() : __locator
    })
_module_typeBindings.ExceptionType = ExceptionType
Namespace.addCategoryObject('typeBinding', 'ExceptionType', ExceptionType)


# Complex type {http://www.opengis.net/ows/1.1}AcceptVersionsType with content type ELEMENT_ONLY
class AcceptVersionsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of one or more specification versions accepted by client, with preferred versions listed first. See Version negotiation subclause for more information. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptVersionsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 80, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Version'), 'Version', '__httpwww_opengis_netows1_1_AcceptVersionsType_httpwww_opengis_netows1_1Version', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 85, 3), )

    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __Version.name() : __Version
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptVersionsType = AcceptVersionsType
Namespace.addCategoryObject('typeBinding', 'AcceptVersionsType', AcceptVersionsType)


# Complex type {http://www.opengis.net/ows/1.1}SectionsType with content type ELEMENT_ONLY
class SectionsType (pyxb.binding.basis.complexTypeDefinition):
    """Unordered list of zero or more names of requested sections in complete service metadata document. Each Section value shall contain an allowed section name as specified by each OWS specification. See Sections parameter subclause for more information.  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SectionsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 89, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Section'), 'Section', '__httpwww_opengis_netows1_1_SectionsType_httpwww_opengis_netows1_1Section', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 94, 3), )

    
    Section = property(__Section.value, __Section.set, None, None)

    _ElementMap.update({
        __Section.name() : __Section
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SectionsType = SectionsType
Namespace.addCategoryObject('typeBinding', 'SectionsType', SectionsType)


# Complex type {http://www.opengis.net/ows/1.1}AcceptFormatsType with content type ELEMENT_ONLY
class AcceptFormatsType (pyxb.binding.basis.complexTypeDefinition):
    """Prioritized sequence of zero or more GetCapabilities operation response formats desired by client, with preferred formats listed first. Each response format shall be identified by its MIME type. See AcceptFormats parameter use subclause for more information. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AcceptFormatsType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 105, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_AcceptFormatsType_httpwww_opengis_netows1_1OutputFormat', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 110, 3), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, None)

    _ElementMap.update({
        __OutputFormat.name() : __OutputFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AcceptFormatsType = AcceptFormatsType
Namespace.addCategoryObject('typeBinding', 'AcceptFormatsType', AcceptFormatsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_opengis_netows1_1Parameter', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 36, 4), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_opengis_netows1_1Constraint', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 41, 4), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}ExtendedCapabilities uses Python identifier ExtendedCapabilities
    __ExtendedCapabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), 'ExtendedCapabilities', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_opengis_netows1_1ExtendedCapabilities', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 51, 1), )

    
    ExtendedCapabilities = property(__ExtendedCapabilities.value, __ExtendedCapabilities.set, None, 'Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ')

    
    # Element {http://www.opengis.net/ows/1.1}Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Operation'), 'Operation', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_opengis_netows1_1Operation', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 57, 1), )

    
    Operation = property(__Operation.value, __Operation.set, None, 'Metadata for one operation that this server implements. ')

    _ElementMap.update({
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __ExtendedCapabilities.name() : __ExtendedCapabilities,
        __Operation.name() : __Operation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata for one operation that this server implements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Parameter', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 68, 4), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, 'Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Constraint', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 73, 4), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}DCP uses Python identifier DCP
    __DCP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DCP'), 'DCP', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1DCP', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 92, 1), )

    
    DCP = property(__DCP.value, __DCP.set, None, 'Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows1_1_CTD_ANON_5_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 84, 3)
    __name._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 84, 3)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this operation (request) (for example, GetCapabilities). The list of required and optional operations implemented shall be specified in the Implementation Specification for this service. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint,
        __DCP.name() : __DCP
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.
"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}HTTP uses Python identifier HTTP
    __HTTP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), 'HTTP', '__httpwww_opengis_netows1_1_CTD_ANON_6_httpwww_opengis_netows1_1HTTP', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 104, 1), )

    
    HTTP = property(__HTTP.value, __HTTP.set, None, 'Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ')

    _ElementMap.update({
        __HTTP.name() : __HTTP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 108, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Get uses Python identifier Get
    __Get = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Get'), 'Get', '__httpwww_opengis_netows1_1_CTD_ANON_7_httpwww_opengis_netows1_1Get', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 110, 4), )

    
    Get = property(__Get.value, __Get.set, None, 'Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. ')

    
    # Element {http://www.opengis.net/ows/1.1}Post uses Python identifier Post
    __Post = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Post'), 'Post', '__httpwww_opengis_netows1_1_CTD_ANON_7_httpwww_opengis_netows1_1Post', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 115, 4), )

    
    Post = property(__Post.value, __Post.set, None, 'Connect point URL and any constraints for the HTTP "Post" request method for this operation request. ')

    _ElementMap.update({
        __Get.name() : __Get,
        __Post.name() : __Post
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Metadata about the organization that provides this specific service instance or server. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ProviderName uses Python identifier ProviderName
    __ProviderName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), 'ProviderName', '__httpwww_opengis_netows1_1_CTD_ANON_8_httpwww_opengis_netows1_1ProviderName', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 30, 4), )

    
    ProviderName = property(__ProviderName.value, __ProviderName.set, None, 'A unique identifier for the service provider organization. ')

    
    # Element {http://www.opengis.net/ows/1.1}ProviderSite uses Python identifier ProviderSite
    __ProviderSite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), 'ProviderSite', '__httpwww_opengis_netows1_1_CTD_ANON_8_httpwww_opengis_netows1_1ProviderSite', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 35, 4), )

    
    ProviderSite = property(__ProviderSite.value, __ProviderSite.set, None, 'Reference to the most relevant web site of the service provider. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceContact uses Python identifier ServiceContact
    __ServiceContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), 'ServiceContact', '__httpwww_opengis_netows1_1_CTD_ANON_8_httpwww_opengis_netows1_1ServiceContact', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 40, 4), )

    
    ServiceContact = property(__ServiceContact.value, __ServiceContact.set, None, 'Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. ')

    _ElementMap.update({
        __ProviderName.name() : __ProviderName,
        __ProviderSite.name() : __ProviderSite,
        __ServiceContact.name() : __ServiceContact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {http://www.opengis.net/ows/1.1}OnlineResourceType with content type EMPTY
class OnlineResourceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference to on-line resource from which data can be obtained. For OWS use in the service metadata document, the CI_OnlineResource class was XML encoded as the attributeGroup "xlink:simpleAttrs", as used in GML. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnlineResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinktype', _ImportedBinding_cwt_wps_xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkrole', _ImportedBinding_cwt_wps_xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_cwt_wps_xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinktitle', _ImportedBinding_cwt_wps_xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkshow', _ImportedBinding_cwt_wps_xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_cwt_wps_xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.OnlineResourceType = OnlineResourceType
Namespace.addCategoryObject('typeBinding', 'OnlineResourceType', OnlineResourceType)


# Complex type {http://www.opengis.net/ows/1.1}MetadataType with content type ELEMENT_ONLY
class MetadataType (pyxb.binding.basis.complexTypeDefinition):
    """This element either references or contains more metadata about the element that includes this element. To reference metadata stored remotely, at least the xlinks:href attribute in xlink:simpleAttrs shall be included. Either at least one of the attributes in xlink:simpleAttrs or a substitute for the AbstractMetaData element shall be included, but not both. An Implementation Specification can restrict the contents of this element to always be a reference or always contain metadata. (Informative: This element was adapted from the metaDataProperty element in GML 3.0.) """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MetadataType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 44, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}AbstractMetaData uses Python identifier AbstractMetaData
    __AbstractMetaData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), 'AbstractMetaData', '__httpwww_opengis_netows1_1_MetadataType_httpwww_opengis_netows1_1AbstractMetaData', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 63, 1), )

    
    AbstractMetaData = property(__AbstractMetaData.value, __AbstractMetaData.set, None, 'Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ')

    
    # Attribute about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'about'), 'about', '__httpwww_opengis_netows1_1_MetadataType_about', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 56, 2)
    __about._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 56, 2)
    
    about = property(__about.value, __about.set, None, 'Optional reference to the aspect of the element which includes this "metadata" element that this metadata provides more information about. ')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinktype', _ImportedBinding_cwt_wps_xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkrole', _ImportedBinding_cwt_wps_xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_cwt_wps_xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinktitle', _ImportedBinding_cwt_wps_xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkshow', _ImportedBinding_cwt_wps_xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_cwt_wps_xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __AbstractMetaData.name() : __AbstractMetaData
    })
    _AttributeMap.update({
        __about.name() : __about,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.MetadataType = MetadataType
Namespace.addCategoryObject('typeBinding', 'MetadataType', MetadataType)


# Complex type {http://www.opengis.net/ows/1.1}WGS84BoundingBoxType with content type ELEMENT_ONLY
class WGS84BoundingBoxType (BoundingBoxType):
    """XML encoded minimum rectangular bounding box (or region) parameter, surrounding all the associated data. This box is specialized for use with the 2D WGS 84 coordinate reference system with decimal values of longitude and latitude. This type is adapted from the general BoundingBoxType, with modified contents and documentation for use with the 2D WGS 84 coordinate reference system. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBoxType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 115, 1)
    _ElementMap = BoundingBoxType._ElementMap.copy()
    _AttributeMap = BoundingBoxType._AttributeMap.copy()
    # Base type is BoundingBoxType
    
    # Element {http://www.opengis.net/ows/1.1}LowerCorner uses Python identifier LowerCorner
    __LowerCorner_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), 'LowerCorner', '__httpwww_opengis_netows1_1_WGS84BoundingBoxType_httpwww_opengis_netows1_1LowerCorner', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 123, 5), )

    
    LowerCorner = property(__LowerCorner_.value, __LowerCorner_.set, None, 'Position of the bounding box corner at which the values of longitude and latitude normally are the algebraic minimums within this bounding box. For more information, see Subclauses 10.4.5 and C.13. ')

    
    # Element {http://www.opengis.net/ows/1.1}UpperCorner uses Python identifier UpperCorner
    __UpperCorner_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), 'UpperCorner', '__httpwww_opengis_netows1_1_WGS84BoundingBoxType_httpwww_opengis_netows1_1UpperCorner', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 128, 5), )

    
    UpperCorner = property(__UpperCorner_.value, __UpperCorner_.set, None, 'Position of the bounding box corner at which the values of longitude and latitude normally are the algebraic minimums within this bounding box. For more information, see Subclauses 10.4.5 and C.13. ')

    
    # Attribute crs is restricted from parent
    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crs'), 'crs', '__httpwww_opengis_netows1_1_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='urn:ogc:def:crs:OGC:2:84')
    __crs._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 134, 4)
    __crs._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 134, 4)
    
    crs = property(__crs.value, __crs.set, None, 'This attribute can be included when considered useful. When included, this attribute shall reference the 2D WGS 84 coordinate reference system with longitude before latitude and decimal values of longitude and latitude. ')

    
    # Attribute dimensions is restricted from parent
    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dimensions'), 'dimensions', '__httpwww_opengis_netows1_1_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger, fixed=True, unicode_default='2')
    __dimensions._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 139, 4)
    __dimensions._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 139, 4)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, 'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

    _ElementMap.update({
        __LowerCorner_.name() : __LowerCorner_,
        __UpperCorner_.name() : __UpperCorner_
    })
    _AttributeMap.update({
        __crs.name() : __crs,
        __dimensions.name() : __dimensions
    })
_module_typeBindings.WGS84BoundingBoxType = WGS84BoundingBoxType
Namespace.addCategoryObject('typeBinding', 'WGS84BoundingBoxType', WGS84BoundingBoxType)


# Complex type {http://www.opengis.net/ows/1.1}DatasetDescriptionSummaryBaseType with content type ELEMENT_ONLY
class DatasetDescriptionSummaryBaseType (DescriptionType):
    """Typical dataset metadata in typical Contents section of an OWS service metadata (Capabilities) document. This type shall be extended and/or restricted if needed for specific OWS use, to include the specific Dataset  description metadata needed. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummaryBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 50, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1BoundingBox', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 70, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}WGS84BoundingBox uses Python identifier WGS84BoundingBox
    __WGS84BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), 'WGS84BoundingBox', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1WGS84BoundingBox', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 113, 1), )

    
    WGS84BoundingBox = property(__WGS84BoundingBox.value, __WGS84BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1DatasetDescriptionSummary', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 48, 1), )

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 62, 5), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unambiguous identifier or name of this coverage, unique for this server. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __BoundingBox.name() : __BoundingBox,
        __WGS84BoundingBox.name() : __WGS84BoundingBox,
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary,
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatasetDescriptionSummaryBaseType = DatasetDescriptionSummaryBaseType
Namespace.addCategoryObject('typeBinding', 'DatasetDescriptionSummaryBaseType', DatasetDescriptionSummaryBaseType)


# Complex type {http://www.opengis.net/ows/1.1}BasicIdentificationType with content type ELEMENT_ONLY
class BasicIdentificationType (DescriptionType):
    """Basic metadata identifying and describing a set of data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 38, 1)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_BasicIdentificationType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_BasicIdentificationType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BasicIdentificationType = BasicIdentificationType
Namespace.addCategoryObject('typeBinding', 'BasicIdentificationType', BasicIdentificationType)


# Complex type {http://www.opengis.net/ows/1.1}DomainType with content type ELEMENT_ONLY
class DomainType (UnNamedDomainType):
    """Valid domain (or allowed set of values) of one quantity, with its name or identifier. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DomainType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 25, 1)
    _ElementMap = UnNamedDomainType._ElementMap.copy()
    _AttributeMap = UnNamedDomainType._AttributeMap.copy()
    # Base type is UnNamedDomainType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element AnyValue ({http://www.opengis.net/ows/1.1}AnyValue) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element NoValues ({http://www.opengis.net/ows/1.1}NoValues) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element ValuesReference ({http://www.opengis.net/ows/1.1}ValuesReference) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element AllowedValues ({http://www.opengis.net/ows/1.1}AllowedValues) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element DefaultValue ({http://www.opengis.net/ows/1.1}DefaultValue) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element Meaning ({http://www.opengis.net/ows/1.1}Meaning) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element DataType ({http://www.opengis.net/ows/1.1}DataType) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element ReferenceSystem ({http://www.opengis.net/ows/1.1}ReferenceSystem) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element UOM ({http://www.opengis.net/ows/1.1}UOM) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netows1_1_DomainType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 31, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 31, 4)
    
    name = property(__name.value, __name.set, None, 'Name or identifier of this quantity. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.DomainType = DomainType
Namespace.addCategoryObject('typeBinding', 'DomainType', DomainType)


# Complex type {http://www.opengis.net/ows/1.1}RangeType with content type ELEMENT_ONLY
class RangeType (pyxb.binding.basis.complexTypeDefinition):
    """A range of values of a numeric parameter. This range can be continuous or discrete, defined by a fixed spacing between adjacent valid values. If the MinimumValue or MaximumValue is not included, there is no value limit in that direction. Inclusion of the specified minimum and maximum values in the range shall be defined by the rangeClosure. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 167, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}MinimumValue uses Python identifier MinimumValue
    __MinimumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), 'MinimumValue', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1MinimumValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 187, 1), )

    
    MinimumValue = property(__MinimumValue.value, __MinimumValue.set, None, 'Minimum value of this numeric parameter. ')

    
    # Element {http://www.opengis.net/ows/1.1}MaximumValue uses Python identifier MaximumValue
    __MaximumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), 'MaximumValue', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1MaximumValue', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 193, 1), )

    
    MaximumValue = property(__MaximumValue.value, __MaximumValue.set, None, 'Maximum value of this numeric parameter. ')

    
    # Element {http://www.opengis.net/ows/1.1}Spacing uses Python identifier Spacing
    __Spacing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), 'Spacing', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1Spacing', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 199, 1), )

    
    Spacing = property(__Spacing.value, __Spacing.set, None, 'The regular distance or spacing between the allowed values in a range. ')

    
    # Attribute {http://www.opengis.net/ows/1.1}rangeClosure uses Python identifier rangeClosure
    __rangeClosure = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'rangeClosure'), 'rangeClosure', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1rangeClosure', _module_typeBindings.STD_ANON, unicode_default='closed')
    __rangeClosure._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 205, 1)
    __rangeClosure._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 180, 2)
    
    rangeClosure = property(__rangeClosure.value, __rangeClosure.set, None, 'Specifies which of the minimum and maximum values are included in the range. Note that plus and minus infinity are considered closed bounds. ')

    _ElementMap.update({
        __MinimumValue.name() : __MinimumValue,
        __MaximumValue.name() : __MaximumValue,
        __Spacing.name() : __Spacing
    })
    _AttributeMap.update({
        __rangeClosure.name() : __rangeClosure
    })
_module_typeBindings.RangeType = RangeType
Namespace.addCategoryObject('typeBinding', 'RangeType', RangeType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Exception'), 'Exception', '__httpwww_opengis_netows1_1_CTD_ANON_9_httpwww_opengis_netows1_1Exception', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 53, 1), )

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows1_1_CTD_ANON_9_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 45, 3)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows1_1_CTD_ANON_9_version', _module_typeBindings.STD_ANON_, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 35, 3)
    __version._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 35, 3)
    
    version = property(__version.value, __version.set, None, 'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. ')

    _ElementMap.update({
        __Exception.name() : __Exception
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://www.opengis.net/ows/1.1}CapabilitiesBaseType with content type ELEMENT_ONLY
class CapabilitiesBaseType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, usually including metadata about the tightly-coupled data served. If the server does not implement the updateSequence parameter, the server shall always return the complete Capabilities document, without the updateSequence parameter. When the server implements the updateSequence parameter and the GetCapabilities operation request included the updateSequence parameter with the current value, the server shall return this element with only the "version" and "updateSequence" attributes. Otherwise, all optional elements shall be included or not depending on the actual value of the Contents parameter in the GetCapabilities operation request. This base type shall be extended by each specific OWS to include the additional contents needed. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CapabilitiesBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OperationsMetadata uses Python identifier OperationsMetadata
    __OperationsMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), 'OperationsMetadata', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1OperationsMetadata', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 25, 1), )

    
    OperationsMetadata = property(__OperationsMetadata.value, __OperationsMetadata.set, None, 'Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceIdentification uses Python identifier ServiceIdentification
    __ServiceIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), 'ServiceIdentification', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1ServiceIdentification', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 23, 1), )

    
    ServiceIdentification = property(__ServiceIdentification.value, __ServiceIdentification.set, None, 'General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceProvider uses Python identifier ServiceProvider
    __ServiceProvider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), 'ServiceProvider', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1ServiceProvider', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 24, 1), )

    
    ServiceProvider = property(__ServiceProvider.value, __ServiceProvider.set, None, 'Metadata about the organization that provides this specific service instance or server. ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_version', _module_typeBindings.VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 34, 2)
    __version._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 34, 2)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 35, 2)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 35, 2)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, 'Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. When not supported by server, server shall not return this attribute. ')

    _ElementMap.update({
        __OperationsMetadata.name() : __OperationsMetadata,
        __ServiceIdentification.name() : __ServiceIdentification,
        __ServiceProvider.name() : __ServiceProvider
    })
    _AttributeMap.update({
        __version.name() : __version,
        __updateSequence.name() : __updateSequence
    })
_module_typeBindings.CapabilitiesBaseType = CapabilitiesBaseType
Namespace.addCategoryObject('typeBinding', 'CapabilitiesBaseType', CapabilitiesBaseType)


# Complex type {http://www.opengis.net/ows/1.1}GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """XML encoded GetCapabilities operation request. This operation allows clients to retrieve service metadata about a specific service instance. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. This base type shall be extended by each specific OWS to include the additional required "service" attribute, with the correct value for that OWS. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 44, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1AcceptVersions', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 49, 3), )

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, 'When omitted, server shall return latest supported version. ')

    
    # Element {http://www.opengis.net/ows/1.1}Sections uses Python identifier Sections
    __Sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sections'), 'Sections', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1Sections', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 54, 3), )

    
    Sections = property(__Sections.value, __Sections.set, None, 'When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. ')

    
    # Element {http://www.opengis.net/ows/1.1}AcceptFormats uses Python identifier AcceptFormats
    __AcceptFormats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), 'AcceptFormats', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1AcceptFormats', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 59, 3), )

    
    AcceptFormats = property(__AcceptFormats.value, __AcceptFormats.set, None, 'When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". ')

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateSequence'), 'updateSequence', '__httpwww_opengis_netows1_1_GetCapabilitiesType_updateSequence', _module_typeBindings.UpdateSequenceType)
    __updateSequence._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 65, 2)
    __updateSequence._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 65, 2)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, 'When omitted or not supported by server, server shall return latest complete service metadata document. ')

    _ElementMap.update({
        __AcceptVersions.name() : __AcceptVersions,
        __Sections.name() : __Sections,
        __AcceptFormats.name() : __AcceptFormats
    })
    _AttributeMap.update({
        __updateSequence.name() : __updateSequence
    })
_module_typeBindings.GetCapabilitiesType = GetCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'GetCapabilitiesType', GetCapabilitiesType)


# Complex type {http://www.opengis.net/ows/1.1}GetResourceByIdType with content type ELEMENT_ONLY
class GetResourceByIdType (pyxb.binding.basis.complexTypeDefinition):
    """Request to a service to perform the GetResourceByID operation. This operation allows a client to retrieve one or more identified resources, including datasets and resources that describe datasets or parameters. In this XML encoding, no "request" parameter is included, since the element name specifies the specific operation. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetResourceByIdType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 32, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_GetResourceByIdType_httpwww_opengis_netows1_1OutputFormat', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 93, 1), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, 'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')

    
    # Element {http://www.opengis.net/ows/1.1}ResourceID uses Python identifier ResourceID
    __ResourceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResourceID'), 'ResourceID', '__httpwww_opengis_netows1_1_GetResourceByIdType_httpwww_opengis_netows1_1ResourceID', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 37, 3), )

    
    ResourceID = property(__ResourceID.value, __ResourceID.set, None, 'Unordered list of zero or more resource identifiers. These identifiers can be listed in the Contents section of the service metadata (Capabilities) document. For more information on this parameter, see Subclause 9.4.2.1 of the OWS Common specification. ')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_opengis_netows1_1_GetResourceByIdType_service', _module_typeBindings.ServiceType, required=True)
    __service._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 48, 2)
    __service._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 48, 2)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_opengis_netows1_1_GetResourceByIdType_version', _module_typeBindings.VersionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 49, 2)
    __version._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 49, 2)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __OutputFormat.name() : __OutputFormat,
        __ResourceID.name() : __ResourceID
    })
    _AttributeMap.update({
        __service.name() : __service,
        __version.name() : __version
    })
_module_typeBindings.GetResourceByIdType = GetResourceByIdType
Namespace.addCategoryObject('typeBinding', 'GetResourceByIdType', GetResourceByIdType)


# Complex type {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType with content type EMPTY
class AbstractReferenceBaseType (pyxb.binding.basis.complexTypeDefinition):
    """ Base for a reference to a remote or local resource. This type contains only a restricted and annotated set of the attributes from the xlink:simpleAttrs attributeGroup. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 26, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/ows/1.1}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_opengis_netows1_1type', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 31, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 31, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkhref', _ImportedBinding_cwt_wps_xlink.hrefType, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 32, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkrole', _ImportedBinding_cwt_wps_xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 37, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_cwt_wps_xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 42, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinktitle', _ImportedBinding_cwt_wps_xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 47, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkshow', _ImportedBinding_cwt_wps_xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 52, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_cwt_wps_xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 57, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
_module_typeBindings.AbstractReferenceBaseType = AbstractReferenceBaseType
Namespace.addCategoryObject('typeBinding', 'AbstractReferenceBaseType', AbstractReferenceBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (DescriptionType):
    """General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 27, 2)
    _ElementMap = DescriptionType._ElementMap.copy()
    _AttributeMap = DescriptionType._AttributeMap.copy()
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}AccessConstraints uses Python identifier AccessConstraints
    __AccessConstraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), 'AccessConstraints', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1AccessConstraints', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 110, 1), )

    
    AccessConstraints = property(__AccessConstraints.value, __AccessConstraints.set, None, 'Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ')

    
    # Element {http://www.opengis.net/ows/1.1}Fees uses Python identifier Fees
    __Fees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fees'), 'Fees', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1Fees', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 116, 1), )

    
    Fees = property(__Fees.value, __Fees.set, None, 'Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceType uses Python identifier ServiceType
    __ServiceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), 'ServiceType', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1ServiceType', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 31, 6), )

    
    ServiceType = property(__ServiceType.value, __ServiceType.set, None, 'A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceTypeVersion uses Python identifier ServiceTypeVersion
    __ServiceTypeVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), 'ServiceTypeVersion', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1ServiceTypeVersion', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 36, 6), )

    
    ServiceTypeVersion = property(__ServiceTypeVersion.value, __ServiceTypeVersion.set, None, 'Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. ')

    
    # Element {http://www.opengis.net/ows/1.1}Profile uses Python identifier Profile
    __Profile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Profile'), 'Profile', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1Profile', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 41, 6), )

    
    Profile = property(__Profile.value, __Profile.set, None, 'Unordered list of identifiers of Application Profiles that are implemented by this server. This element should be included for each specified application profile implemented by this server. The identifier value should be specified by each Application Profile. If this element is omitted, no meaning is implied. ')

    _ElementMap.update({
        __AccessConstraints.name() : __AccessConstraints,
        __Fees.name() : __Fees,
        __ServiceType.name() : __ServiceType,
        __ServiceTypeVersion.name() : __ServiceTypeVersion,
        __Profile.name() : __Profile
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type {http://www.opengis.net/ows/1.1}IdentificationType with content type ELEMENT_ONLY
class IdentificationType (BasicIdentificationType):
    """Extended metadata identifying and describing a set of data. This type shall be extended if needed for each specific OWS to include additional metadata for each type of dataset. If needed, this type should first be restricted for each specific OWS to change the multiplicity (or optionality) of some elements. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 60, 1)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1BoundingBox', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 70, 1), )

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1OutputFormat', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 93, 1), )

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, 'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')

    
    # Element {http://www.opengis.net/ows/1.1}AvailableCRS uses Python identifier AvailableCRS
    __AvailableCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), 'AvailableCRS', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1AvailableCRS', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 99, 1), )

    
    AvailableCRS = property(__AvailableCRS.value, __AvailableCRS.set, None, None)

    _ElementMap.update({
        __BoundingBox.name() : __BoundingBox,
        __OutputFormat.name() : __OutputFormat,
        __AvailableCRS.name() : __AvailableCRS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentificationType = IdentificationType
Namespace.addCategoryObject('typeBinding', 'IdentificationType', IdentificationType)


# Complex type {http://www.opengis.net/ows/1.1}ReferenceType with content type ELEMENT_ONLY
class ReferenceType (AbstractReferenceBaseType):
    """Complete reference to a remote or local resource, allowing including metadata about that resource. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 66, 1)
    _ElementMap = AbstractReferenceBaseType._ElementMap.copy()
    _AttributeMap = AbstractReferenceBaseType._AttributeMap.copy()
    # Base type is AbstractReferenceBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), 'Abstract', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Abstract', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1), )

    
    Abstract = property(__Abstract.value, __Abstract.set, None, 'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Metadata', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Identifier', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, 'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/ows/1.1}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Format'), 'Format', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Format', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5), )

    
    Format = property(__Format.value, __Format.set, None, 'The format of the referenced resource. This element is omitted when the mime type is indicated in the http header of the reference. ')

    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    _ElementMap.update({
        __Abstract.name() : __Abstract,
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier,
        __Format.name() : __Format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceType = ReferenceType
Namespace.addCategoryObject('typeBinding', 'ReferenceType', ReferenceType)


# Complex type {http://www.opengis.net/ows/1.1}ReferenceGroupType with content type ELEMENT_ONLY
class ReferenceGroupType (BasicIdentificationType):
    """Logical group of one or more references to remote and/or local resources, allowing including metadata about that group. A Group can be used instead of a Manifest that can only contain one group. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroupType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 97, 1)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}AbstractReferenceBase uses Python identifier AbstractReferenceBase
    __AbstractReferenceBase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), 'AbstractReferenceBase', '__httpwww_opengis_netows1_1_ReferenceGroupType_httpwww_opengis_netows1_1AbstractReferenceBase', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 24, 1), )

    
    AbstractReferenceBase = property(__AbstractReferenceBase.value, __AbstractReferenceBase.set, None, None)

    _ElementMap.update({
        __AbstractReferenceBase.name() : __AbstractReferenceBase
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceGroupType = ReferenceGroupType
Namespace.addCategoryObject('typeBinding', 'ReferenceGroupType', ReferenceGroupType)


# Complex type {http://www.opengis.net/ows/1.1}ManifestType with content type ELEMENT_ONLY
class ManifestType (BasicIdentificationType):
    """Unordered list of one or more groups of references to remote and/or local resources. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManifestType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 112, 1)
    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    # Base type is BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}ReferenceGroup uses Python identifier ReferenceGroup
    __ReferenceGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), 'ReferenceGroup', '__httpwww_opengis_netows1_1_ManifestType_httpwww_opengis_netows1_1ReferenceGroup', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 95, 1), )

    
    ReferenceGroup = property(__ReferenceGroup.value, __ReferenceGroup.set, None, None)

    _ElementMap.update({
        __ReferenceGroup.name() : __ReferenceGroup
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ManifestType = ManifestType
Namespace.addCategoryObject('typeBinding', 'ManifestType', ManifestType)


# Complex type {http://www.opengis.net/ows/1.1}RequestMethodType with content type ELEMENT_ONLY
class RequestMethodType (OnlineResourceType):
    """Connect point URL and any constraints for this HTTP request method for this operation request. In the OnlineResourceType, the xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to contain this URL. The other attributes in the xlink:simpleAttrs attribute group should not be used. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestMethodType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 124, 1)
    _ElementMap = OnlineResourceType._ElementMap.copy()
    _AttributeMap = OnlineResourceType._AttributeMap.copy()
    # Base type is OnlineResourceType
    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_RequestMethodType_httpwww_opengis_netows1_1Constraint', True, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 131, 5), )

    
    Constraint = property(__Constraint.value, __Constraint.set, None, 'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RequestMethodType = RequestMethodType
Namespace.addCategoryObject('typeBinding', 'RequestMethodType', RequestMethodType)


# Complex type {http://www.opengis.net/ows/1.1}ServiceReferenceType with content type ELEMENT_ONLY
class ServiceReferenceType (ReferenceType):
    """Complete reference to a remote resource that needs to be retrieved from an OWS using an XML-encoded operation request. This element shall be used, within an InputData or Manifest element that is used for input data, when that input data needs to be retrieved from another web service using a XML-encoded OWS operation request. This element shall not be used for local payload input data or for requesting the resource from a web server using HTTP Get. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 38, 1)
    _ElementMap = ReferenceType._ElementMap.copy()
    _AttributeMap = ReferenceType._AttributeMap.copy()
    # Base type is ReferenceType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element {http://www.opengis.net/ows/1.1}RequestMessage uses Python identifier RequestMessage
    __RequestMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage'), 'RequestMessage', '__httpwww_opengis_netows1_1_ServiceReferenceType_httpwww_opengis_netows1_1RequestMessage', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 45, 5), )

    
    RequestMessage = property(__RequestMessage.value, __RequestMessage.set, None, 'The XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. ')

    
    # Element {http://www.opengis.net/ows/1.1}RequestMessageReference uses Python identifier RequestMessageReference
    __RequestMessageReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference'), 'RequestMessageReference', '__httpwww_opengis_netows1_1_ServiceReferenceType_httpwww_opengis_netows1_1RequestMessageReference', False, pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 50, 5), )

    
    RequestMessageReference = property(__RequestMessageReference.value, __RequestMessageReference.set, None, 'Reference to the XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. The referenced message shall be attached to the same message (using the cid scheme), or be accessible using a URL. ')

    
    # Element Format ({http://www.opengis.net/ows/1.1}Format) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    _ElementMap.update({
        __RequestMessage.name() : __RequestMessage,
        __RequestMessageReference.name() : __RequestMessageReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceReferenceType = ServiceReferenceType
Namespace.addCategoryObject('typeBinding', 'ServiceReferenceType', ServiceReferenceType)


IndividualName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 108, 1))
Namespace.addCategoryObject('elementBinding', IndividualName.name().localName(), IndividualName)

OrganisationName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, documentation='Name of the responsible organization. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', OrganisationName.name().localName(), OrganisationName)

PositionName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 120, 1))
Namespace.addCategoryObject('elementBinding', PositionName.name().localName(), PositionName)

AbstractMetaData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation='Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 63, 1))
Namespace.addCategoryObject('elementBinding', AbstractMetaData.name().localName(), AbstractMetaData)

AvailableCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 99, 1))
Namespace.addCategoryObject('elementBinding', AvailableCRS.name().localName(), AvailableCRS)

SupportedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedCRS'), pyxb.binding.datatypes.anyURI, documentation='Coordinate reference system in which data from this data(set) or resource is available or supported. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 100, 1))
Namespace.addCategoryObject('elementBinding', SupportedCRS.name().localName(), SupportedCRS)

AccessConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, documentation='Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 110, 1))
Namespace.addCategoryObject('elementBinding', AccessConstraints.name().localName(), AccessConstraints)

Fees = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, documentation='Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 116, 1))
Namespace.addCategoryObject('elementBinding', Fees.name().localName(), Fees)

Language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Language'), pyxb.binding.datatypes.language, documentation='Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 122, 1))
Namespace.addCategoryObject('elementBinding', Language.name().localName(), Language)

Resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Resource'), pyxb.binding.datatypes.anyType, documentation='XML encoded GetResourceByID operation response. The complexType used by this element shall be specified by each specific OWS.  ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', Resource.name().localName(), Resource)

ExtendedCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, documentation='Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', ExtendedCapabilities.name().localName(), ExtendedCapabilities)

Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), LanguageStringType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

Abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', Abstract.name().localName(), Abstract)

Keywords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', Keywords.name().localName(), Keywords)

PointOfContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointOfContact'), ResponsiblePartyType, documentation='Identification of, and means of communication with, person(s) responsible for the resource(s). For OWS use in the ServiceProvider section of a service metadata document, the optional organizationName element was removed, since this type is always used with the ProviderName element which provides that information. The optional individualName element was made mandatory, since either the organizationName or individualName element is mandatory. The mandatory "role" element was changed to optional, since no clear use of this information is known in the ServiceProvider section. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', PointOfContact.name().localName(), PointOfContact)

Role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', Role.name().localName(), Role)

ContactInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 132, 1))
Namespace.addCategoryObject('elementBinding', ContactInfo.name().localName(), ContactInfo)

BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', BoundingBox.name().localName(), BoundingBox)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

OutputFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, documentation='Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', OutputFormat.name().localName(), OutputFormat)

AnyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), CTD_ANON, documentation='Specifies that any value is allowed for this parameter.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', AnyValue.name().localName(), AnyValue)

NoValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), CTD_ANON_, documentation='Specifies that no values are allowed for this parameter or quantity.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', NoValues.name().localName(), NoValues)

ValuesReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), CTD_ANON_2, documentation='Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 100, 1))
Namespace.addCategoryObject('elementBinding', ValuesReference.name().localName(), ValuesReference)

AllowedValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), CTD_ANON_3, documentation='List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', AllowedValues.name().localName(), AllowedValues)

Value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), ValueType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 148, 1))
Namespace.addCategoryObject('elementBinding', Value.name().localName(), Value)

DefaultValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), ValueType, documentation='The default value for a quantity for which multiple values are allowed. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 159, 1))
Namespace.addCategoryObject('elementBinding', DefaultValue.name().localName(), DefaultValue)

MinimumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), ValueType, documentation='Minimum value of this numeric parameter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 187, 1))
Namespace.addCategoryObject('elementBinding', MinimumValue.name().localName(), MinimumValue)

MaximumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), ValueType, documentation='Maximum value of this numeric parameter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 193, 1))
Namespace.addCategoryObject('elementBinding', MaximumValue.name().localName(), MaximumValue)

Spacing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), ValueType, documentation='The regular distance or spacing between the allowed values in a range. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 199, 1))
Namespace.addCategoryObject('elementBinding', Spacing.name().localName(), Spacing)

Meaning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), DomainMetadataType, documentation='Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 256, 1))
Namespace.addCategoryObject('elementBinding', Meaning.name().localName(), Meaning)

DataType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataType'), DomainMetadataType, documentation='Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 262, 1))
Namespace.addCategoryObject('elementBinding', DataType.name().localName(), DataType)

ReferenceSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), DomainMetadataType, documentation='Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 268, 1))
Namespace.addCategoryObject('elementBinding', ReferenceSystem.name().localName(), ReferenceSystem)

UOM = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UOM'), DomainMetadataType, documentation='Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1))
Namespace.addCategoryObject('elementBinding', UOM.name().localName(), UOM)

Exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', Exception.name().localName(), Exception)

OperationsMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_4, documentation='Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', OperationsMetadata.name().localName(), OperationsMetadata)

Operation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_5, documentation='Metadata for one operation that this server implements. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 57, 1))
Namespace.addCategoryObject('elementBinding', Operation.name().localName(), Operation)

DCP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_6, documentation='Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', DCP.name().localName(), DCP)

HTTP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_7, documentation='Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 104, 1))
Namespace.addCategoryObject('elementBinding', HTTP.name().localName(), HTTP)

ServiceProvider = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_8, documentation='Metadata about the organization that provides this specific service instance or server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', ServiceProvider.name().localName(), ServiceProvider)

Metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', Metadata.name().localName(), Metadata)

WGS84BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), WGS84BoundingBoxType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 113, 1))
Namespace.addCategoryObject('elementBinding', WGS84BoundingBox.name().localName(), WGS84BoundingBox)

OtherSource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), MetadataType, documentation='Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', OtherSource.name().localName(), OtherSource)

DatasetDescriptionSummary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', DatasetDescriptionSummary.name().localName(), DatasetDescriptionSummary)

Range = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Range'), RangeType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 165, 1))
Namespace.addCategoryObject('elementBinding', Range.name().localName(), Range)

ExceptionReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionReport'), CTD_ANON_9, documentation='Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', ExceptionReport.name().localName(), ExceptionReport)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCapabilities'), GetCapabilitiesType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

GetResourceByID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetResourceByID'), GetResourceByIdType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', GetResourceByID.name().localName(), GetResourceByID)

AbstractReferenceBase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', AbstractReferenceBase.name().localName(), AbstractReferenceBase)

ServiceIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_10, documentation='General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', ServiceIdentification.name().localName(), ServiceIdentification)

OperationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationResponse'), ManifestType, documentation='Response from an OWS operation, allowing including multiple output data items with each item either included or referenced. This OperationResponse element, or an element using the ManifestType with a more specific element name, shall be used whenever applicable for responses from OWS operations. This element is specified for use where the ManifestType contents are needed for an operation response, but the Manifest element name is not fully applicable. This element or the ManifestType shall be used instead of using the ows:ReferenceType proposed in OGC 04-105. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', OperationResponse.name().localName(), OperationResponse)

InputData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InputData'), ManifestType, documentation='Input data in a XML-encoded OWS operation request, allowing including multiple data items with each data item either included or referenced. This InputData element, or an element using the ManifestType with a more-specific element name (TBR), shall be used whenever applicable within XML-encoded OWS operation requests. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', InputData.name().localName(), InputData)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), ReferenceType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 64, 1))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

ReferenceGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), ReferenceGroupType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 95, 1))
Namespace.addCategoryObject('elementBinding', ReferenceGroup.name().localName(), ReferenceGroup)

Manifest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Manifest'), ManifestType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 110, 1))
Namespace.addCategoryObject('elementBinding', Manifest.name().localName(), Manifest)

ServiceReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceReference'), ServiceReferenceType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', ServiceReference.name().localName(), ServiceReference)



KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keyword'), LanguageStringType, scope=KeywordsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 57, 3)))

KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), CodeType, scope=KeywordsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 58, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 58, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keyword')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 58, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
KeywordsType._Automaton = _BuildAutomaton()




ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 108, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Name of the responsible organization. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 114, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 120, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartyType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 126, 1)))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartyType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 132, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 87, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 88, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 89, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrganisationName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 87, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 88, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 89, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 90, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponsiblePartyType._Automaton = _BuildAutomaton_()




ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Name of the responsible person: surname, given name, title separated by a delimiter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 108, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation='Role or position of the responsible person. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 120, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Role'), CodeType, scope=ResponsiblePartySubsetType, documentation='Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 126, 1)))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo'), ContactType, scope=ResponsiblePartySubsetType, documentation='Address of the responsible party. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 132, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 101, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 102, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 103, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 104, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 101, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PositionName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 102, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInfo')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 103, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Role')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 104, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ResponsiblePartySubsetType._Automaton = _BuildAutomaton_2()




ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Phone'), TelephoneType, scope=ContactType, documentation='Telephone numbers at which the organization or individual may be contacted. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 144, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), AddressType, scope=ContactType, documentation='Physical and email address at which the organization or individual may be contacted. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 149, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource'), OnlineResourceType, scope=ContactType, documentation='On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleAttrs attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleAttrs attribute group should not be used. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 154, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Time period (including time zone) when individuals can contact the organization or individual. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 159, 3)))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions'), pyxb.binding.datatypes.string, scope=ContactType, documentation='Supplemental instructions on how or when to contact the individual or organization. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 164, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 144, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 149, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 154, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 159, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 164, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Phone')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 144, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 149, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OnlineResource')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 154, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HoursOfService')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 159, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContactInstructions')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 164, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ContactType._Automaton = _BuildAutomaton_3()




TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Voice'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number by which individuals can speak to the responsible organization or individual. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 185, 3)))

TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Facsimile'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation='Telephone number of a facsimile machine for the responsible\norganization or individual. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 190, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 185, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 190, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Voice')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Facsimile')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 190, 3))
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
TelephoneType._Automaton = _BuildAutomaton_4()




AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address line for the location. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 204, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'City'), pyxb.binding.datatypes.string, scope=AddressType, documentation='City of the location. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 209, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), pyxb.binding.datatypes.string, scope=AddressType, documentation='State or province of the location. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 214, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), pyxb.binding.datatypes.string, scope=AddressType, documentation='ZIP or other postal code. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 219, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Country of the physical address. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 224, 3)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress'), pyxb.binding.datatypes.string, scope=AddressType, documentation='Address of the electronic mailbox of the responsible organization or individual. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 229, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 204, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 209, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 214, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 219, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 224, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 229, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DeliveryPoint')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 204, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'City')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 209, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 214, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 219, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 224, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElectronicMailAddress')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 229, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AddressType._Automaton = _BuildAutomaton_5()




BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 78, 3)))

BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), PositionType, scope=BoundingBoxType, documentation='Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 83, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 78, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 83, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoundingBoxType._Automaton = _BuildAutomaton_6()




ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherSource'), MetadataType, scope=ContentsBaseType, documentation='Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 42, 1)))

ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=ContentsBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 48, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 29, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 34, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 29, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherSource')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 34, 3))
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
ContentsBaseType._Automaton = _BuildAutomaton_7()




DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), LanguageStringType, scope=DescriptionType, documentation='Title of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 36, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, scope=DescriptionType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1)))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keywords'), KeywordsType, scope=DescriptionType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 48, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptionType._Automaton = _BuildAutomaton_8()




UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=UnNamedDomainType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyValue'), CTD_ANON, scope=UnNamedDomainType, documentation='Specifies that any value is allowed for this parameter.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 86, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoValues'), CTD_ANON_, scope=UnNamedDomainType, documentation='Specifies that no values are allowed for this parameter or quantity.', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 93, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference'), CTD_ANON_2, scope=UnNamedDomainType, documentation='Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 100, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues'), CTD_ANON_3, scope=UnNamedDomainType, documentation='List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 136, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue'), ValueType, scope=UnNamedDomainType, documentation='The default value for a quantity for which multiple values are allowed. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 159, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meaning'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 256, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataType'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 262, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 268, 1)))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UOM'), DomainMetadataType, scope=UnNamedDomainType, documentation='Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 274, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 46, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 51, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 56, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 61, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 66, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 79, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 80, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoValues')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 81, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 82, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 46, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meaning')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 51, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataType')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 56, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UOM')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 122, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 127, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 66, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnNamedDomainType._Automaton = _BuildAutomaton_9()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), ValueType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 148, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Range'), RangeType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 165, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 142, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Range')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 143, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_10()




ExceptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText'), pyxb.binding.datatypes.string, scope=ExceptionType, documentation='Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 60, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 60, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExceptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExceptionText')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 60, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExceptionType._Automaton = _BuildAutomaton_11()




AcceptVersionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Version'), VersionType, scope=AcceptVersionsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 85, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AcceptVersionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Version')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 85, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AcceptVersionsType._Automaton = _BuildAutomaton_12()




SectionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), pyxb.binding.datatypes.string, scope=SectionsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 94, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 94, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SectionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Section')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 94, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SectionsType._Automaton = _BuildAutomaton_13()




AcceptFormatsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=AcceptFormatsType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 110, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 110, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AcceptFormatsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 110, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AcceptFormatsType._Automaton = _BuildAutomaton_14()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_4, documentation='Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 36, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_4, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 41, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_4, documentation='Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 51, 1)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Operation'), CTD_ANON_5, scope=CTD_ANON_4, documentation='Metadata for one operation that this server implements. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 57, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 31, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 36, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 41, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 46, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Operation')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 31, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 36, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 41, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtendedCapabilities')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 46, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_15()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), DomainType, scope=CTD_ANON_5, documentation='Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 68, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=CTD_ANON_5, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 73, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DCP'), CTD_ANON_6, scope=CTD_ANON_5, documentation='Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 92, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 68, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 73, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 78, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DCP')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 63, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 68, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 73, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 78, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_16()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HTTP'), CTD_ANON_7, scope=CTD_ANON_6, documentation='Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 104, 1)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HTTP')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 99, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_17()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Get'), RequestMethodType, scope=CTD_ANON_7, documentation='Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 110, 4)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Post'), RequestMethodType, scope=CTD_ANON_7, documentation='Connect point URL and any constraints for the HTTP "Post" request method for this operation request. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 115, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Get')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 110, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Post')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 115, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_18()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderName'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, documentation='A unique identifier for the service provider organization. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 30, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite'), OnlineResourceType, scope=CTD_ANON_8, documentation='Reference to the most relevant web site of the service provider. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 35, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact'), ResponsiblePartySubsetType, scope=CTD_ANON_8, documentation='Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 40, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 35, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderName')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 30, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProviderSite')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 35, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceContact')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 40, 4))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_19()




MetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=MetadataType, documentation='Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 63, 1)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 49, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractMetaData')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MetadataType._Automaton = _BuildAutomaton_20()




WGS84BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner'), PositionType2D, scope=WGS84BoundingBoxType, documentation='Position of the bounding box corner at which the values of longitude and latitude normally are the algebraic minimums within this bounding box. For more information, see Subclauses 10.4.5 and C.13. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 123, 5)))

WGS84BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner'), PositionType2D, scope=WGS84BoundingBoxType, documentation='Position of the bounding box corner at which the values of longitude and latitude normally are the algebraic minimums within this bounding box. For more information, see Subclauses 10.4.5 and C.13. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 128, 5)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerCorner')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 123, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperCorner')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 128, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WGS84BoundingBoxType._Automaton = _BuildAutomaton_21()




DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 70, 1)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox'), WGS84BoundingBoxType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 113, 1)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=DatasetDescriptionSummaryBaseType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 48, 1)))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=DatasetDescriptionSummaryBaseType, documentation='Unambiguous identifier or name of this coverage, unique for this server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 62, 5)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 57, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 67, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 72, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 77, 5))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WGS84BoundingBox')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 57, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 62, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 67, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 72, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DatasetDescriptionSummary')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsContents.xsd', 77, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatasetDescriptionSummaryBaseType._Automaton = _BuildAutomaton_22()




BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=BasicIdentificationType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=BasicIdentificationType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BasicIdentificationType._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 46, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 51, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 56, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 61, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 66, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllowedValues')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 79, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 80, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoValues')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 81, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuesReference')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 82, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 46, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meaning')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 51, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataType')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 56, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UOM')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 122, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSystem')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 127, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 66, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DomainType._Automaton = _BuildAutomaton_24()




RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue'), ValueType, scope=RangeType, documentation='Minimum value of this numeric parameter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 187, 1)))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue'), ValueType, scope=RangeType, documentation='Maximum value of this numeric parameter. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 193, 1)))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spacing'), ValueType, scope=RangeType, documentation='The regular distance or spacing between the allowed values in a range. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 199, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 172, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 173, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 174, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinimumValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 172, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaximumValue')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 173, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spacing')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDomainType.xsd', 174, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RangeType._Automaton = _BuildAutomaton_25()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), ExceptionType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 53, 1)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Exception')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd', 29, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_26()




CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata'), CTD_ANON_4, scope=CapabilitiesBaseType, documentation='Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 25, 1)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification'), CTD_ANON_10, scope=CapabilitiesBaseType, documentation='General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 23, 1)))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider'), CTD_ANON_8, scope=CapabilitiesBaseType, documentation='Metadata about the organization that provides this specific service instance or server. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceProvider.xsd', 24, 1)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceIdentification')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceProvider')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OperationsMetadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 32, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CapabilitiesBaseType._Automaton = _BuildAutomaton_27()




GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions'), AcceptVersionsType, scope=GetCapabilitiesType, documentation='When omitted, server shall return latest supported version. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 49, 3)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sections'), SectionsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 54, 3)))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats'), AcceptFormatsType, scope=GetCapabilitiesType, documentation='When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 59, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 49, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 54, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 59, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptVersions')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sections')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 54, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AcceptFormats')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetCapabilities.xsd', 59, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GetCapabilitiesType._Automaton = _BuildAutomaton_28()




GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=GetResourceByIdType, documentation='Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 93, 1)))

GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResourceID'), pyxb.binding.datatypes.anyURI, scope=GetResourceByIdType, documentation='Unordered list of zero or more resource identifiers. These identifiers can be listed in the Contents section of the service metadata (Capabilities) document. For more information on this parameter, see Subclause 9.4.2.1 of the OWS Common specification. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 37, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 37, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 42, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResourceID')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 37, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsGetResourceByID.xsd', 42, 3))
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
GetResourceByIdType._Automaton = _BuildAutomaton_29()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 110, 1)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fees'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 116, 1)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceType'), CodeType, scope=CTD_ANON_10, documentation='A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 31, 6)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion'), VersionType, scope=CTD_ANON_10, documentation='Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 36, 6)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Profile'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_10, documentation='Unordered list of identifiers of Application Profiles that are implemented by this server. This element should be included for each specified application profile implemented by this server. The identifier value should be specified by each Application Profile. If this element is omitted, no meaning is implied. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 41, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 41, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 46, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 51, 6))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceType')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 31, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceTypeVersion')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 36, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Profile')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 41, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fees')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 46, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AccessConstraints')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsServiceIdentification.xsd', 51, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_30()




IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox'), BoundingBoxType, scope=IdentificationType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 70, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat'), MimeType, scope=IdentificationType, documentation='Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 93, 1)))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS'), pyxb.binding.datatypes.anyURI, scope=IdentificationType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 99, 1)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 67, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 72, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 77, 5))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundingBox')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 67, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputFormat')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 72, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvailableCRS')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 77, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentificationType._Automaton = _BuildAutomaton_31()




ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Abstract'), LanguageStringType, scope=ReferenceType, documentation='Brief narrative description of this resource, normally used for display to a human. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/ows19115subset.xsd', 42, 1)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), MetadataType, scope=ReferenceType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsCommon.xsd', 42, 1)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CodeType, scope=ReferenceType, documentation='Unique identifier or name of this dataset. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 87, 1)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Format'), MimeType, scope=ReferenceType, documentation='The format of the referenced resource. This element is omitted when the mime type is indicated in the http header of the reference. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 73, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 78, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 84, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 73, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 78, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Format')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 84, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReferenceType._Automaton = _BuildAutomaton_32()




ReferenceGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1), scope=ReferenceGroupType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 24, 1)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AbstractReferenceBase')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 104, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceGroupType._Automaton = _BuildAutomaton_33()




ManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup'), ReferenceGroupType, scope=ManifestType, location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 95, 1)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 32, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keywords')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 45, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsDataIdentification.xsd', 50, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceGroup')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 119, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ManifestType._Automaton = _BuildAutomaton_34()




RequestMethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Constraint'), DomainType, scope=RequestMethodType, documentation='Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 131, 5)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 131, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RequestMethodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Constraint')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsOperationsMetadata.xsd', 131, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestMethodType._Automaton = _BuildAutomaton_35()




ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage'), pyxb.binding.datatypes.anyType, scope=ServiceReferenceType, documentation='The XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 45, 5)))

ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference'), pyxb.binding.datatypes.anyURI, scope=ServiceReferenceType, documentation='Reference to the XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. The referenced message shall be attached to the same message (using the cid scheme), or be accessible using a URL. ', location=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 50, 5)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 73, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 78, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 84, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 73, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Abstract')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 78, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Format')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 79, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsManifest.xsd', 84, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestMessage')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 45, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestMessageReference')), pyxb.utils.utility.Location('http://schemas.opengis.net/ows/1.1.0/owsInputOutputData.xsd', 50, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceReferenceType._Automaton = _BuildAutomaton_36()


SupportedCRS._setSubstitutionGroup(AvailableCRS)

WGS84BoundingBox._setSubstitutionGroup(BoundingBox)

Reference._setSubstitutionGroup(AbstractReferenceBase)

ServiceReference._setSubstitutionGroup(Reference)
