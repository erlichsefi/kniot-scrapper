from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class FreshMarket(Cerberus):

    ftp_username = 'freshmarket'

    storage_path = './files/freshmarket/'

    def scrape(self):
        Logger.start_scrapper("Fresh Market")
        super(FreshMarket, self).scrape()
