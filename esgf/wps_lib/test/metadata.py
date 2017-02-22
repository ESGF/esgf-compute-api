#! /usr/bin/env python

from esgf.wps_lib import metadata

identification = metadata.ServiceIdentification()
identification.service_type = 'WPS'
identification.service_type_version = ['1.0.0', '2.0.0']
identification.title = 'LLNL WPS Service'
identification.keywords = ['test', '1']

provider = metadata.ServiceProvider()
provider.provider_name = 'LLNL'

operation_execute = metadata.Operation()
operation_execute.name = 'Execute'
operation_execute.get = 'http://llnl.gov/wps?'
operation_execute.post = 'http://llnl.gov/wps'

x = metadata.LiteralData()
x.value = metadata.AnyValue()

y = metadata.LiteralData()
y.value = metadata.AnyValue()

z = metadata.LiteralData()
z.value = metadata.AnyValue()

describe_sum = metadata.ProcessDescription()
describe_sum.identifier = 'sum'
describe_sum.title = 'Sum'
describe_sum.process_version = '1.0.0'
describe_sum.input = [x, y]
describe_sum.output = [z]

process_sum = metadata.Process()
process_sum.title = 'Sum'
process_sum.identifier = 'sum'

process_avg = metadata.Process()
process_avg.title = 'Average'
process_avg.identifier = 'avg'

languages = metadata.Languages()
languages.default = 'en-CA'
languages.supported = ['en-CA', 'en-FR']
