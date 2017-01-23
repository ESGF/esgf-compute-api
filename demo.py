#! /usr/bin/env python

import esgf

wps = esgf.WPS('http://localhost:8000/wps', log=True)

variable = esgf.Variable('file:///export/boutte3/data/tas_6h.nc', 'tas')

op = esgf.Operation('CDSpark.max', inputs=[variable], axes=esgf.NamedParameter('axes', 'x', 'y'))

wps.execute_op(op, method='GET')

for output in op.output:
    print output[0]
