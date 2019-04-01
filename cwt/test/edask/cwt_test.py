import cwt, os, time, cdms2, xml

def create_tempdir():
    temp_dir = os.path.expanduser( "~/.edas" )
    try: os.makedirs( temp_dir, 0755 )
    except Exception: pass
    return temp_dir

def print_Mdata( dataPath ):
    for k in range(0,30):
        if( os.path.isfile(dataPath) ):
            f = cdms2.openDataset(dataPath)
            for variable in f.variables.values():
                try:
                    print "Produced result " + variable.id + ", shape: " +  str( variable.shape ) + ", dims: " + variable.getOrder() + " from file: " + dataPath
                    print "Data: " + str( variable.getValue() )
                except Exception as err:
                    print " Error printing data: " + getattr( err, "message", repr(err) )
                return
        else: time.sleep(1)

def init_wps():
    host = os.environ.get( "EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt" )
    assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
    print "Connecting to wps host: " + host
    return cwt.WPSClient( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

def extractErrorReport(response):
    bracketingText = "wps:ProcessFinished"
    beginIndex = response.find(bracketingText, 0) + len(bracketingText)
    endIndex = response.find("wps:ProcessFinished", beginIndex)
    raw_report = response[beginIndex:endIndex]
    repl_map = {"&amp;": "&", "&quot;": '"', "&lt;": "<", "&gt;": ">"}
    for key, value in repl_map.items(): raw_report = raw_report.replace(key, value)
    return raw_report


def hasNode( parent_node, child_node_name, schema="wps" ):
    if schema == "wps":
        schemaLocation = "{http://www.opengis.net/wps/1.0.0}"
    elif schema == "ows":
        schemaLocation = "{http://www.opengis.net/ows/1.1}"
    else:
        schemaLocation = ""
    for ref in parent_node.iter(schemaLocation + child_node_name): return True
    return False

def status( process ):
    href = process.hrefs.get("status")
    toks = href.split('?')
    url = toks[0]
    parm_toks = toks[1].split('=')
    params = { parm_toks[0]: parm_toks[1] }
    headers = {}
    response = wps.__http_request("get", url, params, None, headers)
    message = response
    process.response = xml.etree.ElementTree.fromstring( response )
    status = "UNKNOWN"
    if   hasNode( process.response, "ProcessAccepted" ): status = "QUEUED"
    elif hasNode( process.response, "ProcessStarted" ): status = "EXECUTING"
    elif hasNode( process.response, "ProcessFinished" ):
        status = "COMPLETED"
        print( "RECEIVED COMPLETION REPORT: " + response )
    elif hasNode( process.response, "ProcessFailed" ):
        status = "ERROR"
        message = extractErrorReport( response )
    return status, message

def download_result( op, temp_dir=os.getenv( "ESGF_CWT_CACHE_DIR", "/tmp" ), raiseErrors=False ):
    status, message = status( op )
    print( "*STATUS: " +  status )
    while status == "QUEUED" or status == "EXECUTING":
        time.sleep(1)
        status, message = status( op )
        print( "*STATUS: " +  status )
    if status == "ERROR":
        msg_toks = message.split(">~>")
        print "\n\n\n ------------------------------------------------------------------------------------------------------------------------------"
        print " *** Remote execution error: " + message
        print "\n ------------------>>" + msg_toks[0]
        if raiseErrors: raise Exception( msg_toks[0] )
        return []
    elif status == "COMPLETED":
        print "HREFS: " + str( op.hrefs )
        file_href = op.hrefs.get("file")
        file_path = temp_dir + "/" + file_href.split('=')[ -1 ]

        downloaded_files = []
        nFiles = 1000
        for fileIndex in range(1000):
            if( fileIndex >= nFiles ): break
            downloaded_file = downloadFile( file_href, file_path, fileIndex )
            if( downloaded_file == None ): break
            if(fileIndex == 0):
                f = cdms2.openDataset(downloaded_file)
                nFiles = int( f.attributes.get( "nFiles", 1 ) )
            downloaded_files += [ downloaded_file ]

        return downloaded_files

domain_data = {'id': 'd0', 'lat': {'start': 23.7, 'end': 49.2, 'crs': 'values'},
               'lon': {'start': -125, 'end': -70.3, 'crs': 'values'},
               'time': {'start': '1980-01-01T00:00:00', 'end': '1990-12-31T23:00:00', 'crs': 'timestamps'}}

wps = init_wps()
temp_dir = create_tempdir()
d0 = cwt.Domain.from_dict(domain_data)
inputs = cwt.Variable("collection://cip_cfsr_mth", "tas", domain=d0)
op_data = { 'name': 'xarray.ave', 'axes':'t', 'input':'tas', 'result':'tave' }
op = cwt.Process.from_dict(op_data)
op.set_inputs(inputs)
wps.execute(op, domains=[d0])
dataPaths = download_result(op, temp_dir, True)
for dataPath in dataPaths: print_Mdata(dataPath)

