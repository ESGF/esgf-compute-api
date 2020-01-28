""" NamedParameter Unittest. """

import cwt


def test_from_string():
    p = cwt.NamedParameter.from_string('axes', 'x|y')

    assert isinstance(p.values, tuple)
    assert len(p.values) == 2
    assert p.values == ('x', 'y')


def test_values():
    p = cwt.NamedParameter('test', 'data', 3.0, 2, float('inf'))

    output = p.to_dict()

    assert 'test' in output

    value = output['test']

    assert 'data' in value
    assert '3.0' in value
    assert '2' in value
    assert 'inf' in value
