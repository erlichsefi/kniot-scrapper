
from kniot_scrapper.scrappers import *

class ScrapperRunner:

    @staticmethod
    def run():
        print("Starting scrapper")

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
        Shufersal.scrape()

