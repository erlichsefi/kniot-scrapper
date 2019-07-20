from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class Keshet(Cerberus):

    chain = 'keshet_taamim'
    ftp_username = 'Keshet'

    def scrape(self):
        Logger.start_scrapper("Keshet Taamim")
        super(Keshet, self).scrape()
