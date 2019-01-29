from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class RamiLevy(Cerberus):

    ftp_username = 'RamiLevi'

    storage_path = './files/ramilevy/'

    def scrape(self):
        Logger.start_scrapper("Rami Levy")
        super(RamiLevy, self).scrape()