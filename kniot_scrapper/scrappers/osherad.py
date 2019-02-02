from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class Osherad(Cerberus):

    ftp_username = 'osherad'

    storage_path = 'dumps/osherad/'

    def scrape(self):
        Logger.start_scrapper("Osher Ad")
        super(Osherad, self).scrape()
