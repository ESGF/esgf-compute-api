import cwt, os, time
# import logging, cdms2, vcs
# from cwt.test.plotters import PlotMgr
# import cdms2, datetime, matplotlib, urllib3
# import matplotlib.pyplot as plt
# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

class TestWorkflow:
    plotter = cwt.initialize()
    host = "https://edas.nccs.nasa.gov/wps/cwt"
#    host ="https://dptomcat03-int/wps/cwt"
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def conus_KE_ave_1month( self ):
        domain_data = { 'id': 'd0', 'lat':{'start':229,'end':279,'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'},'time':{'start':'1980-01-01T00:00:00','end':'1980-01-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def global_KE_ave_1month( self ):
        domain_data = { 'id': 'd0','time':{'start':'1980-01-01T00:00:00','end':'1980-01-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection:/merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def conus_KE_ave_1year( self ):
        domain_data = { 'id': 'd0', 'lat':{'start':229,'end':279,'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'},'time':{'start':'1980-01-01T00:00:00','end':'1980-12-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def global_KE_ave_1year( self ):
        domain_data = { 'id': 'd0','time':{'start':'1980-01-01T00:00:00','end':'1980-12-31T23:00:00','crs':'timestamps'}}
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection:/merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def global_KE_ave_35years( self ):
        domain_data = { 'id': 'd0','time':{'start':'1980-01-01T00:00:00','end':'2014-12-31T23:00:00','crs':'timestamps'} }
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def conus_KE_ave_35years( self ):
        domain_data = { 'id': 'd0', 'lat':{'start':229,'end':279,'crs':'indices'}, 'lon': {'start':88, 'end':181, 'crs':'indices'},'time':{'start':'1980-01-01T00:00:00','end':'2014-12-31T23:00:00','crs':'timestamps'} }
        d0 = cwt.Domain.from_dict(domain_data)
        inputs = cwt.Variable("collection://merrra2_m2i1nxint","KE",domain="d0" )
        op_data =  { 'name': "CDSpark.ave", 'axes':"tyx" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        start = time.time()
        self.wps.execute( op, domains=[d0], async=False )
        dataPath = self.wps.download_result(op, self.temp_dir)
        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"

        self.plotter.print_data(dataPath)

    def test_plot(self):
        self.plotter.mpl_timeplot("/tmp/testData.nc")

    def ListKernels(self):
        print self.wps.getCapabilities( "", False )

    def ListCollections(self):
        print self.wps.getCapabilities( "coll", False )

executor = TestWorkflow()
executor.conus_KE_ave_35years()
# executor.conus_KE_ave_1month()


