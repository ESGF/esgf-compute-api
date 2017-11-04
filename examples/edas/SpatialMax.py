import cwt, os, time, urllib

plotter = cwt.initialize()
host ="https://dptomcat03-int/wps/cwt"

wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

d0 = cwt.Domain([
    cwt.Dimension('latitude', 0, 90),
    cwt.Dimension('longitude', 0, 10),
    cwt.Dimension('time', 0, 1000, cwt.INDICES)
])

inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

op_data = {'name': "CDSpark.max", 'axes': "xy"}
op = cwt.Process.from_dict(op_data)
op.set_inputs(inputs)

wps.execute(op, domains=[d0] )

status = wps.status(op)
print ("STATUS: " + status)
while status == "QUEUED" or status == "EXECUTING":
    time.sleep(1)
    status = wps.status(op)
    print ("STATUS: " + status)
if status == "COMPLETED":
    file_href = op.hrefs.get("file")
    file_path = "/tmp/" + file_href.split('/')[-1]
    urllib.urlretrieve(file_href, file_path)
    print "Result downloaded to: " + file_path