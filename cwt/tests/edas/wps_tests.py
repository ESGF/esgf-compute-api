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

    def cfsr_mth_time_ave(self, lat_start, lat_end, wait = True ):
        t0 = time.time()
        domain_data = {'id': 'd0', 'lat': {"start":lat_start, "end":lat_end, "crs":"values"}, 'time': {'start': '1980-01-01T00:00:00', 'end': '2011-12-31T23:00:00', 'crs': 'timestamps'}}
        process_data = { 'name': 'edas.ave',  'input': [ 'v0' ],  'axes': "tz",  'domain': "d0",  'result': 'p0' }

        process  = cwt.Process.from_dict( process_data )
        variable = cwt.Variable( "collection://cip_cfsr_mth", 'tas', name='v0' )
        domain   = cwt.Domain.from_dict( domain_data )

        self.client.execute( process, inputs=[variable], domain=domain, method='get' )
        if wait:
            monitorExecution( process.context, download = True, filepath="/tmp/result-" + str(time.time()) + ".nc", sleepSecs=2 )
            print("\n Completed request in " + str(time.time() - t0) + " seconds \n")
        return process

    def metrics_test(self):
        process = cwt.Process( 'edas.metrics' )
        self.client.execute( process, method='get' )
        process.wait()
        output_content = json.loads(process.context.processOutputs[0].retrieveData())
        print (" METRICS: ")
        for k, v in output_content.items(): print (" * " + str(k) + ": " + str(v))

    def monitorExecution( self, processes, t0 = time.time() ):
        executions = [ process.context for process in processes ]
        while len(executions) > 0:
            time.sleep(0.2)
            for execution in executions:
                execution.checkStatus( sleepSecs=2 )
                if execution.isComplete():
                    if execution.isSucceded():
                        filepath = "/tmp/result-" + str(time.time()) + ".nc"
                        executions.remove(execution)
                        print("\n Completed request in " + str(time.time() - t0) + " seconds, downloading result to " + filepath + "\n")
                        execution.getOutput(filepath=filepath)
                        for output in execution.processOutputs:
                            if output.reference is not None:
                                print( 'Output URL=%s' % output.reference )
                    else:
                        for ex in execution.errors:
                            print('Error: code=%s, locator=%s, text=%s' % (ex.code, ex.locator, ex.text))

if __name__ == '__main__':
    concurrent = False
    tester = wpsTest()
    t0 = time.time()
    if concurrent:
        p0 = tester.cfsr_mth_time_ave( -80, 0,  False )
        p1 = tester.cfsr_mth_time_ave(   0, 80, False )
        tester.monitorExecution( [ p0, p1 ], t0 )
    else:
        p0 = tester.cfsr_mth_time_ave(-80, 0, True)