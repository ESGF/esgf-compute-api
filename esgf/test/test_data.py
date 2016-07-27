"""
Data for mock testing.
"""

from mock import Mock

IDENTIFICATION = {
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

CONTACT = {
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

PROVIDER = {
    'name': 'llnl.gov',
    'contact': CONTACT,
    'url': 'http://localhost:8000/wps'
}

METADATA = {
    'identification': IDENTIFICATION,
    'provider': PROVIDER
}

def generic_mock(data):
    """ Creates mock class """
    mock = Mock()

    for key, value in data.iteritems():
        setattr(mock, key, value)

    return mock

def generate_identification():
    """ Creates Identification mock """
    return generic_mock(IDENTIFICATION)

def generate_provider():
    """ Creates Provider mock """
    PROVIDER['contact'] = generic_mock(CONTACT)

    return generic_mock(PROVIDER)
