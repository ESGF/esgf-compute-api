import os, time
import logging, cdms2, vcs
import cdms2, datetime, matplotlib, urllib3
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd


class PlotMgr:

    def __init__(self):
        self.logger = logging.getLogger('cwt.wps')

    def mpl_timeplot( self, dataPath, varName="Nd4jMaskedTensor" ):
        self.logger.info( "Plotting file: " +  dataPath )
        f = cdms2.openDataset(dataPath)
        timeSeries = f( varName, squeeze=1 ) # , time=slice(0,1),level=slice(10,11) )
        list_of_datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in timeSeries.getTime().asComponentTime()]
        dates = matplotlib.dates.date2num(list_of_datetimes)
        plt.plot_date(dates, timeSeries.data )
        plt.gcf().autofmt_xdate()
        plt.show()

    def plotly_timeplot( self, dataPath, varName="Nd4jMaskedTensor" ):
        self.logger.info( "Plotting file: " +  dataPath )
        f = cdms2.openDataset(dataPath)
        timeSeries = f( varName, squeeze=1 )
        datetimes = pd.to_datetime(timeSeries.getTime().asdatetime())
        data = [go.Scatter(x=datetimes, y=timeSeries)]
        print(py.plot(data, output_type='file', filename='testTimeSeries.html', auto_open=False))





