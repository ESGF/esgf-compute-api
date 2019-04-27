import cwt

wps = cwt.WPSClient('http://127.0.0.1:5000/ows_wps/cwt')

wps.get_capabilities()

print( wps.client.operations )

print( wps.client.processes )