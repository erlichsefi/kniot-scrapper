from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class Keshet(Cerberus):

    ftp_username = 'Keshet'

    storage_path = 'dumps/keshet_taamim/'

    def scrape(self):
        Logger.start_scrapper("Keshet Taamim")
        super(Keshet, self).scrape()
