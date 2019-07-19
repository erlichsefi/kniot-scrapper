import logging
from kniot_scrapper.engines import Shufersal as ShufersalEngine
from kniot_scrapper.utils import Logger
from scrapy.crawler import CrawlerProcess


class Shufersal:

    def scrape(self):
        Logger.start_scrapper("Shufersal")

        self.scrapy()
    
    def scrapy():
        logging.getLogger('scrapy').propagate = False

        process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
        process.crawl(ShufersalEngine)
        process.start()
