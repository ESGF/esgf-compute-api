import cwt, os, time, cdms2


def create_tempdir():
    temp_dir = os.path.expanduser("~/.edas")
    try:
        os.makedirs(temp_dir, 0755)
    except Exception:
        pass
    return temp_dir


def print_Mdata(dataPath):
    for k in range(0, 30):
        if (os.path.isfile(dataPath)):
            f = cdms2.openDataset(dataPath)
            for variable in f.variables.values():
                try:
                    print "Produced result " + variable.id + ", shape: " + str(
                        variable.shape) + ", dims: " + variable.getOrder() + " from file: " + dataPath
                    print "Data: " + str(variable.getValue())
                except Exception as err:
                    print " Error printing data: " + getattr(err, "message", repr(err))
                return
        else:
            time.sleep(1)


def init_wps():
    host = os.environ.get("EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt")
    assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
    print "Connecting to wps host: " + host
    return cwt.WPS(host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False)


domain_data = {'id': 'd0', 'lat': {'start': 23.7, 'end': 49.2, 'crs': 'values'},
               'lon': {'start': -125, 'end': -70.3, 'crs': 'values'},
               'time': {'start': '1980-01-01T00:00:00', 'end': '1990-12-31T23:00:00', 'crs': 'timestamps'}}

cwt.initialize()
wps = init_wps()
temp_dir = create_tempdir()
d0 = cwt.Domain.from_dict(domain_data)
inputs = cwt.Variable("collection://cip_cfsr_mth", "tas", domain=d0)
op_data = {'name': "xarray.ave", 'axes': "t"}
op = cwt.Process.from_dict(op_data)
op.set_inputs(inputs)
wps.execute(op, domains=[d0])
dataPaths = wps.download_result(op, temp_dir, True)
for dataPath in dataPaths: print_Mdata(dataPath)
