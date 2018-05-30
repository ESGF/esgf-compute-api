import cwt, os

# datainputs = """[domain=[{"name":"d0","lat":{"start":70,"end":90,"system":"values"},"lon":{"start":5,"end":45,"system":"values"}}],
# variable=[{"uri":"file:///dass/nobackup/tpmaxwel/.edas/cache/collections/NCML/MERRA_TAS1hr.ncml","name":"tas:v1","domain":"d0"}],
# operation=[{"name":"CDSpark.average","input":"v1","domain":"d0","axes":"xy"}]]"""

#class TestWorkflow:
#
#    def run( self ):
#        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'} }
#        d0 = cwt.Domain.from_dict(domain_data)
#
#        inputs = cwt.Variable("file:///dass/nobackup/tpmaxwel/.edas/cache/collections/NCML/MERRA_TAS1hr.ncml", "tas", domain="d0", axes="xy" )
#
#        op =  cwt.Process.from_dict( { 'name': "CDSpark.average" } )
#        op.add_inputs( inputs )
#
#        wps = cwt.WPSClient( 'http://localhost:9000/wps', log=True, log_file=os.path.expanduser("~/esgf_api.log") )
#        wps.execute( op, domain=d0, method="GET" )
#
#executor = TestWorkflow()
#executor.run()
