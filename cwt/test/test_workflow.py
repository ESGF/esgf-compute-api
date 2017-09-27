
import cwt, os
# import logging, cdms2, vcs
# from cwt.test.plotters import PlotMgr
# import cdms2, datetime, matplotlib, urllib3
# import matplotlib.pyplot as plt

# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'
host ="https://dptomcat03-int/wps/cwt"

class TestWorkflow:

    def run( self ):
        plotter = cwt.initialize()

        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mon_tas", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.average", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
        wps.execute( op, domain=d0, async=True )

        dataPath = wps.download_result(op)
        plotter.mpl_timeplot(dataPath,"Nd4jMaskedTensor")

executor = TestWorkflow()
executor.run()