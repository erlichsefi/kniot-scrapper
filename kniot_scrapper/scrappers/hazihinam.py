from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class HaziHinam(Cerberus):

    chain = 'hazihinam'
    ftp_username = 'HaziHinam'

    def scrape(self):
        Logger.start_scrapper("Hazi Hinam")
        super(HaziHinam, self).scrape()