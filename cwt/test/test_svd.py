import cwt, os, time

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

def res( bounds, shape ):
    return ( bounds[1] - bounds[0] ) / float(shape)

class SVDTest:
    plotter = cwt.initialize()
    host = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )
    assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
    print "Connecting to wps host: " + host
    wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )
    temp_dir = create_tempdir()

    def __init__(self, _nModes ):
        self.nModes = _nModes

    def eofs( self, collection, variable, lat_bnds, lon_bnds, level, gridShape ):
        if lat_bnds is None: lat_bnds = [ -90, 90 ]
        if lon_bnds is None:
            domain = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":lat_bnds[0],"end":lat_bnds[1],"crs":"values"}, "level":{"start":level,"end":level,"crs":"values"}, "filter":month_filter } )
            gridRes = None if gridShape is None else [ res(lat_bounds,gridShape[0]), res([0,360],gridShape[1]) ]
        else:
            domain = cwt.Domain.from_dict( { 'id': 'd0', "lat":{"start":lat_bnds[0],"end":lat_bnds[1],"crs":"values"}, "lon":{"start":lon_bnds[0],"end":lon_bnds[1],"crs":"values"}, "level":{"start":level,"end":level,"crs":"values"}, "filter":month_filter } )
            gridRes = None if gridShape is None else [ res(lat_bounds,gridShape[0]), res(lon_bnds,gridShape[1]) ]

        if( gridShape is None ):
            svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":str(self.nModes), "domain":"d0", "compu":"true" } )
        else:
            svd =  cwt.Process.from_dict( { 'name': "SparkML.svd", "modes":str(self.nModes), "grid": "uniform", "shape": str(gridShape).strip('[]'), "res": str(gridRes).strip('[]'), "domain":"d0", "compu":"true" } )
        v0 = cwt.Variable("collection://" + collection, variable + ":P0", domain=domain  )
        svd.set_inputs( v0 )
        self.wps.execute( svd, domains=[domain], async=True )
        dataPaths = self.wps.download_result( svd, self.temp_dir )
        for dataPath in dataPaths:
            self.plotter.mpl_plot( dataPath, 0, True )

if __name__ == '__main__':
    variable = "zg"
    collection = "cip_20crv2c_mth"
    lat_bounds = [ -75, 75 ]
    lon_bounds = None
    level = 500   # hPa
    month_filter = "JJA"
    nModes =  8
    gridShape = [30,72]

    executor = SVDTest(nModes)
    executor.eofs( collection, variable, lat_bounds, lon_bounds, level, gridShape )

