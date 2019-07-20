import logging
from kniot_scrapper.engines import Shufersal as ShufersalEngine
from kniot_scrapper.utils import Logger


class Shufersal(ShufersalEngine):

    chain = 'shufersal'

    def scrape(self):
        
        Logger.start_scrapper("Shufersal")
        super(Shufersal, self).scrape()
    
