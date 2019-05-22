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

    def cfsr_mth_time_ave(self):

        domain_data = {'id': 'd0', 'time': {'start': '1980-01-01T00:00:00', 'end': '1980-12-31T23:00:00', 'crs': 'timestamps'}}
        process_data = { 'name': 'edas.ave',  'input': [ 'v0' ],  'axes': "t",  'domain': "d0",  'result': 'p0' }

        process  = cwt.Process.from_dict( process_data )
        variable = cwt.Variable( "collection://cip_cfsr_mth", 'tas', name='v0' )
        domain   = cwt.Domain.from_dict( domain_data )

        self.client.execute( process, inputs=[variable], domain=domain, method='get' )
        monitorExecution( process.context, download = True, filepath="/tmp/result-" + str(time.time()) + ".nc" )

    def metrics_test(self):
        process = cwt.Process( 'edas.metrics' )
        self.client.execute( process, method='get' )
        self.monitorExecution( process.context )

    def monitorExecution(execution, download=False):
        print 'Monitoring Execution'
        while execution.isComplete() is False:
            execution.checkStatus(sleepSecs=3)
            print 'Execution status: %s' % execution.status

        if execution.isSucceded():
            if download:
                filePath = "/tmp/result-" + str(time.time()) + ".txt"
                execution.getOutput(filepath=filePath)
                metrics = json.loads(open(filePath, "r").read())
                print "METRICS: "
                for k, v in metrics.items(): print (" * " + str(k) + " = " + str(v))
            else:
                print 'Execution succeeded, nOutputs: ' + str(len(execution.processOutputs))
                for output in execution.processOutputs:
                    print 'Output: %s' % str(output)
                    if output.reference is not None:
                        print 'Output URL=%s' % output.reference
        else:
            for ex in execution.errors:
                print 'Error: code=%s, locator=%s, text=%s' % (ex.code, ex.locator, ex.text)

if __name__ == '__main__':
    tester = wpsTest()
    tester.metrics_test()