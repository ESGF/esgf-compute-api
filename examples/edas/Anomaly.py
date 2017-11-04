import cwt, os

plotter = cwt.initialize()
host ="https://dptomcat03-int/wps/cwt"

wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

d0_data = { 'id': 'd0', 'lat': {'start':0, 'end':60, 'crs':'values'}, 'lon': {'start':0, 'end':60, 'crs':'values'}, 'time': {'start':0, 'end':100, 'crs':'indices'} }
d0 = cwt.Domain.from_dict(d0_data)

d1_data = { 'id': 'd1', 'lat': {'start':30, 'end':30, 'crs':'values'}, 'lon': {'start':30, 'end':30, 'crs':'values'}, 'time': {'start':0, 'end':100, 'crs':'indices'} }
d1 = cwt.Domain.from_dict(d1_data)

v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )
v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d1 )

v0_ave_data =  { 'name': "CDSpark.ave", 'axes': "xy" }
v0_ave =  cwt.Process.from_dict( v0_ave_data )
v0_ave.set_inputs( v0 )

anomaly =  cwt.Process.from_dict( { 'name': "CDSpark.diff2" } )
anomaly.set_inputs( v1, v0_ave )

wps.execute(anomaly, domains=[d0,d1] )

dataPath = wps.download_result( anomaly )
plotter.mpl_timeplot(dataPath)




