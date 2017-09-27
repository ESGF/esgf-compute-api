import os, time
import logging, cdms2, vcs
import cdms2, datetime, matplotlib, urllib3
import matplotlib.pyplot as plt


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')

    def mpl_timeplot( self, dataPath, varName ):
        self.logger.info( "Plotting file: " +  dataPath )
        f = cdms2.openDataset(dataPath)
        var = f( varName ) # , time=slice(0,1),level=slice(10,11) )
        rank = len(var.shape)
        timeSeries = var[:,0,0] if( rank == 3 ) else var[:,0,0,0] if( rank == 4 ) else var[:,0] if( rank == 2 ) else var[:]
        list_of_datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in var.getTime().asComponentTime()]
        dates = matplotlib.dates.date2num(list_of_datetimes)
        plt.plot_date(dates, timeSeries.data )
        plt.gcf().autofmt_xdate()
        plt.show()
