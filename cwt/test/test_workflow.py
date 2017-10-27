
import cwt, os
# import logging, cdms2, vcs
# from cwt.test.plotters import PlotMgr
# import cdms2, datetime, matplotlib, urllib3
# import matplotlib.pyplot as plt

# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'


class TestWorkflow:
    plotter = cwt.initialize()
    host ="https://dptomcat03-int/wps/cwt"
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

    def spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'values'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = {'name': "CDSpark.ave", 'axes': "xy"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_timeplot(dataPath)

    def spatial_max( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':-180, 'end':-180, 'crs':'values'}, 'lon': {'start':0, 'end':90, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        op_data =  { 'name': "CDSpark.max", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_timeplot(dataPath)

    def time_ave( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        op_data =  { 'name': "CDSpark.ave", 'axes': "t" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        op.set_inputs()

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_spaceplot(dataPath)

    def anomaly( self ):

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

        self.wps.execute( anomaly, domains=[d0,d1], async=True )

        dataPath = self.wps.download_result( anomaly )
        self.plotter.mpl_timeplot(dataPath)

    def average( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':100, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        v1_ave_data =  { 'name': "CDSpark.ave", 'axes': "xt" }
        v1_ave =  cwt.Process.from_dict( v1_ave_data )
        v1_ave.set_inputs( v1 )

        self.wps.execute( v1_ave, domains=[d0], async=True )

        dataPath = self.wps.download_result( v1_ave )
        self.plotter.print_Mdata(dataPath)


    def test_plot(self):
        self.plotter.mpl_timeplot("/tmp/testData.nc")

    def ListKernels(self):
        print self.wps.getCapabilities( "", False )

    def ListCollections(self):
        print self.wps.getCapabilities( "coll", False )

executor = TestWorkflow()
executor.spatial_max()

