from mock import Mock

_IDENTIFICATION = {
    'title': 'Server Title',
    'abstract': 'Server Abstract',
    'keywords': ['K1', 'K2'],
    'accessconstraints': 'None',
    'fees': '3 Million/Year',
    'type': 'WPS Type',
    'service': 'WPS Server',
    'version': '1.0.0',
    'profiles': ['P1', 'P2']
}

_CONTACT = {
    'name': 'John Bob',
    'organization': 'DOE',
    'site': 'Labs',
    'position': 'Software Developer',
    'phone': '5402055432',
    'fax': '4244232345',
    'address': 'Vasco',
    'city': 'Livermore',
    'region': 'North',
    'postcode': 95926,
    'country': 'United States',
    'email': 'bob200@llnl.gov',
    'url': 'http://llnl.gov',
    'hours': '24-7',
    'instructions': 'Do not crash'
}

_PROVIDER = {
    'name': 'llnl.gov',
    'contact': _CONTACT,
    'url': 'http://localhost:8000/wps'
}

_METADATA = {
    'identification': _IDENTIFICATION,
    'provider': _PROVIDER
}

def generic_mock(data):
    mock = Mock()

    for key, value in data.iteritems():
        setattr(mock, key, value)

    return mock

def generate_identification():
    return generic_mock(_IDENTIFICATION)

def generate_provider():
    _PROVIDER['contact'] = generic_mock(_CONTACT)

    return generic_mock(_PROVIDER)
