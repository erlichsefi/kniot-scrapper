
from kniot_scrapper.scrappers import *
import logging

class ScrapperRunner:

    @staticmethod
    def run():
        print("Starting scrapper")

        chainScrappers = {
            "salachdabach": SalachDabach,
            "shufersal": Shufersal,
            "ramiLevy": RamiLevy,
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

        for name, chainScrapper in chainScrappers.items():
            logging.debug(f"scraping {name}") 
            chainScrapper().scrape()
            logging.debug(f"done scraping {name}") 