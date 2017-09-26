import cwt, os, time
import logging

# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'
host ="https://dptomcat03-int/wps/cwt"

class TestWorkflow:

    def run( self ):
        logger = logging.getLogger('cwt.wps')
        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mon_tas", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.average", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
        wps.execute( op, domain=d0, async=True )

        result_file = wps.download_result(op)
        logger.info( "result_file: " +  result_file )

        # logger.info( "STATUS: " +  op.status )
        #
        # while op.processing:
        #     logger.info( "STATUS: " +  op.status )
        #     time.sleep(1)
        #
        # logger.info( "STATUS: " +  op.status )
        # logger.info( "STATUS LOC: " +  op.status_location )

#        logger.info( "RESPONSE: " + str( op.response ) )
#        logger.info( "OUTPUT: " + str( op.response.output ) )

#        wps.status( op, "test" )
#        print str( op.status )

executor = TestWorkflow()
executor.run()