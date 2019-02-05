import cdms2 as cdms
import cdutil
import cdtime
from cwt.plotters import PlotMgr
import vcs
import string
import numpy as np

#===========================================================================================================
# DATA
#-----------------------------------------------------------------------------------------------------------
# Open file ---
# data_path = 'https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP/Reanalysis/NASA-GMAO/GEOS-5/MERRA/mon/atmos/ts.ncml'

data_path = '/dass/pubrepo/CREATE-IP/data/reanalysis/NASA-GMAO/GEOS-5/MERRA2/mon/atmos/ts/ts_Amon_reanalysis_MERRA2_198001-201712.nc'
f = cdms.open(data_path)

start_year = 1980
end_year = 2000

start_time = cdtime.comptime(start_year)
end_time = cdtime.comptime(end_year)

d = f('ts',time=(start_time,end_time),latitude=(40,40),longitude=(40,40))
print "Completed data read"

d_anom = cdutil.ANNUALCYCLE.departures(d).squeeze()
print "Completed data prep"

plotter = PlotMgr()
plotter.graph_data( d_anom.data, "MERRA2 TS(40,40)[1980-2000]: Seasonal Cycle Removed" )