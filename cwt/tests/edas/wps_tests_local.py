import cwt, os, logging, time, json

class TestDataManager:
    CreateIPServer = "https://dataserver.nccs.nasa.gov//thredds/dodsC/bypass/CREATE-IP"

    addresses = {
        "merra2": CreateIPServer + "/reanalysis/MERRA2/mon/atmos/{}.ncml",
        "merra2-day": CreateIPServer + "/reanalysis/MERRA2/day/atmos/{}.ncml",
        "merra2-6hr": CreateIPServer + "/reanalysis/MERRA2/6hr/atmos/{}.ncml",
        "merra": CreateIPServer + "/reanalysis/MERRA/mon/atmos/{}.ncml",
        "ecmwf": CreateIPServer + "/reanalysis/ECMWF/mon/atmos/{}.ncml",
        "cfsr": CreateIPServer + "/reanalysis/CFSR/mon/atmos/{}.ncml",
        "20crv": CreateIPServer + "/reanalysis/20CRv2c/mon/atmos/{}.ncml",
        "jra": CreateIPServer + "/reanalysis/JMA/JRA-55/mon/atmos/{}.ncml",
    }

    @classmethod
    def getAddress(cls, model, varName):
        return cls.addresses[model.lower()].format(varName)

SERVER = "http://localhost:5000/ows_wps/cwt"

class wpsTest:

    def __init__(self):
        self.client = cwt.WPSClient(SERVER)
        self.dataMgr = TestDataManager()
        print( "Connecting to wps host: " + SERVER )

    def cfsr_mth_time_ave(self, nyears, lat_start, lat_end, wait = True ):
        t0 = time.time()
        domain_data = {'id': 'd0', 'lat': {"start":lat_start, "end":lat_end, "crs":"values"}, 'time': {'start': '1980-01-01T00:00:00', 'end': '{}-12-31T23:00:00'.format(1980+nyears-1), 'crs': 'timestamps'}}
        process_data = { 'name': 'edas.ave',  'input': [ 'v0' ],  'axes': "t",  'domain': "d0",  'result': 'p0' }

        process  = cwt.Process.from_dict( process_data )
        variable = cwt.Variable( self.dataMgr.getAddress("merra2","tas"), 'tas', name='v0' )
        domain   = cwt.Domain.from_dict( domain_data )

        self.client.execute( process, inputs=[variable], domain=domain, method='get' )
        if wait:
            self.monitorExecution( [process] )
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
                        print("\n Completed requests in " + str(time.time() - t0) + " seconds, downloading result to " + filepath + "\n")
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
    p0 = tester.cfsr_mth_time_ave( 1, -80, 0,  True )
#    p1 = tester.cfsr_mth_time_ave( 1,  0, 80,  not concurrent )
#    if concurrent: tester.monitorExecution( [ p0, p1 ], t0 )