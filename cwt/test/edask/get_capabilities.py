import cwt, os, time
import numpy as np

plotter = cwt.initialize()
# host = os.environ.get("EDAS_HOST_ADDRESS", "https://edas.nccs.nasa.gov/wps/cwt")
host = "https://edas.nccs.nasa.gov/wps/cwt"
assert host != None, "Must set EDAS_HOST_ADDRESS environment variable"
print "Connecting to wps host: " + host
wps = cwt.WPS(host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False)

# print "\nKERNELS:\n"
# print wps.getCapabilities("", False)

print "\nCOLLECTIONS:\n"
print wps.getCapabilities("coll", False)

#print "\nVARIABLE:\n"
#print wps.getCapabilities("var|cip_cfsr_mon_1980-1995|tas", False)