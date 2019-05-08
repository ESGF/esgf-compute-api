import cwt, os, logging, time, socket

TAS = [
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_185001-190012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_190101-195012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_195101-200012.nc',
    'https://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NASA-GISS/GISS-E2-1-G/amip/r1i1p1f1/Amon/tas/gn/v20181016/tas_Amon_GISS-E2-1-G_amip_r1i1p1f1_gn_200101-201412.nc',
]

TAS_ESGF= [
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_185001-190012.nc'
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_190101-195012.nc',
    'esgf@https://dataserver.nccs.nasa.gov/thredds/dodsC/CMIP5/NASA/GISS/historical/E2-H_historical_r2i1p3/clwvi_Amon_GISS-E2-H_historical_r2i1p3_195101-200512.nc',
]

SERVER = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )



class wpsTest:

    def __init__(self):
        self.client = cwt.WPSClient(SERVER)
        print "Connecting to wps host: " + SERVER

    def cfsr_mth_time_ave(self):

        domain_data = {'id': 'd0', 'lat': {'start': 23.7, 'end': 49.2, 'crs': 'values'},  'lon': {'start': -125, 'end': -70.3, 'crs': 'values'},
                       'time': {'start': '1980-01-01T00:00:00', 'end': '2016-12-31T23:00:00', 'crs': 'timestamps'}}

        process_data = { 'name': 'edas.ave',  'input': [ 'v0' ],  'axes': "t",  'domain': "d0",  'result': 'p0' }

        process  = cwt.Process.from_dict( process_data )
        variable = cwt.Variable( "collection://cip_cfsr_mth", 'tas', name='v0' )
        domain   = cwt.Domain.from_dict( domain_data )

        self.client.execute( process, inputs=[variable], domain=domain, method='get' )
        process.wait()

        print "Completed execution, result available at: " + process.output.uri

    @staticmethod
    def configure():
        print "Configuring logging"
        owslog = logging.getLogger('owslib')
        LOG_DIR = os.path.expanduser("~/.edas/logs")
        if not os.path.exists(LOG_DIR):  os.makedirs(LOG_DIR)
        timestamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime())
        fh = logging.FileHandler("{}/ows-wps-{}-{}.log".format(LOG_DIR, socket.gethostname(), timestamp))
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('ows-wps-%(asctime)s-%(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        owslog.addHandler(fh)
        owslog.addHandler(ch)

if __name__ == '__main__':
    wpsTest.configure()
    tester = wpsTest()
    tester.cfsr_mth_time_ave()