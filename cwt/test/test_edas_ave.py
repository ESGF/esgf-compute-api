import cwt, os

class TestWorkflow:

    plotter = cwt.initialize()
    host ="https://edas.nccs.nasa.gov/wps/cwt"
    wps = cwt.WPS( host, log=True,log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

    def spatial_ave( self ):

# Set the domain to be the continental United States, from 1980 to 2016

#        domain_data = { 'id': 'd0', 'lat': {'start':23.7, 'end':49.2,'crs':'values'},
#                      'lon': {'start':-125, 'end':-70.3, 'crs':'values'},
#                       'time':{'start':'1980-01-01T00:00:00', 'end':'2016-12-31T23:00:00', 'crs':'timestamps'}}

# Set the domain to the ABoVE Study Domain, from 1980 to 2016

        domain_data = { 'id': 'd0', 'lat': {'start':51, 'end':75,'crs':'values'},
                       'lon': {'start':-168, 'end':-99, 'crs':'values'},
                       'time':{'start':'1980-01-01T00:00:00', 'end':'2016-12-31T23:00:00', 'crs':'timestamps'}}

        d0 = cwt.Domain.from_dict(domain_data)

# Set the input data to be monthly CFSR Cloud Cover data (variable clt)

        inputs = cwt.Variable("collection://cip_cfsr_mth", "clt", domain="d0" )

# Set the operation to be "average", operating over the time axis

        op_data =  { 'name': "CDSpark.ave", "weights":"cosine", 'axes': "t" }

        op =  cwt.Process.from_dict( op_data )
        op.set_inputs( inputs )

        self.wps.execute( op, domains=[d0], async=True )
        dataPaths = self.wps.download_result(op)

# Plot average cloud cover over the spatial range plot

        for dataPath in dataPaths:
            self.plotter.mpl_spaceplot(dataPath)

executor = TestWorkflow()
executor.spatial_ave()
