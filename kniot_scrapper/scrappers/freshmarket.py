from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class FreshMarket(Cerberus):

    chain = 'freshmarket'
    ftp_username = 'freshmarket'
    ftp_password = ''

    def scrape(self):
        Logger.start_scrapper("Fresh Market")
        super(FreshMarket, self).scrape()
