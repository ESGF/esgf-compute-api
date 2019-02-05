# Compute First four EOFs of ts from MERRA2
import cwt, os
plotter = cwt.initialize()
host = os.environ.get( "EDAS_HOST_ADDRESS")
assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
print "Connecting to wps host: " + host
wps = cwt.WPS( host, log=True,log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start' :-80, 'end' :80 ,'crs' :'values'}, 'time': { 'start' :'1880-01-01T00', 'end' :'2012-01-01T00', 'crs' :'timestamps'}  } )
v0 = cwt.Variable("collection://cip_20crv2c_mth", "ts", domain=d0  )

decycle = cwt.Process.from_dict({'name': "xarray.decycle", "axis": "t", "norm": "true" } )
decycle.set_inputs( v0 )

detrend = cwt.Process.from_dict({'name': "xarray.detrend", "axis": "t", "wsize": "50" })
detrend.set_inputs( decycle )

eofs =  cwt.Process.from_dict( { 'name': "xarray.eof", "modes" :"4" } )
eofs.set_inputs( detrend )

wps.execute( eofs, domains=[d0], async=True )
dataPaths = wps.download_result(eofs)
for dataPath in dataPaths:
    plotter.mpl_plot( dataPath, 0, True )

    # domains = [{"name": "d0", "lat": {"start": -80, "end": 80, "system": "values"},
    #             "time": {"start": '1880-01-01T00', "end": '2012-01-01T00', "system": "values"}}]
    # variables = [{"uri": self.mgr.getAddress("20crv", "ts"), "name": "ts:v0", "domain": "d0"}]
    # operations = [{"name": "xarray.decycle", "axis": "t", "input": "v0", "norm": "true", "result": "dc"},
    #               {"name": "xarray.detrend", "axis": "t", "input": "dc", "wsize": 50, "result": "dt"},
    #               {"name": "xarray.eof", "modes": 4, "input": "dt"}]
    # results = self.mgr.testExec(domains, variables, operations)