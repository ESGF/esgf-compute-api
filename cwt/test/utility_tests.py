import cwt, os, time

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

class UtilityTests:
    plotter = cwt.initialize()
    host = "https://edas.nccs.nasa.gov/wps/cwt"
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def test_dataset( self ):
        domain_data = { 'id': 'd0' }
        d0 = cwt.Domain.from_dict(domain_data)
        op_data =  { 'name': "util.testDataset", "domain": "d0", "mode": "ave" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        start = time.time()
        self.wps.execute( op, domains=[d0] )

        dataPath = self.wps.download_result( op, self.temp_dir )
        self.plotter.print_Mdata(dataPath)

        end = time.time()
        print "\nCompleted execution in " + str(end-start) + " secs\n"


executor = UtilityTests()
executor.test_dataset()


