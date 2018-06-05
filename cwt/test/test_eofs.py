import cdms2 as cdms
import cdutil
import cdtime
from eofs.cdms import Eof
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
nModes = 1

start_time = cdtime.comptime(start_year)
end_time = cdtime.comptime(end_year)

d = f('ts',time=(start_time,end_time),longitude=(120,290),latitude=(-50,50))
# d = f('ts',time=(start_time,end_time),latitude=(-80,80))
print "Completed data read"

d_anom = cdutil.ANNUALCYCLE.departures(d)
d_anom_center = d_anom - d_anom.mean(axis=0)
d_anom_center_scaled = d_anom_center / d_anom_center.std(axis=0)
print "Completed data prep"

solver = Eof( d_anom_center_scaled, weights='none', center=False )
print "Created solver"

eof = solver.eofs( neofs=nModes )
print "Computed eofs"

frac = solver.varianceFraction()
eof = eof * -1

#========================================== PLOT =================================================================

canvas = vcs.init(geometry=(900,800))

canvas.open()
template = canvas.createtemplate()
template.blank(['title','mean','min','max','dataname','crdate','crtime','units','zvalue','tvalue','xunits','yunits','xname','yname'])
canvas.setcolormap('bl_to_darkred')

for iPlot in range(nModes):
    iso = canvas.createisofill()
    level_distribution = np.array( [-1.6, -1.3, -1.0, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.3, 1.6] )
    iso.levels = list( level_distribution*0.01 )
    iso.ext_1 = 'y' # control colorbar edge (arrow extention on/off)
    iso.ext_2 = 'y' # control colorbar edge (arrow extention on/off)
    cols = vcs.getcolors(iso.levels, range(16,240), split=0)
    iso.fillareacolors = cols
    iso.missing = 0

    p = vcs.createprojection()
    p.type = 'robinson'
    iso.projection = p

    canvas.plot(eof[iPlot],iso,template)

    plot_title = vcs.createtext()
    plot_title.x = .5
    plot_title.y = .97
    plot_title.height = 23
    plot_title.halign = 'center'
    plot_title.valign = 'top'
    plot_title.color='black'
    percentage = str(round(float(frac[iPlot]*100.),1)) + '%'
    plot_title.string = 'EOF mode ' + str(iPlot) + ', MERRA2 TS('+str(start_year)+'-'+str(end_year)+'), '+percentage
    canvas.plot(plot_title)
    canvas.png('/tmp/eof_analysis-mode{0}.png'.format(iPlot))
    canvas.clear()

