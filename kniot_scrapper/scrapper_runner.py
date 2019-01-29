
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
        Shufersal.scrape()
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

