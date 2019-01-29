from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class StopMarket(Cerberus):

    ftp_username = 'Stop_Market'

    storage_path = './files/stop_market/'

    def scrape(self):
        Logger.start_scrapper("Stop Market")
        super(StopMarket, self).scrape()