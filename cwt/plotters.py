import logging
import cdms2, datetime, matplotlib, urllib3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')

    def mpl_timeplot( self, dataPath, varName="Nd4jMaskedTensor" ):
        if dataPath:
            self.logger.info( "Plotting file: " +  dataPath )
            f = cdms2.openDataset(dataPath)
            timeSeries = f( varName, squeeze=1 )
            datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in timeSeries.getTime().asComponentTime()]
            dates = matplotlib.dates.date2num(datetimes)
            fig, ax = plt.subplots()
            ax.plot(dates, timeSeries.data )
            ax.xaxis.set_major_formatter( mdates.DateFormatter('%b %Y') )
            ax.grid(True)
            fig.autofmt_xdate()
            plt.show()

    def mpl_spaceplot( self, dataPath, timeIndex=0, varName="Nd4jMaskedTensor" ):
        if dataPath:
            self.logger.info( "Plotting file: " +  dataPath )
            f = cdms2.openDataset(dataPath)
            spatialData = f( varName, time=slice(timeIndex,timeIndex+1), squeeze=1 )
            fig, ax = plt.subplots()
            ax.imshow(spatialData, interpolation="bilinear", cmap='jet', origin='lower')
            plt.show()

    def print_Mdata(self, dataPath, varName="Nd4jMaskedTensor" ):
            f = cdms2.openDataset(dataPath)
            spatialData = f( varName )
            self.logger.info( "Produced result, shape: " +  str( spatialData.shape ) + ", dims: " + spatialData.getOrder() )


