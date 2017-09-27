import cwt, os
from cwt.wps_lib import operations
from cwt.wps_lib.operations import ExecuteResponse


host = 'http://localhost:9001/cwt'
#host = 'https://dptomcat03-int/wps/cwt'

class TestWorkflow:

    def run( self ):
        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'level': {'start':5, 'end':5, 'crs':'indices'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mon_ta", "ta", domain="d0" )

        op_data =  { 'name': "CDSpark.average", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
        wps.execute( op, domain=d0, async=True )
        response = op.response    # """:type : ExecuteResponse

        print str( response.xml(True) )

executor = TestWorkflow()
executor.run()