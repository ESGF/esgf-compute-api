import cwt, os

class DemoWorkflow:

    def run( self ):

        wps = cwt.WPS( 'http://localhost:9000/wps', log=True, log_file=os.path.expanduser("~/esgf_api.log") )
        wps.init()

        capabilities = wps.capabilities

        print "Capabilities: " + capabilities

executor = DemoWorkflow()

executor.run()