from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class RamiLevy(Cerberus):

    ftp_username = 'RamiLevi'

    storage_path = 'dumps/ramilevy/'

    def scrape(self):
        Logger.start_scrapper("Rami Levy")
        super(RamiLevy, self).scrape()