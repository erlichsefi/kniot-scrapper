import asyncio
import lxml.html
import ntpath
import os
import re
from urllib.parse import urlsplit
from urllib.request import urlretrieve
from kniot_scrapper import Engine
from kniot_scrapper.utils import Gzip
from kniot_scrapper.utils import Logger


class Shufersal(Engine):
    
    base_url = 'http://prices.shufersal.co.il/'

    target_file_extension = '.xml'

    def scrape(self):
        super(Shufersal, self).scrape()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.scrape_pages(self.base_url))

    async def scrape_pages(self, page):
        loop = asyncio.get_event_loop()
        html = lxml.html.parse(page)

        total_pages = self.get_total_pages(html)

        futures = []
        for page_number in range(1, total_pages + 1):
            futures.append(loop.run_in_executor(
                None, 
                self.scrape_page, 
                self.base_url + '?page=' + str(page_number)
            )) 

        for response in await asyncio.gather(*futures):
            pass

    def get_total_pages(self, html):
        return int(re.findall("^\/\?page\=([0-9]{2})$", html.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[6]/@href')[0])[0])

    def scrape_page(self, page):
        html = lxml.html.parse(page)

        file_links = self.collect_file_links(html)

        self.store_xml_files(file_links)
        

    def collect_file_links(self, html):
        links = []
        for link in html.xpath('//*[@id="gridContainer"]/table/tbody/tr/td[1]/a/@href'):
            links.append(link)
        return links

    def store_xml_files(self, links):
        for index, file_link in enumerate(links):
            self.store_xml_file(file_link)

    def store_xml_file(self, file_link):
        file_save_path = os.path.join(self.storage_path, ntpath.basename(urlsplit(file_link).path))
        
        Logger.file_parse(self.chain, ntpath.basename(urlsplit(file_link).path))

        try:
            urlretrieve(file_link, file_save_path)
        except:
            Logger.file_retry(self.chain, ntpath.basename(urlsplit(file_link).path))
            self.store_xml_file(file_link)

        Gzip.extract_xml_file_from_gz_file(file_save_path)

        os.remove(file_save_path)