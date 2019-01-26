import gzip
import ntpath
import os
import re
import scrapy
from tqdm import tqdm
from urllib.parse import urlsplit
from urllib.request import urlretrieve


class Shufersal(scrapy.Spider):
    name = 'shufersal-spider'
    start_urls = ['http://prices.shufersal.co.il']
    allowed_domains = ['prices.shufersal.co.il']

    storage_path = './files/shufersal/'
    progressbar = False

    files_per_page = 20
    original_file_extension = '.gz'
    target_file_extension = '.xml'

    def parse(self, response):

        links = self.collect_links(response)

        total_pages = self.get_total_pages(response)

        self.start_progress_bar(total_pages)

        self.get_xml_files(links)

        return self.continue_to_next_pages(response)

    @staticmethod
    def collect_links(response):
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

    def start_progress_bar(self, total_pages):
        if self.progressbar:
            return 0
        self.progressbar = tqdm(total=total_pages * self.files_per_page)

    def get_xml_files(self, links):
        for index, file_link in enumerate(links):
            self.progressbar.update(1)

            file_save_path = self.storage_path + ntpath.basename(urlsplit(file_link).path)
            filename = os.path.splitext(file_save_path)[0]

            urlretrieve(file_link, filename + self.original_file_extension)

            self.extract_xml_file_from_gz_file(file_save_path, filename)

            os.remove(filename + self.original_file_extension)

    def extract_xml_file_from_gz_file(self, file_save_path, filename):
        with gzip.open(file_save_path, 'rb') as infile:
            with open(filename + self.target_file_extension, 'wb') as outfile:
                for line in infile:
                    outfile.write(line)

    def continue_to_next_pages(self, response):
        for next_page in response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[contains(.,">")]'):
            yield response.follow(next_page, self.parse)
