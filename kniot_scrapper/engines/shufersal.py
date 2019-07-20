import ntpath
import os
import re
import urllib
import lxml.html
from kniot_scrapper.utils import Gzip
from urllib.parse import urlsplit
from urllib.request import urlretrieve


class Shufersal:
    
    storage_path = 'dumps/shufersal/'

    start_page = 'http://prices.shufersal.co.il/'

    original_file_extension = '.gz'
    target_file_extension = '.xml'

    def scrape(self):

        self.scrape_page(self.start_page);

    def scrape_page(self, page):

        html = lxml.html.parse(page)
        test=html.xpath("//*[@id="gridContainer"]/table/tbody/tr/td[1]/a/@href")
        print(test)
        return 'hello'

        file_links = self.collect_file_links(response)

        total_pages = self.get_total_pages(response)

        self.store_xml_files(file_links)

        return self.scrape_page(response)

    @staticmethod
    def collect_file_links(response):

        links = []
        for link in response.xpath('//*[@id="gridContainer"]/table/tbody/tr/td[1]/a/@href').extract():
            links.append(link)
        return links

    @staticmethod
    def get_total_pages(response):

        last_page_link = response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[last()]/@href').extract()[0]
        regex = r"[0-9]+"
        matches = re.search(regex, last_page_link)
        return int(matches.group())

    def store_xml_files(self, links):

        for index, file_link in enumerate(links):
            file_save_path = self.storage_path + ntpath.basename(urlsplit(file_link).path)
            filename = os.path.splitext(file_save_path)[0]

            urlretrieve(file_link, filename + self.original_file_extension)

            Gzip.extract_xml_file_from_gz_file(self.target_file_extension, file_save_path, filename)

            os.remove(filename + self.original_file_extension)

    def continue_to_next_pages(self, response):
        
        for next_page in response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[contains(.,">")]'):
            yield response.follow(next_page, self.parse)
