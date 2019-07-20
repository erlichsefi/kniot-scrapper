from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class SuperDosh(Cerberus):

    chain = 'superdosh'
    ftp_username = 'SuperDosh'

    def scrape(self):
        Logger.start_scrapper("SuperDosh")
        super(SuperDosh, self).scrape()
