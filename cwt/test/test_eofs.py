import cdms2 as cdms
import cdutil
import cdtime, math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.dates as mdates
from cwt.plotters import PlotMgr
from pyedas.eofs.cdms import Eof
import vcs, EzTemplate
import string
import numpy as np

def plot_eofs( eofs, nMode, experiment_title, pve ):
    canvas = vcs.init(geometry=(1400,1000))
    canvas.open()
    canvas.setcolormap('bl_to_darkred')
    M=EzTemplate.Multi(rows=nMode/2,columns=2)
    M.margins.top=0.1
    M.margins.bottom=0.05
    M.spacing.horizontal=.05
    M.spacing.vertical=.05

    for iPlot in range( nMode ):
        iso = canvas.createisofill()
        level_distribution = np.array( [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] )
        iso.levels = list( level_distribution*0.007 )
        iso.ext_1 = 'y' # control colorbar edge (arrow extention on/off)
        iso.ext_2 = 'y' # control colorbar edge (arrow extention on/off)
        cols = vcs.getcolors(iso.levels, range(16,240), split=0)
        iso.fillareacolors = cols
        iso.missing = 0
        variable = eofs[iPlot]
        percentage = str(round(float(pve[iPlot]*100.),1)) + '%'
        plot_title_str = 'EOF mode ' + str(iPlot) + ',' + experiment_title +  ', ' + percentage

        p = vcs.createprojection()
        p.type = 'robinson'
        iso.projection = p
        t=M.get( legend='local' )
        variable.setattribute( "long_name", plot_title_str )
        canvas.plot(variable,iso,t)
        canvas.png('/tmp/eof_analysis-mode{0}.png'.format(iPlot))

    canvas.interact()



data_path_ts = 'https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP/Reanalysis/NASA-GMAO/GEOS-5/MERRA/mon/atmos/ts.ncml'
data_path_zg = 'https://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP/Reanalysis/NASA-GMAO/GEOS-5/MERRA/mon/atmos/zg.ncml'
outDir = "/tmp/"

data_path = data_path_zg

f = cdms.open(data_path)

start_year = 1980
end_year = 2000
nModes = 4
experiment = 'MERRA2-TS('+str(start_year)+'-'+str(end_year)+')'
display_eofs = True

scale = True
start_time = cdtime.comptime(start_year)
end_time = cdtime.comptime(end_year)

# d = f('ts',time=(start_time,end_time),longitude=(120,290),latitude=(-50,50))
# d = f('ts',time=(start_time,end_time),latitude=(-80,80))  # type: cdms.AbstractVariable
d = f('zg',latitude=(-80,80), level=(500,500) )  # type: cdms.AbstractVariable
print "Completed data read"

d_anom = cdutil.ANNUALCYCLE.departures(d)
print "Completed data prep"

solver = Eof( d_anom, weights='none', center=True, scale=True )
print "Created solver"

eof = solver.eofs( neofs=nModes )
pcs = solver.pcs().transpose()
print "Computed eofs"

frac = solver.varianceFraction()

if display_eofs:
    plot_eofs( eof, nModes, experiment, frac )

outfilePath = outDir + experiment + '-PCs.nc'
outfile = cdms.open(outfilePath,'w')
timeAxis = d.getTime()

for iPlot in range(nModes):
    pc = pcs[iPlot]  # type: cdms.Variable
    pve = str(round(float(frac[iPlot]*100.),1)) + '%'
    plot_title_str = 'PC-' + str(iPlot) + ',' + experiment +  ', ' + pve
    v = cdms.createVariable( pc.data, None, 0, 0, None, float('nan'), None, [timeAxis],  {"pve":pve, "long_name": plot_title_str }, "PC-" + str(iPlot) )
    outfile.write(v)
outfile.close()





