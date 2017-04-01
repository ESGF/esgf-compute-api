import esgf, os

lat = esgf.Dimension.from_single_value(45, name='lat')
lon = esgf.Dimension.from_single_value(30, name='lon')

domain0 = esgf.Domain([], name='d0')
domain1 = esgf.Domain([lat, lon], name='d1')

variable = esgf.Variable('collection:/collection:/GISS_r1i1p1', 'tas', name='v0', domains=[domain0])
wps = esgf.WPS('http://localhost:9001/wps', log=True, log_file=os.path.expanduser("~/esgf_api.log"))
wps.init()

process = wps.get_process('CDSpark.max')

process.execute([variable], domain0, [esgf.NamedParameter("axes", "t")], False, False, "GET")

print "Results:"

for output in process._result.processOutputs:
    if output.reference:    print "  >> Reference: " + output.reference

if output.mimeType:     print "  >> MimeType: " + output.mimeType

if output.data:
    print "  >> Data: " + ', '.join(output.data)