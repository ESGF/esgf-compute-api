import cwt, getpass
levels = """100000,97500,95000,92500,90000,87500,85000,82500,80000,77500,75000,70000,65000,60000,55000,50000,45000,40000,35000,30000,25000,20000,15000,10000"""
collections =  [ "cip_jra55_6hr", "cip_merra2_6hr", "cip_cfsr_6hr", "cip_eraint_6hr" ]
d0 = cwt.Domain.from_dict( { 'id': 'd0', 'time': {'start':'1980-01-01T00:00:00','end':'1980-01-31T23:59:00','crs':'timestamps'} } )

def getEnsembleInput( collection, levels, domain ):
    variable = cwt.Variable( "collection://" + collection, "ta", domain=domain, name="ta-" + collection )
    return cwt.Process.from_dict( { 'name':"CDSpark.filter", 'plev':levels, 'input':variable, 'result':"filt-ta-"+collection } )

plotter = cwt.initialize()
wps = cwt.WPS( "https://edas.nccs.nasa.gov/wps/cwt", log=True, log_file="/tmp/{}/logs/esgf_api.log".format(getpass.getuser()), verify=False )
ens_inputs = [ getEnsembleInput( collection, levels, d0 ) for collection in collections ]
ens_ave = cwt.Process.from_dict({ 'name': "CDSpark.eAve", "cwt": "~cip_jra55_6hr", "input": ens_inputs })
wps.execute( ens_ave, domains=[d0] )
wps.get_status( ens_ave )
