import os, time
import logging, cdms2, vcs
import cdms2, datetime, matplotlib, urllib3
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import matplotlib.dates as mdates


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')

    def mpl_timeplot( self, dataPath, varName="Nd4jMaskedTensor" ):
        self.logger.info( "Plotting file: " +  dataPath )
        f = cdms2.openDataset(dataPath)
        timeSeries = f( varName, squeeze=1 )
        datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in timeSeries.getTime().asComponentTime()]
        dates = matplotlib.dates.date2num(datetimes)
        fig, ax = plt.subplots()
        ax.plot(dates, timeSeries.data )
        ax.xaxis.set_major_formatter( mdates.DateFormatter('%Y') )
        ax.grid(True)
        fig.autofmt_xdate()
        plt.show()

    def mpl_spaceplot( self, dataPath, timeIndex=0, varName="Nd4jMaskedTensor" ):
        self.logger.info( "Plotting file: " +  dataPath )
        f = cdms2.openDataset(dataPath)
        spatialData = f( varName, time=slice(timeIndex,timeIndex+1), squeeze=1 )
        fig, ax = plt.subplots()
        ax.imshow(spatialData, interpolation="none", cmap='viridis')
        plt.show()

    def plotly_timeplot( self, dataPath, varName="Nd4jMaskedTensor" ):
        self.logger.info( "Plotting file: " +  dataPath )
        py.offline.init_notebook_mode()   # py.init_notebook_mode(connected=True)
        f = cdms2.openDataset(dataPath)
        timeSeries = f( varName, squeeze=1 )
        datetimes = pd.to_datetime(timeSeries.getTime().asdatetime())
        data = [go.Scatter(x=datetimes, y=timeSeries)]
        py.iplot(data)
#        print(py.plot(data, output_type='file', filename='testTimeSeries.html', auto_open=False))





