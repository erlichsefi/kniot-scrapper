from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class TivTaam(Cerberus):

    ftp_username = 'TivTaam'

    storage_path = 'dumps/tivtaam/'

    def scrape(self):
        Logger.start_scrapper("Tiv Taam")
        super(TivTaam, self).scrape()
