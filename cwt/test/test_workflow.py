import cwt, os, time
# import logging, cdms2, vcs
# from cwt.test.plotters import PlotMgr
# import cdms2, datetime, matplotlib, urllib3
# import matplotlib.pyplot as plt
# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

class TestWorkflow:
    plotter = cwt.initialize()
    host ="https://dptomcat03-int/wps/cwt"
#    host = "https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt"
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def time_selection_test(self):

        domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'2011-01-01T00:00:00', 'end':'2011-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )

        op_data =  { 'name': "CDSpark.ave", 'axes': "xy" }

        op =  cwt.Process.from_dict( op_data ) # """:type : Process """

        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op)

        self.plotter.mpl_timeplot(dataPath)

    def weighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "CDSpark.ave", 'weights':'cosine', 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_timeplot(dataPath)

    def nonweighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "CDSpark.ave", 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_timeplot(dataPath)



    def spatial_max( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':10, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        op_data =  { 'name': "CDSpark.max", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_timeplot(dataPath)

    def time_ave( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':90, 'crs':'values'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable( "collection://cip_merra2_mth", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.ave", 'axes': "t" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        op.set_inputs()

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op)
        self.plotter.mpl_spaceplot(dataPath)

    def sia_comparison_time_ave( self ):

        start_year = 1958     #  Holdings:  1958 - 2001
        end_year = 1968

        domain_data = { 'id': 'd0','time': {'start':str(start_year)+'-01-01T00:00:00','end':str(end_year)+'-12-31T23:00:00','crs':'timestamps'  } }
        d0 = cwt.Domain.from_dict(domain_data)

        print "\nExecuing global time average for variabe 'tas' from collection 'iap-ua_eraint_tas1hr' for " + str(end_year-start_year+1) + " years, starting with " + str(start_year) +"\n"

        inputs = cwt.Variable( "collection://iap-ua_eraint_tas1hr", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.ave", 'axes': "t" }
        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        op.set_inputs()

        start = time.time()
        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result( op, self.temp_dir )
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"
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

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )

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
executor.time_selection_test()

