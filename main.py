from Spiders import Shufersal
from scrapy.crawler import CrawlerProcess
import logging


class Main:
    def __init__(self):
        self.init_shufersal(self)

    @staticmethod
    def init_shufersal(self):
        logging.getLogger('scrapy').propagate = False
        print("Crawling Shufersal...")
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(Shufersal.Shufersal())
        process.start()


if __name__ == '__main__':
    Main()
