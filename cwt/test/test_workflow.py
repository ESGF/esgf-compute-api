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
    host = "https://edas.nccs.nasa.gov/wps/cwt"
#    host ="https://dptomcat03-int/wps/cwt"
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def clt_time_ave( self ):
        domain_data = { 'id': 'd0', 'lat':{'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
                        'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_cfsr_mth","clt",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"t" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def time_selection_test(self):

        domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'2010-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )

        op_data =  { 'name': "CDSpark.ave", 'axes': "xy" }

        op =  cwt.Process.from_dict( op_data ) # """:type : Process """

        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op, self.temp_dir)

        self.plotter.mpl_timeplot(dataPath,True)

    def weighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "CDSpark.ave", 'weights':'cosine', 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_timeplot(dataPath)

    def nonweighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "CDSpark.ave", 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_timeplot(dataPath)



    def spatial_max( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':10, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        op_data =  { 'name': "CDSpark.max", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result(op, self.temp_dir)
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

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def sia_comparison_time_ave( self ):

        start_year = 1960     #  Holdings:  1958 - 2001
        end_year = 1969

        domain_data = { 'id': 'd0','time': {'start':str(start_year)+'-01-01T00:00:00','end':str(end_year)+'-12-31T23:00:00','crs':'timestamps'  } }
        d0 = cwt.Domain.from_dict(domain_data)

        print "\nExecuing global time average for variable 'tas' from collection 'iap-ua_eraint_tas1hr' for " + str(end_year-start_year+1) + " years, starting with " + str(start_year) +"\n"

        inputs = cwt.Variable( "collection://iap-ua_eraint_tas1hr", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.ave", 'axes': "t" }
        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=True )

        dataPath = self.wps.download_result( op, self.temp_dir )
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"
        self.plotter.mpl_spaceplot(dataPath)

    def anomaly( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0' } )
        d1 = cwt.Domain.from_dict( { 'id': 'd1', 'lat': {'start':-40, 'end':-10, 'crs':'values'}, 'lon': {'start':115, 'end':155, 'crs':'values'} } )

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )
        v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d1  )

        v0_ave_data =  { 'name': "CDSpark.ave", 'axes': "xy"}
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )

        v1_ave_data =  { 'name': "CDSpark.ave", 'axes': "xy"}
        v1_ave =  cwt.Process.from_dict( v1_ave_data )
        v1_ave.set_inputs( v1 )

        anomaly =  cwt.Process.from_dict( { 'name': "CDSpark.eDiff", "domain": "d0" } )
        anomaly.set_inputs( v1_ave, v0_ave )

        self.wps.execute( anomaly, domains=[d0,d1], async=True )

        dataPath = self.wps.download_result( anomaly, self.temp_dir )
        self.plotter.mpl_timeplot(dataPath)

    def climate_change_anomaly(self):
        d0_data = {'id': 'd0', 'time': {'start': '2016-01-01T00:00:00', 'end': '2016-12-31T23:00:00', 'crs': 'timestamps'}}
        d1_data = {'id': 'd1', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-12-31T23:00:00', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(d0_data)
        d1 = cwt.Domain.from_dict(d1_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
        v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d1)

        v0_ave_data = {'name': "CDSpark.ave", 'axes': "t"}
        v0_ave = cwt.Process.from_dict(v0_ave_data)
        v0_ave.set_inputs(v0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "t"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        anomaly = cwt.Process.from_dict( { 'name': "CDSpark.eDiff", "domain": "d0" } )
        anomaly.set_inputs(v0_ave, v1_ave)

        self.wps.execute(anomaly, domains=[d0, d1], async=True)

        dataPath = self.wps.download_result(anomaly, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def average( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':100, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )

        v1_ave_data =  { 'name': "CDSpark.ave", 'axes': "xt" }
        v1_ave =  cwt.Process.from_dict( v1_ave_data )
        v1_ave.set_inputs( v1 )

        self.wps.execute( v1_ave, domains=[d0], async=True )

        dataPath = self.wps.download_result( v1_ave, self.temp_dir )
        self.plotter.print_Mdata(dataPath)


    def test_plot(self):
        self.plotter.mpl_timeplot("/tmp/testData.nc")

    def ListKernels(self):
        print self.wps.getCapabilities( "", False )

    def ListCollections(self):
        print self.wps.getCapabilities( "coll", False )

executor = TestWorkflow()
executor.spatial_max()


