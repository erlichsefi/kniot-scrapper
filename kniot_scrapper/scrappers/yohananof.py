from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class Yohananof(Cerberus):

    chain = 'yohananof'
    ftp_username = 'yohananof'

    def scrape(self):
        Logger.start_scrapper("Yohananof")
        super(Yohananof, self).scrape()
