import logging, os, time, threading
import cdms2, datetime, matplotlib, math, traceback
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')
        self.threads = []

    def mpl_timeplot( self, dataPath ):
        if dataPath:
            for k in range(0,30):
                if( os.path.isfile(dataPath) ):
                    self.logger.info( "TimePlotting file: " +  dataPath )
                    f = cdms2.openDataset(dataPath)
                    varNames = f.variables.keys()
                    cvars = f.axes
                    fig = plt.figure()
                    iplot = 1
                    nCols = min( len(varNames), 4 )
                    nRows = math.ceil( len(varNames) / float(nCols) )
                    for varName in varNames:
                        try:
                            timeSeries = f( varName, squeeze=1 )
                            timeAxis = timeSeries.getTime()
                            datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in timeAxis.asComponentTime()]
                            dates = matplotlib.dates.date2num(datetimes)
                            ax = fig.add_subplot( nRows, nCols, iplot )
                            ax.plot(dates, timeSeries.data )
                            ax.set_title(varName)
                            ax.xaxis.set_major_formatter( mdates.DateFormatter('%b %Y') )
                            ax.grid(True)
                            iplot = iplot + 1
                        except Exception as err:
                            self.logger.info( "Skipping plot for variable: " +  varName )
                            if( varName.startswith("result") ): traceback.print_exc()

                    fig.autofmt_xdate()
                    plt.show()
                    return
                else: time.sleep(1)

    def run_background(self, process, args=() ):
        thread = threading.Thread(target=process, args=args )
        thread.daemon = True
        thread.start()
        self.threads.append( thread )

    def getAxis(self, axes, atype ):
        """ Constructor
        :type axes: list[cdms2.FileAxis]
        """
        for axis in axes:
#            print " XX: " + axis.getShortName()
            try:
                if( (atype == "X") and self.isLongitude(axis) ): return axis[:]
                if( (atype == "Y") and self.isLatitude(axis) ): return axis[:]
                if( (atype == "Z") and self.isLevel(axis) ): return axis[:]
                if( (atype == "T") and self.isTime(axis) ): return axis[:]
            except Exception as ex:
                print "Exception in getAxis({0})".format(atype), ex
                traceback.print_exc()

        return None

    def isTime(self, axis ):
        id = axis.id.lower()
        hasAxis = hasattr(axis, 'axis')
        if ( hasAxis and axis.axis == 'T' ): return True
        return ( id.startswith( 'tim' ) )

    def isLongitude(self, axis ):
        id = axis.id.lower()
        hasAxis = hasattr(axis, 'axis')
        if ( hasAxis and axis.axis == 'X' ): return True
        return ( id.startswith( 'lon' ) )

    def isLatitude(self, axis ):
        id = axis.id.lower()
        if (hasattr(axis, 'axis') and axis.axis == 'Y'): return True
        return ( id.startswith( 'lat' ) )

    def isLevel(self, axis ):
        id = axis.id.lower()
        if (hasattr(axis, 'axis') and axis.axis == 'Z'): return True
        return ( id.startswith( 'lev' ) or id.startswith( 'plev' ) )

    def getRowsCols( self, number ):
        largest_divisor = 1
        for i in range(2, number):
            if( number % i == 0 ):
                largest_divisor = i
        complement = number/largest_divisor
        return (complement,largest_divisor) if( largest_divisor > complement ) else (largest_divisor,complement)

    def getVariable( self, f ):
        for var in f.variables.values():
            if var.id.startswith("result-"):
                return var
        return None

    def mpl_plot(self, dataPath, timeIndex=0, smooth=False):
        f = cdms2.openDataset( dataPath )
        var = self.getVariable( f )
        naxes = self.getNAxes( var.shape )
        if( naxes == 1 ): self.mpl_timeplot( dataPath )
        else: self.mpl_spaceplot( dataPath, timeIndex, smooth )

    def getNAxes(self, shape ):
        naxes = 0
        for axisLen in shape:
            if( axisLen > 1 ):
                naxes = naxes + 1
        return naxes

    def getAxes( self, dset ):
        vars = dset.variables.values()
        axes = dset.axes.values()
        lons = self.getAxis( vars , "X" )
        lats = self.getAxis( vars , "Y" )
        if( lons is None ):
            lons = self.getAxis( axes , "X" )
        if( lats is None ):
            lats = self.getAxis( axes , "Y" )
        return (lats, lons, vars)

    def mpl_spaceplot( self, dataPath, timeIndex=0, smooth=False ):
        if dataPath:
            for k in range(0,30):
                if( os.path.isfile(dataPath) ):
                    self.logger.info( "SpacePlotting file: " +  dataPath )
                    f = cdms2.openDataset(dataPath)
                    lats, lons, vars = self.getAxes( f )
                    fig = plt.figure()
                    varNames = list( map( lambda v: v.id, vars ) )
                    varNames.sort()
                    nCols = min( len(varNames), 4 )
                    nRows = math.ceil( len(varNames) / float(nCols) )
                    iplot = 1
                    for varName in varNames:
                        variable = f( varName )
                        if len( variable.shape ) > 1:
                            ax = fig.add_subplot( nRows, nCols, iplot )
                            ax.set_title(varName)
                            spatialData = variable( time=slice(timeIndex,timeIndex+1), squeeze=1 )
                            m = Basemap( llcrnrlon=lons[0],
                                         llcrnrlat=lats[0],
                                         urcrnrlon=lons[len(lons)-1],
                                         urcrnrlat=lats[len(lats)-1],
                                         epsg='4326',
                                         lat_0 = lats.mean(),
                                         lon_0 = lons.mean())
                            lon, lat = np.meshgrid( lons.data, lats.data )
                            xi, yi = m(lon, lat)
                            smoothing = 'gouraud' if smooth else 'flat'
                            cs2 = m.pcolormesh(xi, yi, spatialData, cmap='jet', shading=smoothing )
                            lats_space = abs(lats[0])+abs(lats[len(lats)-1])
                            m.drawparallels(np.arange(lats[0],lats[len(lats)-1], round(lats_space/5, 0)), labels=[1,0,0,0], dashes=[6,900])
                            lons_space = abs(lons[0])+abs(lons[len(lons)-1])
                            m.drawmeridians(np.arange(lons[0],lons[len(lons)-1], round(lons_space/5, 0)), labels=[0,0,0,1], dashes=[6,900])
                            m.drawcoastlines()
                            m.drawstates()
                            m.drawcountries()
                            cbar = m.colorbar(cs2,location='bottom',pad="10%")
                            iplot = iplot + 1
                    plt.show()
                    return
                else: time.sleep(1)


    def print_Mdata(self, dataPath ):
        for k in range(0,30):
            if( os.path.isfile(dataPath) ):
                f = cdms2.openDataset(dataPath)
                for variable in f.variables.values():
                    self.logger.info( "Produced result " + variable.id + ", shape: " +  str( variable.shape ) + ", dims: " + variable.getOrder() + " from file: " + dataPath )
                    self.logger.info( "Data Sample: " + str( variable[0] ) )
                    return
            else: time.sleep(1)



    def print_data(self, dataPath ):
        for k in range(0,30):
            if( os.path.isfile(dataPath) ):
                try:
                    f = cdms2.openDataset(dataPath) # """:type : cdms2.CdmsFile """
                    varName = f.variables.values()[0].id
                    spatialData = f( varName ) # """:type : cdms2.FileVariable """
                    self.logger.info( "Produced result, shape: " +  str( spatialData.shape ) + ", dims: " + spatialData.getOrder() )
        #            self.logger.info( "Data: \n" + ', '.join( str(x) for x in spatialData.getValue() ) )
                    self.logger.info( "Data: \n" + str( spatialData.getValue() ) )
                except Exception:
                    self.logger.error( " ** Error printing result data ***")
                return
            else: time.sleep(1)



