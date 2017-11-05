import cwt, os

def getEnsembleInput( collection, domain ):
    variable = cwt.Variable( "collection://" + collection, "ta", domain=domain, name=collection )
    return variable

plotter = cwt.initialize()
host = "https://dptomcat03-int/wps/cwt"
wps = cwt.WPS(host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False)

d0 = cwt.Domain.from_dict( { 'id': 'd0',
      'time': {'start':'1980-01-01T00:00:00','end':'1980-01-01T23:59:00','crs':'timestamps'},
      'level': { 'start':'70000', 'end':'70000', 'crs':'values' } } )

collections =  [ "cip_jra55_6hr", "cip_merra2_6hr", "cip_cfsr_6hr", "cip_eraint_6hr" ]
ens_inputs = [ getEnsembleInput( collection, d0 ) for collection in collections ]
ens_ave = cwt.Process.from_dict({ 'name': "CDSpark.eAve", "crs": "~cip_jra55_6hr", "input": ens_inputs })

wps.execute( ens_ave, domains=[d0] )

dataPath = wps.download_result( ens_ave )
print "Operation completed, result: " + dataPath

