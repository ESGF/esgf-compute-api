import cwt, os, time
import numpy as np
# import logging, cdms2, vcs
# from cwt.test.plotters import PlotMgr
# import cdms2, datetime, matplotlib, urllib3
# import matplotlib.pyplot as plt
# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'

plotter = cwt.initialize()

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

def generate_output( dataPath, plot ):
    if plot: plotter.mpl_plot( dataPath )
    else: plotter.print_data( dataPath )

host = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )
assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
print "Connecting to wps host: " + host
wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
temp_dir = create_tempdir()

def test_binning(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':5, 'end':7,'crs':'indices'}, 'lon': {'start':5, 'end':10, 'crs':'indices'}, 'time': { 'start':'1950-01-01T00:00:00Z', 'end':'2001-01-01T00:00:00Z', 'crs':'timestamps'} } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
    yearlyAve =  cwt.Process.from_dict( { 'name': "xarray.ave", "axes":"t", "groupby": "t.year" } )
    yearlyAve.set_inputs( v0 )
    wps.execute( yearlyAve, domains=[d0], async=True )
    dataPaths = wps.download_result(yearlyAve, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_precip(plot=False):
    d0 = cwt.Domain.from_dict(  {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2014-12-31T23:59:00Z', 'crs': 'timestamps'}})
    v0 = cwt.Variable("collection://cip_merra_6hr", "tas", domain=d0  )
    v0_ave =  cwt.Process.from_dict( { 'name': "xarray.ave", 'axes': "t", 'groupby': "t.year" } )
    v0_ave.set_inputs( v0 )
    wps.execute( v0_ave, domains=[d0], async=True )
    dataPaths = wps.download_result( v0_ave, temp_dir, True )
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_time_bin_selection(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'1990-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain=d0 )
    op0 =  cwt.Process.from_dict( { 'name': "xarray.ave", 'axes': "xy" } ) # """:type : Process """
    op0.set_inputs( inputs )
    op1 =  cwt.Process.from_dict( { 'name': "xarray.ave", 'axes': "t", "groupby" : "t.year" } ) # """:type : Process """
    op1.set_inputs( op0 )
    wps.execute( op1, domains=[d0], async=True )
    dataPaths = wps.download_result(op1, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_lowpass(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
    svd =  cwt.Process.from_dict( { 'name': "xarray.lowpass", "wsize": 60 } )
    svd.set_inputs( v0 )
    wps.execute( svd, domains=[d0], async=True )
    dataPaths = wps.download_result(svd, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_spatial_ave(plot=False):
    domain_data = {'id': 'd0', 'lat': {'start': 23.7, 'end': 49.2, 'crs': 'values'},
                   'lon': {'start': -125, 'end': -70.3, 'crs': 'values'},
                   'time': {'start': '1980-01-01T00:00:00', 'end': '2016-12-31T23:00:00', 'crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_cfsr_mth", "clt", domain=d0)
    op_data = {'name': "xarray.ave", 'axes': "t"}
    op = cwt.Process.from_dict(op_data)
    op.set_inputs(inputs)
    wps.execute(op, domains=[d0], async=True)
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_time_selection(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':-90, 'end':90,'crs':'values'}, 'lon': {'start':-180, 'end':180, 'crs':'values'}, 'time': { 'start':'2010-01-01T00:00:00', 'end':'2010-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_mth", "pr", domain="d0" )
    op_data =  { 'name': "xarray.ave", 'axes': "xy" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_ListKernels(plot=False):
    print wps.getCapabilities( "", False )

def test_ListCollections(plot=False):
    print wps.getCapabilities( "coll", False )

def test_highpass(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33,'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'} } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
    highpass =  cwt.Process.from_dict( { 'name': "xarray.detrend", "wsize": 60 } )
    highpass.set_inputs( v0 )
    wps.execute( highpass, domains=[d0], async=True )
    dataPaths = wps.download_result(highpass, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_highpass1(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":-80,"end":80,"crs":"values"} } )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "tas", domain=d0  )
    highpass =  cwt.Process.from_dict( { 'name': "xarray.detrend", "wsize": 60  } )
    highpass.set_inputs( v0 )
    wps.execute( highpass, domains=[d0], async=True )
    dataPaths = wps.download_result(highpass, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_baseline(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':33, 'end':33, 'crs':'indices'}, 'lon': {'start':33, 'end':33, 'crs':'indices'}} )
    v0 = cwt.Variable("collection://cip_20crv2c_mth", "psl", domain=d0  )
    svd =  cwt.Process.from_dict( { 'name': "xarray.subset" } )
    svd.set_inputs( v0 )
    wps.execute( svd, domains=[d0], async=True )
    dataPaths = wps.download_result(svd, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )


def test_test_getCollections(plot=False):
    return wps.getCapabilities("coll", False)

def test_cloud_cover_demo(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'}, 'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_cfsr_mth", "clt", domain=d0 )
    op_data = { 'name': "xarray.ave", 'axes': "t" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v1 )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_cip_cloud_cover(plot=False):

    domain_data = { 'id': 'd0', 'lat': {'start':23.7,'end':49.2,'crs':'values'},'lon': {'start':-125, 'end':-70.3, 'crs':'values'},'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_cfsr_mth", "clt",domain=d0 )

    op_data = { 'name': "xarray.ave", 'axes': "t" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v1 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths: generate_output( dataPath, plot )

def test_cip_high_precip(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':37, 'end':38,'crs':'values'}, 'lon': {'start':0, 'end':100, 'crs':'values'}, 'time':{'start':'2014-09-01T00:00:00', 'end':'2017-03-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable("collection://cip_merra2_mth", "pr",domain=d0 )

    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( v0 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths  = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths: generate_output( dataPath, plot )

def test_cip_precip_sum(plot=False):
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
    dataPaths = wps.download_result(op, temp_dir, True)

    wps.execute( op1, domains=[d0], async=True )
    dataPaths1 = wps.download_result(op1, temp_dir, True)

    for dataPath in dataPaths: generate_output( dataPath, plot )
    for dataPath1 in dataPaths1: plotter.print_Mdata(dataPath1)

def test_cip_max_temp(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':46, 'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'1980-06-01T00:00:00', 'end':'2016-08-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable( "collection://cip_eraint_mth", "tas", domain=d0 )
    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data )
    op.set_inputs( v0 )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_cip_max_temp_heatwave(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':46,'end':47,'crs':'values'}, 'lon': {'start':5, 'end':15, 'crs':'values'}, 'time':{'start':'2002-06-01T00:00:00', 'end':'2002-08-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v0 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d0 )

    op_data = { 'name': "xarray.max", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( v0 )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)

    domain_data = { 'id': 'd1', 'lat': {'start':46,'end':47,'crs':'values'},'lon': {'start':5, 'end':15, 'crs':'values'},'time':{'start':'2003-06-01T00:00:00','end':'2003-08-31T23:00:00', 'crs':'timestamps'}}
    d1 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable("collection://cip_eraint_6hr", "tas",domain=d1 )

    op_data1 = { 'name': "xarray.max", 'axes': "xy" }
    op1 = cwt.Process.from_dict( op_data1 ) # """:type : Process """
    op1.set_inputs( v1 )

    wps.execute( op1, domains=[d1], async=True )
    dataPaths1 = wps.download_result(op1, temp_dir, True)
    for dataPath in dataPaths: generate_output( dataPath, plot )
    for dataPath1 in dataPaths1: generate_output( dataPath1, plot )

def test_cip_min_temp(plot=False):
    domain_data = { 'id': 'd0', 'lat': {'start':40.2, 'end':40.5,'crs':'values'}, 'lon': {'start':-105.6, 'end':-105.8, 'crs':'values'}, 'time':{'start':'1948-01-01T00:00:00', 'end':'2009-12-31T23:00:00', 'crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://iap-ua_nra_tas1hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.min", 'axes': "xy" }
    op = cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )

    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths: generate_output( dataPath, plot )

def test_timeseries_processing(plot=False):
    d0 = cwt.Domain.from_dict( { 'id': 'd0', 'lat': {'start':40, 'end':40,'crs':'values'}, 'lon': {'start':40, 'end':40, 'crs':'values'}, 'time': { 'start':'1980-01-01T00:00:00', 'end':'1988-01-01T00:00:00', 'crs':'timestamps'}  } )
    v0 = cwt.Variable("collection://cip_merra2_mth", "ts", domain=d0  )
    seasonal_cycle = cwt.Process.from_dict({'name': "xarray.ave", "groupby": "t.month", 'axes': "t"} )
    seasonal_cycle.set_inputs( v0 )
    seasonal_cycle_removed = cwt.Process.from_dict({'name': "xarray.diff", "domain": "d0"})
    seasonal_cycle_removed.set_inputs( v0, seasonal_cycle )
    op = seasonal_cycle_removed
    op.set_inputs( v0 )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )


def test_clt_time_ave(plot=False):
    domain_data = { 'id': 'd0', 'lat':{'start':23.7,'end':49.2,'crs':'values'}, 'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
                    'time':{'start':'1980-01-01T00:00:00','end':'2016-12-31T23:00:00','crs':'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_cfsr_mth","clt",domain="d0" )
    op_data =  { 'name': "xarray.ave", 'axes':"t" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )
    wps.execute( op, domains=[d0], async=True )
    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_weighted_spatial_ave(plot=False):
    domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.ave", 'axes': "xy" }
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(inputs)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_nonweighted_spatial_ave(plot=False):
    domain_data = {'id':'d0','time':{'start':'1995-01-01T00:00:00','end':'1997-12-31T23:00:00','crs':'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)
    inputs = cwt.Variable("collection://cip_merra2_6hr", "tas", domain=d0 )

    op_data = { 'name': "xarray.mean", 'axes': "xy" }
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(inputs)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_spatial_max(plot=False):

    domain_data = { 'id': 'd0', 'lat': {'start':0, 'end':90, 'crs':'values'}, 'lon': {'start':0, 'end':10, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
    d0 = cwt.Domain.from_dict(domain_data)

    inputs = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0 )

    op_data =  { 'name': "xarray.max", 'axes': "xy" }
    op =  cwt.Process.from_dict( op_data ) # """:type : Process """
    op.set_inputs( inputs )

    wps.execute( op, domains=[d0], async=True )

    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_anomaly(plot=False):

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

    dataPaths = wps.download_result( anomaly, temp_dir, True )
    for dataPath in dataPaths:  generate_output( dataPath, plot )


def test_climate_change_anomaly(plot=False):
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

    dataPaths = wps.download_result(anomaly, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_diff_WITH_REGRID(plot=False):
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-02-29T23:00:00', 'crs': 'timestamps'}  }
    d0 = cwt.Domain.from_dict(domain_data)

    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain="d0")
    v1 = cwt.Variable("collection://cip_cfsr_mth", "tas", domain="d0")

    op_data = {'name': "xarray.diff","crs":"~cip_merra2_mth"}
    op = cwt.Process.from_dict(op_data)  # """:type : Process """
    op.set_inputs(v0,v1)

    wps.execute(op, domains=[d0], async=True)

    dataPaths = wps.download_result(op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_diff_with_regrid1(plot=False):
    domain_data = { 'id': 'd0', 'time': {'start':"1990-01-01T00:00:00Z", 'end':"1991-01-01T00:00:00Z", 'crs':'timestamps'} }
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_merra2_mth", "tas" )
    v2 = cwt.Variable("collection://cip_cfsr_mth", "tas" )

    diff_data =  { 'name': "xarray.diff",  "crs":"~cip_merra2_mth" }


    diff_op = cwt.Process.from_dict(diff_data)
    diff_op.set_inputs(v1, v2)

    wps.execute(diff_op, domains=[d0], async=True)

    dataPaths = wps.download_result(diff_op, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )


def test_average(plot=False):
    domain_data = {'id': 'd0', 'lat': {'start': 70, 'end': 90, 'crs': 'values'},
                   'lon': {'start': 5, 'end': 45, 'crs': 'values'}, 'time': {'start': 0, 'end': 100, 'crs': 'indices'}}
    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_merra2_mth", "tas")

    v1_ave_data = {'name': "xarray.ave", 'axes': "xt"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )


def test_wps(plot=False):
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2001-12-31T23:59:00Z','crs': 'timestamps'}}
    d0 = cwt.Domain.from_dict(domain_data)
    v1 = cwt.Variable( "https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP//reanalysis/MERRA2/mon/atmos/tas.ncml", "tas", domain=d0)
    v1_ave_data = {'name': "xarray.ave", 'axes': "yx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)
    wps.execute(v1_ave, domains=[d0], async=True)
    dataPaths = wps.download_result(v1_ave, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_seasonal_anomaly(plot=False):
    d0 = cwt.Domain.from_dict({'id': 'd0', 'lat': {'start': 40, 'end': 40, 'crs': 'values'},
                               'lon': {'start': 260, 'end': 260, 'crs': 'values'},
                               'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z', 'crs': 'timestamps'}})
    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
    v0_ave_data = {'name': "xarray.ave", 'axes': "t", 'groupby': "t.season"}
    v0_ave = cwt.Process.from_dict(v0_ave_data)
    v0_ave.set_inputs(v0)
    anomaly = cwt.Process.from_dict({'name': "xarray.diff", "domain": "d0"})
    anomaly.set_inputs(v0_ave, v0)

    wps.execute(anomaly, domains=[d0], async=True)
    dataPaths = wps.download_result(anomaly, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_seasonal_cycle(plot=False):
    d0 = cwt.Domain.from_dict({'id': 'd0', 'lat': {'start': 40, 'end': 40, 'crs': 'values'},
                               'lon': {'start': 260, 'end': 260, 'crs': 'values'},
                               'time': {'start': '1980-01-01T00:00:00Z', 'end': '1992-12-31T23:59:00Z','crs': 'timestamps'}} )
    v0 = cwt.Variable("collection://cip_merra2_mth", "tas", domain=d0)
    v0_ave_data = {'name': "xarray.ave", 'axes': "t", 'groupby': "t.season"}
    v0_ave = cwt.Process.from_dict(v0_ave_data)
    v0_ave.set_inputs(v0)
    wps.execute(v0_ave, domains=[d0], async=True)
    dataPaths = wps.download_result(v0_ave, temp_dir, True)
    for dataPath in dataPaths:
        generate_output( dataPath, plot )

def test_KE_ave_conus_1y(plot=False):
    domain_data = {'id': 'd0', 'lat': {'start':229, 'end':279, 'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'}, 'time': {'start': '1980-01-01T00:00:00Z', 'end': '2015-12-31T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://merra2_inst1_2d_int_Nx", "KE", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

def test_KE_ave_global_1y(plot=False):
    #       domain_data = { 'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '2015-12-31T23:00:00', 'crs': 'timestamps'} }
    domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00Z', 'end': '1980-12-31T23:59:00Z', 'crs': 'timestamps'}}

    d0 = cwt.Domain.from_dict(domain_data)

    v1 = cwt.Variable("collection://cip_cfsr_mth", "tas", domain=d0)

    v1_ave_data = {'name': "xarray.ave", 'axes': "tyx"}
    v1_ave = cwt.Process.from_dict(v1_ave_data)
    v1_ave.set_inputs(v1)

    wps.execute(v1_ave, domains=[d0], async=True)

    dataPaths = wps.download_result(v1_ave, temp_dir, True)
    for dataPath in dataPaths:  generate_output( dataPath, plot )

if __name__ == '__main__':
#    test_binning()
    test_KE_ave_global_1y()