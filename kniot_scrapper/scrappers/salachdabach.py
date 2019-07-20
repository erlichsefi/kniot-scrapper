
from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class SalachDabach(Cerberus):

    chain = 'salachdabach'
    ftp_username = 'Retalix'
    ftp_password = '12345'
    ftp_path = 'SalachDabach'

    def scrape(self):
        Logger.start_scrapper("SalachDabach")
        super(SalachDabach, self).scrape()
