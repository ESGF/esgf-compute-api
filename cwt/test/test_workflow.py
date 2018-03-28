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

    def regrid_test(self):
        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")

        op_data = {'name': "CDSpark.noOp", "grid": "uniform", "shape": "18,36", "res": "10,10"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true")

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)


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

    def regrid( self ):

        domain_data = { 'id': 'd0', 'time': {'start':10, 'end':20, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable( "collection://giss_r1i1p1", "tas", domain="d0" )

        op_data =  { "name":"CDSpark.noOp", "grid":"gaussian", "shape":"32" }
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

    def diff_WITH_REGRID(self):
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-31T23:00:00', 'crs': 'timestamps'}  }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")
        v1 = cwt.Variable("collection://cip_cfsr_mth", "tas", domain="d0")

        op_data = {'name': "CDSpark.eDiff","crs":"~cip_merra2_mth"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0,v1)

        self.wps.execute(op, domains=[d0], async=True)

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def regrid_test_brief(self):
        domain_data = {'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-31T23:00:00', 'crs': 'timestamps'}  }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain="d0")

        op_data = {'name': "CDSpark.noOp", "grid":"uniform", "shape":"18,36", "res":"5,10" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true" )

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def regrid_test(self):
        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")

        op_data = {'name': "CDSpark.noOp", "grid": "uniform", "shape": "18,36", "res": "10,10"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true")

        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_spaceplot(dataPath)

    def diff_with_regrid1(self):
        domain_data = { 'id': 'd0', 'time': {'start':"1990-01-01T00:00:00Z", 'end':"1991-01-01T00:00:00Z", 'crs':'timestamps'} }
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )
        v2 = cwt.Variable("collection://cip_cfsr_mth", "tas" )

        diff_data =  { 'name': "CDSpark.eDiff",  "crs":"~cip_merra2_mth" }
        diff_op =  cwt.Process.from_dict( diff_data )
        diff_op.set_inputs( v1, v2 )

        self.wps.execute( diff_op, domains=[d0], async=True )

        dataPath = self.wps.download_result( diff_op, self.temp_dir )
        self.plotter.print_Mdata(dataPath)


  #       test("DiffWithRegrid")  { if(test_regrid)  {
  #   print( s"Running test DiffWithRegrid" )
  #   val MERRA_mon_variable = s"""{"uri":"collection:/cip_merra2_mon_1980-2015","name":"tas:v0","domain":"d0"}"""
  #   val CFSR_mon_variable   = s"""{"uri":"collection:/cip_cfsr_mon_1980-1995","name":"tas:v1","domain":"d0"}"""
  #   val ECMWF_mon_variable = s"""{"uri":"collection:/cip_ecmwf_mon_1980-2015","name":"tas:v2","domain":"d0"}"""
  #   val datainputs =
  #     s"""[   variable=[$MERRA_mon_variable,$CFSR_mon_variable],
  #             domain=[  {"name":"d0","time":{"start":"1990-01-01T00:00:00Z","end":"1991-01-01T00:00:00Z","system":"values"}},
  #                       {"name":"d1","time":{"start":"1990-01-01T00:00:00Z","end":"1991-01-01T00:00:00Z","system":"values"},"lat":{"start":20,"end":50,"system":"values"},"lon":{"start":30,"end":40,"system":"values"}} ],
  #             operation=[{"name":"CDSpark.eDiff","input":"v0,v1","domain":"d0","crs":"~cip_merra2_mon_1980-2015"}]]""".stripMargin.replaceAll("\\s", "")
  #   val result_node = executeTest(datainputs)
  #   val result_data = CDFloatArray( getResultData( result_node ).slice(0,0,10) )
  #   println( " ** Op Result:       " + result_data.mkBoundedDataString( ", ", 200 ) )
  # } }

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

    def testClock(self):

        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        util_data = {'name': "util.testClock" }
        util_op = cwt.Process.from_dict(util_data)

        self.wps.execute(util_op, domains=[d0], async=True)
        dataPath = self.wps.download_result(util_op, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def performance_test_global_1day(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def performance_test_global_1mth(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def performance_test_conus_1mth(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)


    def performance_test_global_1y(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def performance_test_conus_1y(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)



    def performance_test_global(self):
        domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'} }

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def performance_test_conus(self):
        domain_data = { 'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'} }
#        domain_data = { 'id': 'd0' }

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)

        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

    def seasonal_anomaly( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40, 'crs':'values'}, 'lon': {'start':260, 'end':260, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z', 'crs': 'timestamps'} } )

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )

        v0_ave_data =  { 'name': "CDSpark.ave", 'axes': "t", 'groupBy': "seasonOfYear" }
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )

        anomaly =  cwt.Process.from_dict( { 'name': "CDSpark.eDiff", "domain": "d0" } )
        anomaly.set_inputs( v0_ave, v0 )

        self.wps.execute( anomaly, domains=[d0], async=True )

        dataPath = self.wps.download_result( anomaly, self.temp_dir )
        self.plotter.mpl_timeplot(dataPath)

    def seasonal_cycle( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40, 'crs':'values'}, 'lon': {'start':260, 'end':260, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z', 'crs': 'timestamps'} } )
        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )
        v0_ave_data =  { 'name': "CDSpark.ave", 'axes': "t", 'groupBy': "seasonOfYear" }
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )
        self.wps.execute( v0_ave, domains=[d0], async=True )
        dataPath = self.wps.download_result( v0_ave, self.temp_dir )
        self.plotter.mpl_timeplot(dataPath)

    def spatial_ave( self ):
        domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'}, 'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable( "collection://cip_cfsr_mth", "clt", domain=d0 )
        op_data = { 'name': "CDSpark.ave", 'axes': "t" }
        op = cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPath = self.wps.download_result(op)
        self.plotter.mpl_spaceplot(dataPath)

    def precip_test( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'} } )
        v0 = cwt.Variable("collection://merra2_m2t1nxlnd", "PRECTOTLAND", domain=d0  )
        v0_ave =  cwt.Process.from_dict( { 'name': "CDSpark.ave", 'axes': "t", 'groupBy': "year" } )
        v0_ave.set_inputs( v0 )

        self.wps.execute( v0_ave, domains=[d0], async=True )

        dataPath = self.wps.download_result( v0_ave, self.temp_dir )
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
        self.plotter.mpl_timeplot(dataPath)

    def time_bin_selection_test(self):
        domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'1990-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes': "txy", "groupBy" : "year" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPath = self.wps.download_result(op, self.temp_dir)
        self.plotter.mpl_timeplot(dataPath)

    def test_plot(self):
        self.plotter.mpl_spaceplot("/Users/tpmaxwel/.edas/efmfoD8o.nc")

    def ListKernels(self):
        print self.wps.getCapabilities( "", False )

    def ListCollections(self):
        print self.wps.getCapabilities( "coll", False )

    def svd_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-80,"end":80,"crs":"values"}, "filter":"DJF" } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
        highpass = cwt.Process.from_dict({'name': "CDSpark.highpass", "grid": "uniform", "shape": "32,72", "res": "5,5", "groupBy": "10-year"})
        highpass.set_inputs(v0)
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"9" } )
        svd.set_inputs( highpass )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPath = self.wps.download_result(svd, self.temp_dir)
        self.plotter.mpl_spaceplot( dataPath, 0, True )

    def lowpass_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "CDSpark.lowpass", "groupBy": "5-year" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPath = self.wps.download_result(svd, self.temp_dir)
        self.plotter.mpl_timeplot( dataPath )

    def highpass_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
        highpass =  cwt.Process.from_dict( { 'name': "CDSpark.highpass", "groupBy": "5-year" } )
        highpass.set_inputs( v0 )
        self.wps.execute( highpass, domains=[d0], async=True )
        dataPath = self.wps.download_result(highpass, self.temp_dir)
        self.plotter.mpl_timeplot( dataPath )

 #   val datainputs = s"""[domain=[{"name":"d0","lat":{"start":25,"end":25,"system":"indices"},"lon":{"start":20,"end":20,"system":"indices"}}],variable=[{"uri":"collection:/giss_r1i1p1","name":"tas:v1","domain":"d0"}],operation=[{"name":"CDSpark.lowpass","input":"v1","domain":"d0","groupBy":"5-year"}]]"""


    def baseline_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33, 'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'}} ) # , 'time': { 'start':'1900-01-01T00:00:00', 'end':'2000-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "CDSpark.subset" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPath = self.wps.download_result(svd, self.temp_dir)
        self.plotter.mpl_timeplot( dataPath )


    def reset_wps( self ):
        d0 = cwt.Domain.from_dict( {'id': 'd0' } )
        reset =  cwt.Process.from_dict( { 'name': "util.reset" } )
        self.wps.execute( reset, domains=[d0]  )

    def performance_test_conus_1day( self, weighted ):
        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://merrra2_m2i1nxint", "KE", domain=d0)
        v1_ave_data = {'name': "CDSpark.ave", 'axes': "tyx", "weights":"cosine"} if weighted else {'name': "CDSpark.ave", 'axes': "tyx" }
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)
        self.wps.execute(v1_ave, domains=[d0], async=True)
        dataPath = self.wps.download_result(v1_ave, self.temp_dir)
        self.plotter.print_Mdata(dataPath)

if __name__ == '__main__':
    executor = TestWorkflow()
    executor.svd_test()

#    dataPath = "/Users/tpmaxwel/.edas/p0lVpkMf.nc"
#    executor.plotter.performance_test_global(dataPath)

