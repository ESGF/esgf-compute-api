import cwt, os, logging, time, json
from cwt.wps import monitorExecution

TAS = [
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_185001-190012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_190101-195012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_195101-200012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_200101-201412.nc',
]

TAS_ESGF= [
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_185001-190012.nc'
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_190101-195012.nc',
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_195101-200512.nc',
]

SERVER = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )

class wpsTest:

    def __init__(self):
        self.client = cwt.WPSClient(SERVER)
        print "Connecting to wps host: " + SERVER

    def cfsr_mth_time_ave(self, lat_start, lat_end ):

        domain_data = {'id': 'd0', 'lat': {"start":lat_start, "end":lat_end, "crs":"values"}, 'time': {'start': '1980-01-01T00:00:00', 'end': '2011-12-31T23:00:00', 'crs': 'timestamps'}}
        process_data = { 'name': 'edas.ave',  'input': [ 'v0' ],  'axes': "t",  'domain': "d0",  'result': 'p0' }

        process  = cwt.Process.from_dict( process_data )
        variable = cwt.Variable( "collection://cip_cfsr_mth", 'ta', name='v0' )
        domain   = cwt.Domain.from_dict( domain_data )

        self.client.execute( process, inputs=[variable], domain=domain, method='get' )
        monitorExecution( process.context, download = True, filepath="/tmp/result-" + str(time.time()) + ".nc" )

    def metrics_test(self):
        process = cwt.Process( 'edas.metrics' )
        self.client.execute( process, method='get' )
        process.wait()
        output_content = json.loads(process.context.processOutputs[0].retrieveData())
        print (" METRICS: ")
        for k, v in output_content.items(): print (" * " + str(k) + ": " + str(v))


if __name__ == '__main__':
    tester = wpsTest()

    t1 = time.time()
    tester.cfsr_mth_time_ave(-80,0)
    print("\n Completed request1 in " + str(time.time() - t1) + " seconds \n")

    t2 = time.time()
    tester.cfsr_mth_time_ave(0,80)
    print("\n Completed request2 in " + str(time.time() - t2) + " seconds \n")