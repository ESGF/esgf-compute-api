import cwt, getpass
collections =  [ "cip_jra55_6hr", "cip_merra2_6hr", "cip_cfsr_6hr", "cip_eraint_6hr" ]
d0 = cwt.Domain.from_dict( { 'id': 'd0', 'time': {'start':'1980-01-01T00:00:00','end':'1980-12-31T23:00:00','crs':'timestamps'}, 'lev': {'start':'80000','end':'80000','crs':'values'} } )

plotter = cwt.initialize()
wps = cwt.WPS( "https://edas.nccs.nasa.gov/wps/cwt", log=True, log_file="/tmp/{}/logs/esgf_api.log".format(getpass.getuser()), verify=False )
ens_inputs = [ cwt.Variable( "collection://" + collection, "ta", domain=d0, name=collection ) for collection in collections ]
ens_ave = cwt.Process.from_dict({ 'name': "CDSpark.eAve", "cwt": "~cip_jra55_6hr", "input": ens_inputs })
wps.execute( ens_ave, domains=[d0] )
wps.get_status( ens_ave )
