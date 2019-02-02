from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class Yohananof(Cerberus):

    ftp_username = 'yohananof'

    storage_path = 'dumps/yohananof/'

    def scrape(self):
        Logger.start_scrapper("Yohananof")
        super(Yohananof, self).scrape()
