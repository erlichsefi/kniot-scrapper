import logging
from scrapy.crawler import CrawlerProcess
from kniot_scrapper.scrappers import DorAlon
from kniot_scrapper.scrappers import FreshMarket
from kniot_scrapper.scrappers import HaziHinam
from kniot_scrapper.scrappers import Keshet
from kniot_scrapper.scrappers import Osherad
from kniot_scrapper.scrappers import RamiLevy
from kniot_scrapper.scrappers import Shufersal
from kniot_scrapper.scrappers import StopMarket
from kniot_scrapper.scrappers import SuperDosh
from kniot_scrapper.scrappers import TivTaam
from kniot_scrapper.scrappers import Yohananof

class ScrapperRunner:

    def run(self):
        self.init_cerberus()
        self.init_shufersal()

    @staticmethod
    def init_shufersal():
        logging.getLogger('scrapy').propagate = False

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(Shufersal)
        process.start()

    @staticmethod
    def init_cerberus():
        RamiLevy().scrape()
        Osherad().scrape()
        HaziHinam().scrape()
        Keshet().scrape()
        SuperDosh().scrape()
        Yohananof().scrape()
        StopMarket().scrape()
        DorAlon().scrape()
        TivTaam().scrape()
        FreshMarket().scrape()