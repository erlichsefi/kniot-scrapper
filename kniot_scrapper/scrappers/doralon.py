from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class DorAlon(Cerberus):

    chain = 'doralon'
    ftp_username = 'doralon'
    ftp_password = ''

    def scrape(self):
        Logger.start_scrapper("Dor Alon")
        super(DorAlon, self).scrape()
