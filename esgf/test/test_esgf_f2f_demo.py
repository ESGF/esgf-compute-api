import esgf, os

class DemoWorkflow:

    def run( self ):

#        lat = esgf.Dimension(20, 60, esgf.Dimension.values, name="lat" )
#        lon = esgf.Dimension(200, 300, esgf.Dimension.values, name="lon"  )
#        time = esgf.Dimension( 0, 100, esgf.Dimension.values, name="time"  )
        d0 = esgf.Domain( [], name='d0' )

        op1 = esgf.Operation.from_dict( { 'name': 'CDSpark.multiAverage' } )
        for index in range(1,4): op1.add_input( esgf.Variable('collection:/GISS_r%di1p1'%(index), 'tas', domains=[d0] ) )

        op3 = esgf.Operation.from_dict( { 'name': 'CDSpark.regrid', 'crs':'gaussian~128' } )
        op3.add_input( op1 )

        op2 = esgf.Operation.from_dict( { 'name': 'CDSpark.multiAverage' } )
        for index in range(1,4): op2.add_input( esgf.Variable('collection:/GISS-E2-R_r%di1p1'%(index), 'tas', domains=[d0] ) )

        op4 = esgf.Operation.from_dict( { 'name': 'CDSpark.regrid', 'crs':'gaussian~128'  } )
        op4.add_input( op2 )

        op5 = esgf.Operation.from_dict( { 'name': 'CDSpark.multiAverage' } )
        op5.add_input( op3 )
        op5.add_input( op4 )

        wps = esgf.WPS( 'http://localhost:9001/wps', log=True, log_file=os.path.expanduser("~/esgf_api.log") )
        wps.init()

        process = esgf.Process( wps, op5 )
        process.execute( None, d0, [], True, True, "GET")

        print "Results:"
        for output in process._result.processOutputs:
            if output.reference:     print "  >> Reference: "  output.reference
            if output.mimeType:      print "  >> MimeType: "  output.mimeType


executor = DemoWorkflow()

executor.run()
