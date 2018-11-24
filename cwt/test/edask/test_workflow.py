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

plotter = cwt.initialize()
host = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )
assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
print "Connecting to wps host: " + host
wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
temp_dir = create_tempdir()

def test_kernel_error( self ):
    domain_data = { 'id': 'd0', 'lat':{'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
                    'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00','crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_cfsr_mth","clt",domain="d0" )
    op_data =  { 'name': "ssdrrr.xyxy", 'axes':"t" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_clt_time_ave( self ):
    domain_data = { 'id': 'd0', 'lat':{'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
                    'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00','crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_cfsr_mth","clt",domain="d0" )
    op_data =  { 'name': "xarray.ave", 'axes':"t" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_weighted_spatial_ave(self):
    domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.ave", 'axes': "xy" }
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(inputs)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_nonweighted_spatial_ave(self):
    domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.mean", 'axes': "xy" }
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(inputs)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_spatial_max( self ):

    domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':10, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
    d0 = cwt.Domain.from_dict(domain_data)

    inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

    op_data =  { 'name': "xarray.max", 'axes': "xy" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )

    wps.execute( op, domains=[d0], async=True )

    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_sia_comparison_time_ave( self ):

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
    wps.execute( op, domains=[d0], async=True )

    dataPaths = wps.download_result( op, self.temp_dir )
    end = time.time()
    print "\nCompleted execution in " + str(end-start) + " secs\n"
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_anomaly( self ):

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
    anomaly =  cwt.Process.from_dict( { 'name': "xarray.diff", "domain": "d0" } )
    anomaly.set_inputs( v1_ave, v0_ave )

    wps.execute( anomaly, domains=[d0,d1], async=True )

    dataPaths = wps.download_result( anomaly, self.temp_dir )
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_climate_change_anomaly(self):
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

    anomaly = cwt.Process.from_dict( { 'name': "xarray.diff", "domain": "d0" } )
    anomaly.set_inputs(v0_ave, v1_ave)

    wps.execute(anomaly, domains=[d0, d1], async=True)

    dataPaths = wps.download_result(anomaly, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_diff_WITH_REGRID(self):
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-31T23:00:00', 'crs': 'timestamps'}  }
    d0 = cwt.Domain.from_dict(domain_data)

    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")
    v1 = cwt.Variable("collection://cip_cfsr_mth", "tas", domain="d0")

    op_data = {'name': "xarray.diff","crs":"~cip_merra2_mth"}
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(v0,v1)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_diff_with_regrid1(self):
    domain_data = { 'id': 'd0', 'time': {'start':"1990-01-01T00:00:00Z", 'end':"1991-01-01T00:00:00Z", 'crs':'timestamps'} }
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )
    v2 = cwt.Variable("collection://cip_cfsr_mth", "tas" )

    diff_data =  { 'name': "xarray.diff",  "crs":"~cip_merra2_mth" }


    diff_op = cwt.Process.from_dict(diff_data)
    diff_op.set_inputs(v1, v2)

    wps.execute(diff_op, domains=[d0], async=True)

    dataPaths = wps.download_result(diff_op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_average(self):
    domain_data = {'id': 'd0', 'lat': {'start': 70, 'end': 90, 'crs': 'values'},
                   'lon': {'start': 5, 'end': 45, 'crs': 'values'}, 'time': {'start': 0, 'end': 100, 'crs': 'indices'}}
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_merra2_mth", "tas")

    v1_ave_data = {'name': "xarray.ave", 'axes': "xt"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_testClock(self):
    domain_data = {'id': 'd0'}
    d0 = cwt.Domain.from_dict(domain_data)

    util_data = {'name': "util.testClock"}
    util_op = cwt.Process.from_dict(util_data)

    wps.execute(util_op, domains=[d0], async=True)
    dataPaths = wps.download_result(util_op, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_performance_test_global_1day(self):
    domain_data = {'id': 'd0',
                   'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_performance_test_global_1mth(self):
    #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

    domain_data = {'id': 'd0',
                   'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_performance_test_global_1y(self):
    #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_cfsr_mon_1980-1995", "tas", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_wps_test(self):
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2001-12-31T23:59:00Z','crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable( "https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP//reanalysis/MERRA2/mon/atmos/tas.ncml", "tas", domain=d0)
    v1_ave_data = {'name': "xarray.ave", 'axes': "yx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)
    wps.execute(v1_ave, domains=[d0], async=True)
    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath,1)

def test_performance_test_conus_1y(self):
    #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
    domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)



def test_performance_test_global(self):
    domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2015-01-01T00:00:00Z', 'crs': 'timestamps'} }
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)  # , profile="active" )

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_seasonal_anomaly(self):
    d0 = cwt.Domain.from_dict({'id': 'd0', 'lat': {'start': 40, 'end': 40, 'crs': 'values'},
                               'lon': {'start': 260, 'end': 260, 'crs': 'values'},
                               'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z',
                                        'crs': 'timestamps'}})
    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
    v0_ave_data = {'name': "xarray.ave", 'axes': "t", 'groupby': "t.season"}
    v0_ave = cwt.Process.from_dict(v0_ave_data)
    v0_ave.set_inputs(v0)
    anomaly = cwt.Process.from_dict({'name': "xarray.diff", "domain": "d0"})
    anomaly.set_inputs(v0_ave, v0)

    wps.execute(anomaly, domains=[d0], async=True)
    dataPaths = wps.download_result(anomaly, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_seasonal_cycle(self):
    d0 = cwt.Domain.from_dict({'id': 'd0', 'lat': {'start': 40, 'end': 40, 'crs': 'values'},
                               'lon': {'start': 260, 'end': 260, 'crs': 'values'},
                               'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z',
                                        'crs': 'timestamps'}}
                              )
    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
    v0_ave_data = {'name': "xarray.ave", 'axes': "t", 'groupby': "t.season"}
    v0_ave = cwt.Process.from_dict(v0_ave_data)
    v0_ave.set_inputs(v0)
    wps.execute(v0_ave, domains=[d0], async=True)
    dataPaths = wps.download_result(v0_ave, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)


def test_spatial_ave(self):
    domain_data = {'id': 'd0', 'lat': {'start': 23.7, 'end': 49.2, 'crs': 'values'},
                   'lon': {'start': -125, 'end': -70.3, 'crs': 'values'},
                   'time': {'start': '1980-01-01T00:00:00', 'end': '2016-12-31T23:00:00', 'crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_cfsr_mth", "clt", domain=d0)
    op_data = {'name': "xarray.ave", 'axes': "t"}
    op = cwt.Process.from_dict(op_data)
    op.set_inputs(inputs)
    wps.execute(op, domains=[d0], async=True)
    dataPaths = wps.download_result(op)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)


def test_precip_test(self):
    d0 = cwt.Domain.from_dict(
        {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'}})

    v0 = cwt.Variable("collection://merra2_m2t1nxlnd", "PRECTOTLAND", domain=d0  )
    v0_ave =  cwt.Process.from_dict( { 'name': "xarray.ave", 'axes': "t", 'groupBy': "t.year" } )
    v0_ave.set_inputs( v0 )

    wps.execute( v0_ave, domains=[d0], async=True )

    dataPaths = wps.download_result( v0_ave, self.temp_dir )
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_time_selection_test(self):
    domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'2010-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
    op_data =  { 'name': "xarray.ave", 'axes': "xy" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_time_bin_selection_test(self):
    domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'1990-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
    op_data =  { 'name': "xarray.ave", 'axes': "txy", "groupby" : "t.year" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_ListKernels(self):
    print wps.getCapabilities( "", False )

def test_ListCollections(self):
    print wps.getCapabilities( "coll", False )


def test_lowpass_test( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'}} )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
    svd =  cwt.Process.from_dict( { 'name': "xarray.lowpass", "wsize": 60 } )
    svd.set_inputs( v0 )
    wps.execute( svd, domains=[d0], async=True )
    dataPaths = wps.download_result(svd, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata( dataPath )

def test_highpass_test( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'}} )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
    highpass =  cwt.Process.from_dict( { 'name': "xarray.detrend", "wsize": 60 } )
    highpass.set_inputs( v0 )
    wps.execute( highpass, domains=[d0], async=True )
    dataPaths = wps.download_result(highpass, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata( dataPath )

def test_highpass_test1( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-80,"end":80,"crs":"values"} } ) # , 'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
    highpass =  cwt.Process.from_dict( { 'name': "xarray.detrend", "wsize": 60  } )
    highpass.set_inputs( v0 )
    wps.execute( highpass, domains=[d0], async=True )
    dataPaths = wps.download_result(highpass, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata( dataPath )

#   val datainputs = s"""[domain=[{"name":"d0","lat":{"start":25,"end":25,"system":"indices"},"lon":{"start":20,"end":20,"system":"indices"}}],variable=[{"uri":"collection:/giss_r1i1p1","name":"tas:v1","domain":"d0"}],operation=[{"name":"array.lowpass","input":"v1","domain":"d0","groupBy":"5-year"}]]"""


def test_baseline_test( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33, 'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'}} ) # , 'time': { 'start':'1900-01-01T00:00:00', 'end':'2000-12-31T23:00:00', 'crs':'timestamps' } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
    svd =  cwt.Process.from_dict( { 'name': "xarray.subset" } )
    svd.set_inputs( v0 )
    wps.execute( svd, domains=[d0], async=True )
    dataPaths = wps.download_result(svd, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata( dataPath )

def test_binning_test( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':5, 'end':7,'crs':'indices'}, 'lon': {'start':5, 'end':10, 'crs':'indices'} ,
                                 'time': { 'start':'1850-01-01T00:00:00Z', 'end':'1854-01-01T00:00:00Z', 'crs':'timestamps'} } )
    v0 = cwt.Variable("collection://giss_r1i1p1", "tas", domain=d0  )
    yearlyAve =  cwt.Process.from_dict( { 'name': "xarray.ave", "axes":"t", "groupBy": "t.year" } )
    yearlyAve.set_inputs( v0 )
    wps.execute( yearlyAve, domains=[d0], async=True )
    dataPaths = wps.download_result(yearlyAve, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_data( dataPath )

def test_performance_test_conus_1day(self, weighted):
    domain_data = {'id': 'd0', 'lat': {'start': 229, 'end': 279, 'crs': 'indices'},
                   'lon': {'start': 88, 'end': 181, 'crs': 'indices'},
                   'time': {'start': '1980-01-15T00:00:00Z', 'end': '1980-01-15T23:59:59Z', 'crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)
    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx" } if weighted else {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)
    wps.execute(v1_ave, domains=[d0], async=True)
    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_test_getCollections(self):
    return wps.getCapabilities("coll", False)

def test_performance_test_conus(self):
    domain_data = {'id': 'd0', 'lat': {'start': 229, 'end': 279, 'crs': 'indices'},
                   'lon': {'start': 88, 'end': 181, 'crs': 'indices'},
                   'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_cloud_cover_demo(self):
    domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'}, 'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_cfsr_mth", "clt", domain=d0 )

    op_data = { 'name': "xarray.ave", 'axes': "t" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v1 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)


def test_performance_test_conus_1mth(self):
    #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }

    domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-01-31T23:59:59Z', 'crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx" }
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, self.temp_dir)
    for dataPath in dataPaths:  self.plotter.print_Mdata(dataPath)

def test_cip_cloud_cover(self):

    domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'},'lon': {'start':-125, 'end':-70.3, 'crs':'values'},'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_cfsr_mth", "clt",domain=d0 )

    op_data = { 'name': "xarray.ave", 'axes': "t" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v1 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)
    for dataPath in dataPaths: self.plotter.print_Mdata(dataPath)

def test_cip_high_precip( self ):
    domain_data = { 'id': 'd0', 'lat': {'start':37, 'end':38,'crs':'values'}, 'lon': {'start':0, 'end':100, 'crs':'values'}, 'time':{'start':'2014-09-01T00:00:00', 'end':'2017-03-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable("collection://cip_merra2_mth", "pr",domain=d0 )

    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( v0 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths  = wps.download_result(op)
    for dataPath in dataPaths: self.plotter.print_Mdata(dataPath)

def test_cip_precip_sum(self):
    domain_data = { 'id': 'd0', 'lat': {'start':20, 'end':57,'crs':'values'}, 'lon': {'start':-190, 'end':-118, 'crs':'values'}, 'time':{'start':'2014-12-15T00:00:00', 'end':'2014-12-20T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)

    inputs = cwt.Variable("collection://cip_merra2_6hr", "pr",domain=d0 )
    op_data = { 'name': "xarray.sum", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )

    op_data1 = { 'name': "xarray.sum", 'axes': "t" }
    op1 = cwt.Process.from_dict( op_data1 ) # """:type : Process """
    op1.set_inputs( inputs )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)

    wps.execute( op1, domains=[d0], async=True )
    dataPaths1 = wps.download_result(op1)

    for dataPath in dataPaths: self.plotter.print_Mdata(dataPath)
    for dataPath1 in dataPaths1: self.plotter.print_Mdata(dataPath1)

def test_cip_max_temp(self):
    domain_data = { 'id': 'd0', 'lat': {'start':46, 'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'1980-06-01T00:00:00', 'end':'2016-08-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable( "collection://cip_eraint_mth", "tas", domain=d0 )
    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v0 )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)
    for dataPath in dataPaths:
        self.plotter.print_Mdata(dataPath)

def test_cip_max_temp_heatwave(self):
    domain_data = { 'id': 'd0', 'lat': {'start':46,'end':47,'crs':'values'}, 'lon': {'start':5, 'end':15, 'crs':'values'}, 'time':{'start':'2002-06-01T00:00:00', 'end':'2002-08-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d0 )

    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( v0 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)

    domain_data = { 'id': 'd1', 'lat': {'start':46,'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'2003-06-01T00:00:00','end':'2003-08-31T23:00:00', 'crs':'timestamps'}}
    d1 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d1 )

    op_data1 = { 'name': "xarray.max", 'axes': "xy" }
    op1 = cwt.Process.from_dict( op_data1 ) # """:type : Process """
    op1.set_inputs( v1 )

    wps.execute( op1, domains=[d1], async=True )
    dataPaths1 = wps.download_result(op1)
    for dataPath in dataPaths: self.plotter.print_Mdata(dataPath)
    for dataPath1 in dataPaths1: self.plotter.print_Mdata(dataPath1)

def test_cip_min_temp(self):
    domain_data = { 'id': 'd0', 'lat': {'start':40.2, 'end':40.5,'crs':'values'}, 'lon': {'start':-105.6, 'end':-105.8, 'crs':'values'}, 'time':{'start':'1948-01-01T00:00:00', 'end':'2009-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://iap-ua_nra_tas1hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.min", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op)
    for dataPath in dataPaths: self.plotter.print_Mdata(dataPath)

def test_timeseries_processing_test( self ):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40,'crs':'values'}, 'lon': {'start':40, 'end':40, 'crs':'values'}, 'time': { 'start':'1980-01-01T00:00:00', 'end':'1988-01-01T00:00:00', 'crs':'timestamps'}  } ) # ,'time': { 'start':'1990-01-01T00:00:00', 'end':'1995-12-31T23:00:00', 'crs':'timestamps'} } )
    v0 = cwt.Variable("collection://cip_merra2_mth", "ts", domain=d0  )

    seasonal_cycle = cwt.Process.from_dict({'name': "xarray.ave", "groupby": "t.month", 'axes': "t"} )
    seasonal_cycle.set_inputs( v0 )

    seasonal_cycle_removed = cwt.Process.from_dict({'name': "xarray.diff", "domain": "d0"})
    seasonal_cycle_removed.set_inputs( v0, seasonal_cycle )
    op = seasonal_cycle_removed
    op.set_inputs( v0 )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, self.temp_dir)
    for dataPath in dataPaths:
        self.plotter.print_data( dataPath )

if __name__ == '__main__':
    test_kernel_error()