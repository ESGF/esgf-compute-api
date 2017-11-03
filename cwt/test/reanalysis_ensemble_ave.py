import cwt, os

def getEnsembleInput( collection, levels ):
    variable = cwt.Variable( "collection://" + collection, "ta", domain=d0, name=collection )
    var_filtered = cwt.Process.from_dict({'name': "CDSpark.compress", 'plev': levels})
    var_filtered.set_inputs(variable)
    return var_filtered

plotter = cwt.initialize()
wps = cwt.WPS( "https://dptomcat03-int/wps/cwt" )
levels = "100000,97500,95000,92500,90000,87500,85000,82500,80000,77500,75000,70000,65000,60000,55000,50000,45000,40000,35000,30000,25000,20000,15000,10000"
domain_data = {'id':'d0','time':{'start':'1980-01-01T00:00:00','end':'1980-12-31T23:00:00','crs':'values'}}
d0 = cwt.Domain.from_dict(domain_data)
collections =  [ "cip_jra55_6hr", "cip_merra2_6hr", "cip_cfsr_6hr", "cip_eraint_6hr" ]

ens_inputs =  [ getEnsembleInput( collection, levels ) for collection in collections ]
ens_ave = cwt.Process.from_dict({ 'name': "CDSpark.eAve" })
ens_ave.set_inputs( ens_inputs )

wps.execute( ens_ave, domains=[d0], async=True )

