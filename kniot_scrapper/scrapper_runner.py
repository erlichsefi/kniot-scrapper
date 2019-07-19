
from kniot_scrapper.scrappers import *

class ScrapperRunner:

    @staticmethod
    def run():
        print("Starting scrapper")

        chainScrappers = {
            "ramiLevy": RamiLevy,
            "shufersal": Shufersal,
            "osherad": Osherad,
            "haziHinam": HaziHinam,
            "keshet": Keshet,
            "superDosh": SuperDosh,
            "yohananof": Yohananof,
            "stopMarket": StopMarket,
            "dorAlon": DorAlon,
            "tivTaam": TivTaam,
            "freshMarket": FreshMarket,
        }

        for chainScrapper in chainScrappers.values(): 
            chainScrapper().scrape()
     

