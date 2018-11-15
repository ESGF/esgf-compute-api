# Compute First four EOFs of ts from MERRA2
import cwt, os
plotter = cwt.initialize()
host = os.environ.get( "EDAS_HOST_ADDRESS")
assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
print "Connecting to wps host: " + host
wps = cwt.WPS( host, log=True,log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start' :-80, 'end' :80 ,'crs' :'values'}, 'time': { 'start' :'1980-01-01T00:00:00', 'end' :'1999-12-31T00:00:00', 'crs' :'timestamps'}  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
v0 = cwt.Variable("collection://cip_merra2_mth", "ts", domain=d0  )

seasonal_cycle = cwt.Process.from_dict({'name': "xarray.ave", "groupBy": "monthOfYear", 'axes': "t"} )
seasonal_cycle.set_inputs( v0 )

seasonal_cycle_removed = cwt.Process.from_dict({'name': "xarray.eDiff", "domain": "d0"})
seasonal_cycle_removed.set_inputs( v0, seasonal_cycle )

eofs =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes" :"4", "compu" :"true" } )
eofs.set_inputs( seasonal_cycle_removed )

wps.execute( eofs, domains=[d0], async=True )
dataPaths = wps.download_result(eofs)
for dataPath in dataPaths:
    plotter.mpl_plot( dataPath, 0, True )