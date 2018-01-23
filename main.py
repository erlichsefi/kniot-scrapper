from Spiders import Shufersal
from scrapy.crawler import CrawlerProcess

class Main():
    def __init__(self):
        self.init_shufersal(self)

    @staticmethod
    def init_shufersal(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(Shufersal.Shufersal())
        process.start()


if __name__ == '__main__':
    Main()