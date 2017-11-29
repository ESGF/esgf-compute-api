import logging
import cdms2, datetime, matplotlib, urllib3
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')

    def mpl_timeplot( self, dataPath ):
        if dataPath:
            self.logger.info( "Plotting file: " +  dataPath )
            f = cdms2.openDataset(dataPath)
            varName = f.variables.values()[0].id
            timeSeries = f( varName, squeeze=1 )
            datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in timeSeries.getTime().asComponentTime()]
            dates = matplotlib.dates.date2num(datetimes)
            fig, ax = plt.subplots()
            ax.plot(dates, timeSeries.data )
            ax.xaxis.set_major_formatter( mdates.DateFormatter('%b %Y') )
            ax.grid(True)
            fig.autofmt_xdate()
            plt.show()

    def mpl_spaceplot( self, dataPath, timeIndex=0 ):
        if dataPath:
            self.logger.info( "Plotting file: " +  dataPath )
            f = cdms2.openDataset(dataPath)
            lons = f.getAxis('lon')
            lats = f.getAxis('lat')
            lons2 = lons[:]
            lats2 = lats[:]
            m = Basemap(llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[len(lons)-1], urcrnrlat=lats[len(lats)-1], epsg='4326', lat_0 = lats2.mean(), lon_0 = lons2.mean())
            varName = f.variables.values()[0].id
            spatialData = f( varName, time=slice(timeIndex,timeIndex+1), squeeze=1)
            fig, ax = plt.subplots()
            lon, lat = np.meshgrid(lons2, lats2)
            xi, yi = m(lon, lat)
            cs2 = m.pcolormesh(xi, yi, spatialData, cmap='jet')
            # draw parallels
            lats_space = abs(lats[0])+abs(lats[len(lats)-1])
            m.drawparallels(np.arange(lats[0],lats[len(lats)-1], round(lats_space/5, 0)), labels=[1,0,0,0], dashes=[6,900])
            # draw meridians
            lons_space = abs(lons[0])+abs(lons[len(lons)-1])
            m.drawmeridians(np.arange(lons[0],lons[len(lons)-1], round(lons_space/5, 0)), labels=[0,0,0,1], dashes=[6,900])
            m.drawcoastlines()
            m.drawstates()
            m.drawcountries()
            cbar = m.colorbar(cs2,location='bottom',pad="10%")
            plt.show()

    def print_Mdata(self, dataPath, varName="Nd4jMaskedTensor" ):
            f = cdms2.openDataset(dataPath)
            spatialData = f( varName )
            self.logger.info( "Produced result, shape: " +  str( spatialData.shape ) + ", dims: " + spatialData.getOrder() )


