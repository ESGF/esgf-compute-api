import cwt, os

class DemoWorkflow:

    def run( self ):

        VALUES = cwt.CRS('values')
        INDICES = cwt.CRS('indices')

        time = cwt.Dimension( "time", 0, 100, INDICES )
        d0 = cwt.Domain( [time], name='d0' )

        op1 = cwt.Operation.from_dict( { 'name': 'CDSpark.max', 'axes': "xy" } )
        op1.add_input( cwt.Variable('file:///dass/nobackup/tpmaxwel/.edas/cache/collections/NCML/CIP_MERRA2_6hr_tas.ncml', 'tas', domains=[d0] ) )

        wps = cwt.WPS( 'http://localhost:9001/wps', log=True, log_file=os.path.expanduser("~/esgf_api.log") )
        wps.init()

        process = esgf.Process( wps, op1 )
        process.execute( None, d0, [], True, True, "GET")

        print "Results:"
        for output in process._result.processOutputs:
            if output.reference:     print "  >> Reference: "  + output.reference
            if output.mimeType:      print "  >> MimeType: "  + output.mimeType


executor = DemoWorkflow()

executor.run()