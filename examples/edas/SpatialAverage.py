import cwt, os

plotter = cwt.initialize()
host ="https://dptomcat03-int/wps/cwt"

wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

d0 = cwt.Domain.from_dict( {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'values'}} )
inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

op_data = { 'name': "CDSpark.ave", 'weights': 'cosine', 'axes': "xy" }
op = cwt.Process.from_dict(op_data)
op.set_inputs(inputs)

wps.execute(op, domains=[d0] )

dataPath = wps.download_result(op)
plotter.mpl_timeplot(dataPath)