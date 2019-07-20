import ntpath
import os
import re
import urllib
import lxml.html
import re
from lxml import etree
from kniot_scrapper.utils import Gzip
from urllib.parse import urlsplit
from urllib.request import urlretrieve


class Shufersal:
    
    storage_path = 'dumps/shufersal/'

    base_url = 'http://prices.shufersal.co.il/'

    original_file_extension = '.gz'
    target_file_extension = '.xml'

    def scrape(self):

        self.scrape_page(self.base_url);

    def scrape_page(self, page):

        html = lxml.html.parse(page)

        total_pages = self.get_total_pages(html)

        for page_number in range(1, total_pages + 1):
            html = lxml.html.parse(self.base_url + '?page=' + str(page_number))

            file_links = self.collect_file_links(html)

            self.store_xml_files(file_links)

    def collect_file_links(self, html):

        links = []
        for link in html.xpath('//*[@id="gridContainer"]/table/tbody/tr/td[1]/a/@href'):
            links.append(link)
        return links

    def store_xml_files(self, links):

        for index, file_link in enumerate(links):
            file_save_path = self.storage_path + ntpath.basename(urlsplit(file_link).path)
            filename = os.path.splitext(file_save_path)[0]

            urlretrieve(file_link, filename + self.original_file_extension)

            Gzip.extract_xml_file_from_gz_file(self.target_file_extension, file_save_path, filename)

            os.remove(filename + self.original_file_extension)

    def get_total_pages(self, html):

        return int(re.findall("^\/\?page\=([0-9]{2})$", html.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[6]/@href')[0])[0])