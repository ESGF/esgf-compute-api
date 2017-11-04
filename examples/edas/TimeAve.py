import cwt, os

plotter = cwt.initialize()
host ="https://dptomcat03-int/wps/cwt"

wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':90, 'crs':'values'} }

d0 = cwt.Domain.from_dict(domain_data)
inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

op_data = {'name': "CDSpark.ave", 'axes': "t"}
op = cwt.Process.from_dict(op_data)
op.set_inputs(inputs)

wps.execute(op, domains=[d0] )

dataPath = wps.download_result(op)
plotter.mpl_timeplot(dataPath)