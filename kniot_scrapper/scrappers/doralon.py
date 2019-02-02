from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class DorAlon(Cerberus):

    ftp_username = 'doralon'

    storage_path = 'dumps/doralon/'

    def scrape(self):
        Logger.start_scrapper("Dor Alon")
        super(DorAlon, self).scrape()
