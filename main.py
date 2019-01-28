from scrappers import shufersal
from scrappers import ramilevy
from scrappers import osherad
from scrapy.crawler import CrawlerProcess
import logging


class Main:
    def __init__(self):
        #self.init_shufersal()
        #self.init_rami_levy()
        self.init_osherad()

    @staticmethod
    def init_shufersal():
        logging.getLogger('scrapy').propagate = False
        print("Crawling Shufersal...")

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(shufersal.Shufersal())
        process.start()

    @staticmethod
    def init_rami_levy():
        print("Crawling Rami Levy...")

        ramilevy.RamiLevy().scrape()

    @staticmethod
    def init_osherad():
        print("Crawling Osher Ad...")

        osherad.Osherad().scrape()



if __name__ == '__main__':
    Main()
