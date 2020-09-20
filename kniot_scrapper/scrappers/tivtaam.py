from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class TivTaam(Cerberus):

    chain = 'tivtaam'
    ftp_username = 'TivTaam'
    ftp_password = ''

    def scrape(self):
        Logger.start_scrapper("Tiv Taam")
        super(TivTaam, self).scrape()
