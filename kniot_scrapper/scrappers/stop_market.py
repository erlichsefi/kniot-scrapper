from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class StopMarket(Cerberus):

    chain = 'stop_market'
    ftp_username = 'Stop_Market'

    def scrape(self):
        Logger.start_scrapper("Stop Market")
        super(StopMarket, self).scrape()