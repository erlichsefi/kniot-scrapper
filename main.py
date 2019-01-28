from scrappers import shufersal
from scrappers import ramilevy
from scrapy.crawler import CrawlerProcess
import logging


class Main:
    def __init__(self):
        self.init_shufersal()
        self.init_rami_levy()

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



if __name__ == '__main__':
    Main()
