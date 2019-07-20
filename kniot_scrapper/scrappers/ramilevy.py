from kniot_scrapper.engines import Cerberus
from kniot_scrapper.utils import Logger


class RamiLevy(Cerberus):

    chain = 'ramilevy'
    ftp_username = 'RamiLevi'

    def scrape(self):
        Logger.start_scrapper("Rami Levy")
        super(RamiLevy, self).scrape()