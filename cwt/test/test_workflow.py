
import cwt, os, time
import logging, cdms2, vcs
import cdms2, datetime, matplotlib
import matplotlib.pyplot as plt

# host = 'https://www-proxy-dev.nccs.nasa.gov/edas/wps/cwt'
host ="https://dptomcat03-int/wps/cwt"

class TestWorkflow:

    def run( self ):
        print "Initializing EDAS python client"
        logger = logging.getLogger('cwt.wps')
        domain_data = { 'id': 'd0', 'lat': {'start':70, 'end':90, 'crs':'values'}, 'lon': {'start':5, 'end':45, 'crs':'values'}, 'time': {'start':0, 'end':1000, 'crs':'indices'} }
        d0 = cwt.Domain.from_dict(domain_data)

        inputs = cwt.Variable("collection://cip_merra2_mon_tas", "tas", domain="d0" )

        op_data =  { 'name': "CDSpark.average", 'axes': "xy" }
        op =  cwt.Process.from_dict( op_data ) # """:type : Process """
        op.set_inputs( inputs )

        wps = cwt.WPS( host, log=True, log_file=os.path.expanduser("~/esgf_api.log"), verify=False )

        print "Submitting request."
        wps.execute( op, domain=d0, async=True )

        dataPath = wps.download_result(op)
        logger.info( "Plotting file: " +  dataPath )
        varName = "Nd4jMaskedTensor"
        f = cdms2.openDataset(dataPath)
        var = f( varName ) # , time=slice(0,1),level=slice(10,11) )
        timeSeries = var[:,0,0]
        list_of_datetimes = [datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, int(x.second)) for x in var.getTime().asComponentTime()]
        dates = matplotlib.dates.date2num(list_of_datetimes)
        plt.plot_date(dates, timeSeries.data )
        plt.gcf().autofmt_xdate()
        plt.show()


executor = TestWorkflow()
executor.run()