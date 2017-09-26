import cwt, os

#host = 'http://localhost:9000/wps/cwt'
host = 'https://dptomcat03-int/wps/cwt'

class TestWorkflow:

    def run( self ):
        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mon_tas", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.average", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
        wps.execute( op, domain=d0, async=True )
        print str( op.response )

        wps.status( op )
        print str( op.status )

executor = TestWorkflow()
executor.run()