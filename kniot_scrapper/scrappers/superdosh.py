from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class SuperDosh(Cerberus):

    ftp_username = 'SuperDosh'

    storage_path = 'dumps/superdosh/'

    def scrape(self):
        Logger.start_scrapper("SuperDosh")
        super(SuperDosh, self).scrape()
