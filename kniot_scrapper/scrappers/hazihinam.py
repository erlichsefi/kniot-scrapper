from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class HaziHinam(Cerberus):

    ftp_username = 'HaziHinam'

    storage_path = './files/hazihinam/'

    def scrape(self):
        Logger.start_scrapper("Hazi Hinam")
        super(HaziHinam, self).scrape()