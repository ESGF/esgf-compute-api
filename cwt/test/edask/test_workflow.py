import cwt, os, time
import numpy as np
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
    host = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )
    assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
    print "Connecting to wps host: " + host
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def clt_time_ave( self ):
        domain_data = { 'id': 'd0', 'lat':{'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
                        'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_cfsr_mth","clt",domain="d0" )
        op_data =  { 'name': "xarray.ave", 'axes':"t" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def regrid_test(self):
        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")

        op_data = {'name': "xarray.noOp", "grid": "uniform", "shape": "18,36", "res": "10,10"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true")

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)


    def weighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "xarray.ave", 'weights':'cosine', 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath)

    def nonweighted_spatial_ave(self):
        domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

        op_data = { 'name': "xarray.ave", 'axes': "xy" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(inputs)

        self.wps.execute(op, domains=[d0], async=True)

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath)



    def spatial_max( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':10, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

        op_data =  { 'name': "xarray.max", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath)

    def regrid( self ):

        domain_data = { 'id': 'd0', 'time': {'start':10, 'end':20, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable( "collection://giss_r1i1p1", "tas", domain="d0" )

        op_data =  { "name":"xarray.noOp", "grid":"gaussian", "shape":"32" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        op.set_inputs()

        self.wps.execute( op, domains=[d0], async=True )

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def sia_comparison_time_ave( self ):

        start_year = 1960     #  Holdings:  1958 - 2001
        end_year = 1969

        domain_data = { 'id': 'd0','time': {'start':str(start_year)+'-01-01T00:00:00','end':str(end_year)+'-12-31T23:00:00','crs':'timestamps'  } }
        d0 = cwt.Domain.from_dict(domain_data)

        print "\nExecuing global time average for variable 'tas' from collection 'iap-ua_eraint_tas1hr' for " + str(end_year-start_year+1) + " years, starting with " + str(start_year) +"\n"

        inputs = cwt.Variable( "collection://iap-ua_eraint_tas1hr", "tas", domain="d0" )

        op_data =  { 'name': "xarray.ave", 'axes': "t" }
        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=True )

        dataPaths = self.wps.download_result( op, self.temp_dir )
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def anomaly( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0' } )
        d1 = cwt.Domain.from_dict( { 'id': 'd1', 'lat': {'start':-40, 'end':-10, 'crs':'values'}, 'lon': {'start':115, 'end':155, 'crs':'values'} } )

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )
        v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d1  )

        v0_ave_data =  { 'name': "xarray.ave", 'axes': "xy"}
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )

        v1_ave_data =  { 'name': "xarray.ave", 'axes': "xy"}
        v1_ave =  cwt.Process.from_dict( v1_ave_data )
        v1_ave.set_inputs( v1 )

        anomaly =  cwt.Process.from_dict( { 'name': "xarray.eDiff", "domain": "d0" } )
        anomaly.set_inputs( v1_ave, v0_ave )

        self.wps.execute( anomaly, domains=[d0,d1], async=True )

        dataPaths = self.wps.download_result( anomaly, self.temp_dir )
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath)


    def climate_change_anomaly(self):
        d0_data = {'id': 'd0', 'time': {'start': '2016-01-01T00:00:00', 'end': '2016-12-31T23:00:00', 'crs': 'timestamps'}}
        d1_data = {'id': 'd1', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-12-31T23:00:00', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(d0_data)
        d1 = cwt.Domain.from_dict(d1_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
        v1 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d1)

        v0_ave_data = {'name': "xarray.ave", 'axes': "t"}
        v0_ave = cwt.Process.from_dict(v0_ave_data)
        v0_ave.set_inputs(v0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "t"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        anomaly = cwt.Process.from_dict( { 'name': "xarray.eDiff", "domain": "d0" } )
        anomaly.set_inputs(v0_ave, v1_ave)

        self.wps.execute(anomaly, domains=[d0, d1], async=True)

        dataPaths = self.wps.download_result(anomaly, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def diff_WITH_REGRID(self):
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-31T23:00:00', 'crs': 'timestamps'}  }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")
        v1 = cwt.Variable("collection://cip_cfsr_mth", "tas", domain="d0")

        op_data = {'name': "xarray.eDiff","crs":"~cip_merra2_mth"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0,v1)

        self.wps.execute(op, domains=[d0], async=True)

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def regrid_test_brief(self):
        domain_data = {'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-31T23:00:00', 'crs': 'timestamps'}  }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain="d0")

        op_data = {'name': "xarray.noOp", "grid":"uniform", "shape":"18,36", "res":"5,10" }
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true" )

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def regrid_test(self):
        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")

        op_data = {'name': "xarray.noOp", "grid": "uniform", "shape": "18,36", "res": "10,10"}
        op = cwt.Process.from_dict(op_data)  # """:type : Process """
        op.set_inputs(v0)

        self.wps.execute(op, domains=[d0], async=True, profile="true")

        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)

    def diff_with_regrid1(self):
        domain_data = { 'id': 'd0', 'time': {'start':"1990-01-01T00:00:00Z", 'end':"1991-01-01T00:00:00Z", 'crs':'timestamps'} }
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )
        v2 = cwt.Variable("collection://cip_cfsr_mth", "tas" )

        diff_data =  { 'name': "xarray.eDiff",  "crs":"~cip_merra2_mth" }
        diff_op =  cwt.Process.from_dict( diff_data )
        diff_op.set_inputs( v1, v2 )

        self.wps.execute( diff_op, domains=[d0], async=True )

        dataPaths = self.wps.download_result( diff_op, self.temp_dir )
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


  #       test("DiffWithRegrid")  { if(test_regrid)  {
  #   print( s"Running test DiffWithRegrid" )
  #   val MERRA_mon_variable = s"""{"uri":"collection:/cip_merra2_mon_1980-2015","name":"tas:v0","domain":"d0"}"""
  #   val CFSR_mon_variable   = s"""{"uri":"collection:/cip_cfsr_mon_1980-1995","name":"tas:v1","domain":"d0"}"""
  #   val ECMWF_mon_variable = s"""{"uri":"collection:/cip_ecmwf_mon_1980-2015","name":"tas:v2","domain":"d0"}"""
  #   val datainputs =
  #     s"""[   variable=[$MERRA_mon_variable,$CFSR_mon_variable],
  #             domain=[  {"name":"d0","time":{"start":"1990-01-01T00:00:00Z","end":"1991-01-01T00:00:00Z","system":"values"}},
  #                       {"name":"d1","time":{"start":"1990-01-01T00:00:00Z","end":"1991-01-01T00:00:00Z","system":"values"},"lat":{"start":20,"end":50,"system":"values"},"lon":{"start":30,"end":40,"system":"values"}} ],
  #             operation=[{"name":"xarray.eDiff","input":"v0,v1","domain":"d0","crs":"~cip_merra2_mon_1980-2015"}]]""".stripMargin.replaceAll("\\s", "")
  #   val result_node = executeTest(datainputs)
  #   val result_data = CDFloatArray( getResultData( result_node ).slice(0,0,10) )
  #   println( " ** Op Result:       " + result_data.mkBoundedDataString( ", ", 200 ) )
  # } }

    def average( self ):

        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':100, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )

        v1_ave_data =  { 'name': "xarray.ave", 'axes': "xt" }
        v1_ave =  cwt.Process.from_dict( v1_ave_data )
        v1_ave.set_inputs( v1 )

        self.wps.execute( v1_ave, domains=[d0], async=True )

        dataPaths = self.wps.download_result( v1_ave, self.temp_dir )
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def testClock(self):

        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)

        util_data = {'name': "util.testClock" }
        util_op = cwt.Process.from_dict(util_data)

        self.wps.execute(util_op, domains=[d0], async=True)
        dataPaths = self.wps.download_result(util_op, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def performance_test_global_1day(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def performance_test_global_1mth(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def performance_test_global_1y(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://cip_cfsr_mon_1980-1995", "tas", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def wps_test(self):
        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2001-12-31T23:59:00Z','crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable( "https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP//reanalysis/MERRA2/mon/atmos/tas.ncml", "tas", domain=d0)
        v1_ave_data = {'name': "xarray.ave", 'axes': "yx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)
        self.wps.execute(v1_ave, domains=[d0], async=True)
        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath,1)

    def performance_test_conus_1y(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)



    def performance_test_global(self):
        domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2015-01-01T00:00:00Z', 'crs': 'timestamps'} }

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True ) # , profile="active" )

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)



    def seasonal_anomaly( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40, 'crs':'values'}, 'lon': {'start':260, 'end':260, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z', 'crs': 'timestamps'} } )

        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )

        v0_ave_data =  { 'name': "xarray.ave", 'axes': "t", 'groupBy': "seasonOfYear" }
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )

        anomaly =  cwt.Process.from_dict( { 'name': "xarray.eDiff", "domain": "d0" } )
        anomaly.set_inputs( v0_ave, v0 )

        self.wps.execute( anomaly, domains=[d0], async=True )

        dataPaths = self.wps.download_result( anomaly, self.temp_dir )
        for dataPath in dataPaths:  self.plotter.mpl_timeplot(dataPath)

    def seasonal_cycle( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40, 'crs':'values'}, 'lon': {'start':260, 'end':260, 'crs':'values'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z', 'crs': 'timestamps'} } )
        v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0  )
        v0_ave_data =  { 'name': "xarray.ave", 'axes': "t", 'groupBy': "seasonOfYear" }
        v0_ave =  cwt.Process.from_dict( v0_ave_data )
        v0_ave.set_inputs( v0 )
        self.wps.execute( v0_ave, domains=[d0], async=True )
        dataPaths = self.wps.download_result( v0_ave, self.temp_dir )
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot(dataPath)

    def spatial_ave( self ):
        domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'}, 'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable( "collection://cip_cfsr_mth", "clt", domain=d0 )
        op_data = { 'name': "xarray.ave", 'axes': "t" }
        op = cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot(dataPath)

    def precip_test( self ):

        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'} } )
        v0 = cwt.Variable("collection://merra2_m2t1nxlnd", "PRECTOTLAND", domain=d0  )
        v0_ave =  cwt.Process.from_dict( { 'name': "xarray.ave", 'axes': "t", 'groupBy': "year" } )
        v0_ave.set_inputs( v0 )

        self.wps.execute( v0_ave, domains=[d0], async=True )

        dataPaths = self.wps.download_result( v0_ave, self.temp_dir )
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot(dataPath)

    def time_selection_test(self):
        domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'2010-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
        op_data =  { 'name': "xarray.ave", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot(dataPath)

    def time_bin_selection_test(self):
        domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'1990-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
        op_data =  { 'name': "xarray.ave", 'axes': "txy", "groupBy" : "year" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot(dataPath)

    def test_plot(self):
        self.plotter.mpl_spaceplot("/Users/tpmaxwel/.edas/wiqYJl6O.nc")

    def ListKernels(self):
        print self.wps.getCapabilities( "", False )

    def ListCollections(self):
        print self.wps.getCapabilities( "coll", False )


    def lowpass_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "xarray.lowpass", "groupBy": "5-year" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot( dataPath )

    def lowpass_profile_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-75,"end":75,"crs":"values"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v1 = cwt.Variable("collection://cip_20crv2c_mth", "psl:P", domain=d0  )
        lowpass = cwt.Process.from_dict({'name': "xarray.lowpass", "grid": "uniform", "shape": "32,72", "res": "5,5", "groupBy": "5-year"})
        lowpass.set_inputs(v1)
        self.wps.execute( lowpass, domains=[d0], async=True, profile="active" )
        dataPaths = self.wps.download_result(lowpass, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot( dataPath, 0, True )

    def highpass_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
        highpass =  cwt.Process.from_dict( { 'name': "xarray.highpass", "groupBy": "5-year" } )
        highpass.set_inputs( v0 )
        self.wps.execute( highpass, domains=[d0], async=True )
        dataPaths = self.wps.download_result(highpass, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot( dataPath )

    def highpass_test1( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-80,"end":80,"crs":"values"} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
        highpass =  cwt.Process.from_dict( { 'name': "xarray.highpass", "grid": "uniform", "shape": "32,72", "res": "5,5", "groupBy": "5-year" } )
        highpass.set_inputs( v0 )
        self.wps.execute( highpass, domains=[d0], async=True )
        dataPaths = self.wps.download_result(highpass, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot( dataPath )

 #   val datainputs = s"""[domain=[{"name":"d0","lat":{"start":25,"end":25,"system":"indices"},"lon":{"start":20,"end":20,"system":"indices"}}],variable=[{"uri":"collection:/giss_r1i1p1","name":"tas:v1","domain":"d0"}],operation=[{"name":"xarray.lowpass","input":"v1","domain":"d0","groupBy":"5-year"}]]"""


    def baseline_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33, 'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'}} ) # , 'time': { 'start':'1900-01-01T00:00:00', 'end':'2000-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "xarray.subset" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot( dataPath )

    def binning_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':5, 'end':7,'crs':'indices'}, 'lon': {'start':5, 'end':10, 'crs':'indices'} ,
                                     'time': { 'start':'1850-01-01T00:00:00Z', 'end':'1854-01-01T00:00:00Z', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain=d0  )
        yearlyAve =  cwt.Process.from_dict( { 'name': "xarray.ave", "axes":"t", "groupBy": "year" } )
        yearlyAve.set_inputs( v0 )
        self.wps.execute( yearlyAve, domains=[d0], async=True )
        dataPaths = self.wps.download_result(yearlyAve, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.print_data( dataPath )



        #     230.1202, 224.2958, 228.4658, 228.0224, 226.1936, 225.7275,
        #     222.0484, 223.9207, 223.3873, 222.8198, 225.1187, 224.4428,
        #     229.7138, 229.7007, 229.8149, 229.4356, 227.8259, 228.9415,
        #     231.1172, 229.9618, 228.9264, 228.0932, 227.1155, 226.0691,
        #     227.9059, 227.116,  226.5818, 225.653,  224.769,  223.5814,
        #     229.1446, 229.0689, 229.1144, 229.0135, 227.8756, 228.0897,
        #     223.9355, 228.5432, 228.4396, 227.1773, 223.7382, 225.177,
        #     228.7011, 226.9322, 218.759, 218.5423, 225.1021,  224.3837,
        #     229.1338, 227.1501, 229.3834, 228.9121, 228.2971, 228.9964,
        #     231.3791, 230.4205, 225.0711, 228.0521, 227.1422, 225.7934,
        #     228.5478, 227.8226, 223.3534, 224.6234, 226.147,  225.1512,
        #     228.3303, 228.9947, 228.601, 229.2599, 228.1443, 228.9194).map(_.toFloat), Float.MaxValue)
        #
        # """[domain=[{"name":"d0","lat":{"start":5,"end":7,"system":"indices"},"lon":{"start":5,"end":10,"system":"indices"},"time":{"start":"1850-01-01T00:00:00Z","end":"1854-01-01T00:00:00Z","system":"timestamps"}}],
        #         | variable=[{"uri":"collection:/giss_r1i1p1","name":"tas:v1","domain":"d0"}],
        #         | operation=[{ "name":"xarray.ave", "axes":"t", "input":"v1", "groupBy":"year" }]]""".stripMargin


    def reset_wps( self ):
        d0 = cwt.Domain.from_dict( {'id': 'd0' } )
        reset =  cwt.Process.from_dict( { 'name': "util.reset" } )
        self.wps.execute( reset, domains=[d0]  )

    def performance_test_conus_1day( self, weighted ):
        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)
        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx", "weights":"cosine"} if weighted else {'name': "xarray.ave", 'axes': "tyx" }
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)
        self.wps.execute(v1_ave, domains=[d0], async=True)
        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.print_Mdata(dataPath)

    def test_getCollections(self):
        return self.wps.getCapabilities("coll",False)

    def performance_test_conus(self):
        domain_data = { 'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'} }
#        domain_data = { 'id': 'd0' }

        d0 = cwt.Domain.from_dict(domain_data)

        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.print_Mdata(dataPath)

    def svd_test_reduced( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-75,"end":75,"crs":"values"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v1 = cwt.Variable("collection://cip_20crv2c_mth", "psl:P", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"8", "compu":"true" } )
        svd.set_inputs( v1 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot( dataPath, 0, True )

    def svd_test2( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-75,"end":75,"crs":"values"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas:T", domain=d0  )
        v1 = cwt.Variable("collection://cip_20crv2c_mth", "psl:P", domain=d0  )
        highpass = cwt.Process.from_dict({'name': "xarray.highpass", "grid": "uniform", "shape": "32,72", "res": "5,5", "groupBy": "5-year"})
        highpass.set_inputs(v0,v1)
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"8" } )
        svd.set_inputs( highpass )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot( dataPath, 0, True )


    def svd_test_0( self ):
        d200 = cwt.Domain.from_dict( { 'id': 'd200', "lat":{"start":-75,"end":75,"crs":"values"}, "level":{"start":16,"end":16,"crs":"indices"}, "filter":"DJF" } )
        d500 = cwt.Domain.from_dict( { 'id': 'd500', "lat":{"start":-75,"end":75,"crs":"values"}, "level":{"start":10,"end":10,"crs":"indices"}, "filter":"DJF" } )
        d850 = cwt.Domain.from_dict( { 'id': 'd850', "lat":{"start":-75,"end":75,"crs":"values"}, "level":{"start":3,"end":3,"crs":"indices"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        ds = cwt.Domain.from_dict( { 'id': 'ds', "lat":{"start":-75,"end":75,"crs":"values"}, 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'}, "filter":"DJF" } )
        v200 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P200", domain=d200  )
        v500 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P500", domain=d500  )
        v850 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P850", domain=d850  )
        vs = cwt.Variable("collection://cip_20crv2c_mth", "psl:PS", domain=ds  )
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"8", "grid": "uniform", "shape": "32,72", "res": "5,5" } )
        svd.set_inputs( vs )
        self.wps.execute( svd, domains=[ds], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot( dataPath, 0, True )


    def regrid_cip_20crv_zg_collection( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0' } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P", domain=d0  )
        regrid =  cwt.Process.from_dict( { 'name':"xarray.noOp", "grid":"uniform", "shape":"32,72", "res":"5,5" } )
        regrid.set_inputs( v0 )
        self.wps.execute( regrid, domains=[d0], async=True, runargs={ "responseForm":"collection:cip_20crv2c_mth_zg_32x72" } )
        self.wps.track_status(regrid)

    def svd_test_zg( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-75,"end":75,"crs":"values"}, "level":{"start":5,"end":5,"crs":"indices"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"8", "grid": "uniform", "shape": "32,72", "res": "5,5" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot( dataPath, 0, True )

    def svd_test_zg1(self):
        d0 = cwt.Domain.from_dict({'id': 'd0', "lat": {"start": -75, "end": 75, "crs": "values"}, "level": {"start": 5, "end": 5, "crs": "indices"}, "filter": "DJF"})  # } ) # , "filter":"DJF" , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P0", domain=d0)
        #        d1 = cwt.Domain.from_dict( { 'id': 'd1', "lat":{"start":-75,"end":75,"crs":"values"}, "level":{"start":10,"end":10,"crs":"indices"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        #        v1 = cwt.Variable("collection://cip_20crv2c_mth", "zg:P1", domain=d1  )
        highpass =  cwt.Process.from_dict( { 'name': "xarray.highpass", "domain": "d0", "groupBy": "5-year", "grid": "uniform", "shape": "30,72", "res": "5,5" } )
        highpass.set_inputs( v0 )
        svd = cwt.Process.from_dict(  {'name': "SparkML.svd", "modes": "8" } )
        svd.set_inputs( highpass )
        self.wps.execute(svd, domains=[d0], async=True)
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_plot(dataPath, 0, True)

    def svd_test_zg1_col(self):
        d0 = cwt.Domain.from_dict({'id': 'd0',  "level": {"start": 5, "end": 5, "crs": "indices"}, "filter": "DJF"})  # } ) # , "filter":"DJF" , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_20crv2c_zg_DJF_32x72_NDT", "zg", domain=d0)
        svd = cwt.Process.from_dict(  {'name': "SparkML.svd", "modes": "8", "norm": "false" } )
        svd.set_inputs( v0 )
        self.wps.execute(svd, domains=[d0], async=True)
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_plot(dataPath, 0, True)

    def svd_test_ts( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-75,"end":75,"crs":"values"}, "filter":"DJF" } ) #  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_cfsr_mth", "ts", domain=d0  )
        svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"4", "grid": "uniform", "shape": "32,72", "res": "5,5" } )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[d0], async=True )
        dataPaths = self.wps.download_result(svd, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_plot( dataPath, 0, True )

    def preprocess_zg1(self):
        d0 = cwt.Domain.from_dict({'id': 'd0', "lat": {"start": -80, "end": 80, "crs": "values"}, "filter": "DJF"})
        v0 = cwt.Variable("collection://cip_20crv2c_mth", "zg", domain=d0)
        rescale = cwt.Process.from_dict(  {'name': "SparkML.rescale", "domain": "d0", "grid": "uniform", "shape": "32,72", "responseForm": "collection:cip_20crv2c_zg_DJF_32x72_NDT" } )
        rescale.set_inputs( v0 )
        self.wps.execute(rescale, domains=[d0], async=True ) #, runargs = {"responseForm": "collection:cip_20crv2c_zg_DJF_32x72_NDT"} )

    def cloud_cover_demo(self):
        domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'}, 'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://cip_cfsr_mth", "clt", domain=d0 )

        op_data = { 'name': "xarray.ave", "weights":"cosine", 'axes': "t" }
        op = cwt.Process.from_dict( op_data )
        op.set_inputs( v1 )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)
        for dataPath in dataPaths:  self.plotter.mpl_spaceplot(dataPath)


    def performance_test_conus_1mth(self):
        #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

        domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

        v1_ave_data = {'name': "xarray.ave", 'axes': "tyx", "cache":"true"}
        v1_ave = cwt.Process.from_dict(v1_ave_data)
        v1_ave.set_inputs(v1)

        self.wps.execute(v1_ave, domains=[d0], async=True)

        dataPaths = self.wps.download_result(v1_ave, self.temp_dir)
        for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

    def cip_cloud_cover(self):

        domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'},'lon': {'start':-125, 'end':-70.3, 'crs':'values'},'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://cip_cfsr_mth", "clt",domain=d0 )

        op_data = { 'name': "xarray.ave", "weights":"cosine", 'axes': "t" }
        op = cwt.Process.from_dict( op_data )
        op.set_inputs( v1 )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)
        for dataPath in dataPaths: self.plotter.mpl_spaceplot(dataPath)

    def cip_high_precip(self):
        domain_data = { 'id': 'd0', 'lat': {'start':37, 'end':38,'crs':'values'}, 'lon': {'start':0, 'end':100, 'crs':'values'}, 'time':{'start':'2014-09-01T00:00:00', 'end':'2017-03-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v0 = cwt.Variable("collection://cip_merra2_mth", "pr",domain=d0 )

        op_data = { 'name': "xarray.max", 'axes': "xy" }
        op = cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( v0 )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths  = self.wps.download_result(op)
        for dataPath in dataPaths: self.plotter.mpl_timeplot(dataPath)

    def cip_precip_sum(self):
        domain_data = { 'id': 'd0', 'lat': {'start':20, 'end':57,'crs':'values'}, 'lon': {'start':-190, 'end':-118, 'crs':'values'}, 'time':{'start':'2014-12-15T00:00:00', 'end':'2014-12-20T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_6hr", "pr",domain=d0 )
        op_data = { 'name': "xarray.sum", 'axes': "xy" }
        op = cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        op_data1 = { 'name': "xarray.sum", 'axes': "t" }
        op1 = cwt.Process.from_dict( op_data1 ) # """:type : Process """
        op1.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)

        self.wps.execute( op1, domains=[d0], async=True )
        dataPaths1 = self.wps.download_result(op1)

        for dataPath in dataPaths: self.plotter.mpl_timeplot(dataPath)
        for dataPath1 in dataPaths1: self.plotter.mpl_spaceplot(dataPath1)

    def cip_max_temp(self):
        domain_data = { 'id': 'd0', 'lat': {'start':46, 'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'1980-06-01T00:00:00', 'end':'2016-08-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v0 = cwt.Variable( "collection://cip_eraint_mth", "tas", domain=d0 )
        op_data = { 'name': "xarray.max", 'axes': "xy" }
        op = cwt.Process.from_dict( op_data )
        op.set_inputs( v0 )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)
        for dataPath in dataPaths:
            self.plotter.mpl_timeplot(dataPath)

    def cip_max_temp_heatwave(self):
        domain_data = { 'id': 'd0', 'lat': {'start':46,'end':47,'crs':'values'}, 'lon': {'start':5, 'end':15, 'crs':'values'}, 'time':{'start':'2002-06-01T00:00:00', 'end':'2002-08-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        v0 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d0 )

        op_data = { 'name': "xarray.max", 'axes': "xy" }
        op = cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( v0 )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)

        domain_data = { 'id': 'd1', 'lat': {'start':46,'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'2003-06-01T00:00:00','end':'2003-08-31T23:00:00', 'crs':'timestamps'}}
        d1 = cwt.Domain.from_dict(domain_data)
        v1 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d1 )

        op_data1 = { 'name': "xarray.max", 'axes': "xy" }
        op1 = cwt.Process.from_dict( op_data1 ) # """:type : Process """
        op1.set_inputs( v1 )

        self.wps.execute( op1, domains=[d1], async=True )
        dataPaths1 = self.wps.download_result(op1)
        for dataPath in dataPaths: self.plotter.mpl_timeplot(dataPath)
        for dataPath1 in dataPaths1: self.plotter.mpl_timeplot(dataPath1)

    def cip_min_temp(self):
        domain_data = { 'id': 'd0', 'lat': {'start':40.2, 'end':40.5,'crs':'values'}, 'lon': {'start':-105.6, 'end':-105.8, 'crs':'values'}, 'time':{'start':'1948-01-01T00:00:00', 'end':'2009-12-31T23:00:00', 'crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://iap-ua_nra_tas1hr", "tas", domain=d0 )

        op_data = { 'name': "xarray.min", 'axes': "xy" }
        op = cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)
        for dataPath in dataPaths: self.plotter.mpl_timeplot(dataPath)

    def plot_test(self, plot_files):
        for plot_file in plot_files:
            self.plotter.mpl_plot(plot_file, 0, True)

    def data_plotter(self):
        data =  np.array( [ 0.19393921, -1.2894897, -0.8175659, -2.628357, 0.14718628, -2.170807, 0.76083374, 1.3248596, 0.57592773, -0.674469, -0.0138549805, 0.31555176, -0.7801819, -3.9342346, 1.8656921, -0.934845, -0.072906494, -0.026885986,
                            0.10437012, 1.9228516, -1.3204346, 1.5502625, 1.3361816, -0.23022461, -1.8243713, -0.80422974, -1.894104, -1.0467529, -0.83477783, 1.6516724, 0.19799805, 0.16830444, 0.65579224, -2.20813, 0.47097778, 0.025634766, 2.710968,
                            -3.6307068, 2.4335632, -0.8474121, 1.7366333, 0.7738342, 0.67840576, -0.7659607, -2.5101624, 1.5240479, 0.30142212, -0.09515381, -3.1026917, 0.7971802, 0.0016784668, -0.60372925, -0.97579956, 0.21594238, -0.039855957, 0.41815186,
                            -0.2744751, 2.3583984, -0.7037964, 1.361023, 2.7900085, -0.37365723, -1.190155, -1.7558594, 0.7376404, -0.56625366, -0.6083374, -2.4179382, 0.4194336, 0.14251709, 0.3616333, -0.475708, -0.8239746, -0.27529907, -0.020629883, -0.9572449,
                            0.25823975, -0.5349121, -0.7706909, -1.1563416, -0.43118286, 0.7505493, 0.041534424, 0.7348938, -2.2020264, -0.52459717, 1.0487671, 0.159729, 0.4981079, -0.2133789, -0.332489, -1.0993652, 0.41140747, -1.5540161, -0.65740967, -1.0648193,
                            1.2191467, -0.7008667, -2.1305542, -2.209137] )
        self.plotter.graph_data( data )

    def timeseries_processing_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40,'crs':'values'}, 'lon': {'start':40, 'end':40, 'crs':'values'}, 'time': { 'start':'1980-01-01T00:00:00', 'end':'1988-01-01T00:00:00', 'crs':'timestamps'}  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_merra2_mth", "ts", domain=d0  )

        seasonal_cycle = cwt.Process.from_dict({'name': "xarray.ave", "groupBy": "monthOfYear", 'axes': "t"} )
        seasonal_cycle.set_inputs( v0 )

        seasonal_cycle_removed = cwt.Process.from_dict({'name': "xarray.eDiff", "domain": "d0"})
        seasonal_cycle_removed.set_inputs( v0, seasonal_cycle )
        op = seasonal_cycle_removed

        op.set_inputs( v0 )
        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.print_data( dataPath )

    def eofs_test( self ):
        d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':-80, 'end':80,'crs':'values'}, 'time': { 'start':'1980-01-01T00:00:00', 'end':'1999-12-31T00:00:00', 'crs':'timestamps'}  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
    #         d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':-50, 'end':50,'crs':'values'}, 'lon': {'start':120, 'end':290,'crs':'values'}, 'time': { 'start':'1980-01-01T00:00:00', 'end':'1999-12-31T00:00:00', 'crs':'timestamps'}  } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
        v0 = cwt.Variable("collection://cip_merra2_mth", "ts", domain=d0  )

        seasonal_cycle = cwt.Process.from_dict({'name': "xarray.ave", "groupBy": "monthOfYear", 'axes': "t"} )
        seasonal_cycle.set_inputs( v0 )

        seasonal_cycle_removed = cwt.Process.from_dict({'name': "xarray.eDiff", "domain": "d0"})
        seasonal_cycle_removed.set_inputs( v0, seasonal_cycle )

        eofs =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":"4", "compu":"true" } )
        eofs.set_inputs( seasonal_cycle_removed )

        self.wps.execute( eofs, domains=[d0], async=True )
        dataPaths = self.wps.download_result(eofs, self.temp_dir)
        for dataPath in dataPaths:
            self.plotter.mpl_plot( dataPath, 0, True )

    def test_getCapabilities(self):
        return self.wps.getCapabilities("",False)

if __name__ == '__main__':
    executor = TestWorkflow()
    executor.cip_high_precip()

#    executor.cip_max_temp()
#    executor.performance_test_conus_1mth()


#    dataPaths = "/Users/tpmaxwel/.edas/p0lVpkMf.nc"
#    executor.plotter.performance_test_global(dataPath)


# if __name__ == '__main__':
#     plotter = cwt.initialize()
#     host = "https://edas.nccs.nasa.gov/wps/cwt"
#     wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
#     d0 = cwt.Domain.from_dict(  {'id': 'd0', 'lat': {'start': 5, 'end': 7, 'crs': 'indices'}, 'lon': {'start': 5, 'end': 10, 'crs': 'indices'}, 'time': {'start': '1850-01-01T00:00:00Z', 'end': '1854-01-01T00:00:00Z', 'crs': 'timestamps'}})
#     v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain=d0)
#     yearlyAve = cwt.Process.from_dict({'name': "xarray.ave", "axes": "t", "groupBy": "year"})
#     yearlyAve.set_inputs(v0)
#     wps.execute(yearlyAve, domains=[d0], async=True)
#     dataPaths = wps.download_result(yearlyAve)
#     plotter.print_data(dataPath)

#    dataPaths = "/Users/tpmaxwel/.edas/p0lVpkMf.nc"
#    executor.plotter.performance_test_global(dataPath)


# if __name__ == '__main__':
#     plotter = cwt.initialize()
#     host = "https://edas.nccs.nasa.gov/wps/cwt"
#     wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
#     d0 = cwt.Domain.from_dict(  {'id': 'd0', 'lat': {'start': 5, 'end': 7, 'crs': 'indices'}, 'lon': {'start': 5, 'end': 10, 'crs': 'indices'}, 'time': {'start': '1850-01-01T00:00:00Z', 'end': '1854-01-01T00:00:00Z', 'crs': 'timestamps'}})
#     v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain=d0)
#     yearlyAve = cwt.Process.from_dict({'name': "xarray.ave", "axes": "t", "groupBy": "year"})
#     yearlyAve.set_inputs(v0)
#     wps.execute(yearlyAve, domains=[d0], async=True)
#     dataPaths = wps.download_result(yearlyAve)
#     plotter.print_data(dataPath)
