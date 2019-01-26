import scrapy
from urllib.parse import urlsplit
from urllib.request import urlretrieve
import ntpath
import gzip
import os
import re
from tqdm import tqdm


class Shufersal(scrapy.Spider):
    name = 'shufersal-spider'
    start_urls = ['http://prices.shufersal.co.il']
    allowed_domains = ['prices.shufersal.co.il']
    bar = False

    def parse(self, response):

        links = self.collect_links(response)

        total_pages = self.get_total_pages(response)

        self.start_progress_bar(total_pages)

        self.download_from_links(links)

        self.continue_to_next_pages(response)

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
        if self.bar:
            return 0
        self.bar = tqdm(total=total_pages * 20)

    def download_from_links(self, links):
        for index, file_link in enumerate(links):
            self.bar.update(1)

            file_save_path = './files/shufersal/' + ntpath.basename(urlsplit(fileLink).path)
            filename = os.path.splitext(file_save_path)[0]

            urlretrieve(file_link, filename + '.gz')

            with gzip.open(file_save_path, 'rb') as infile:
                with open(filename + '.xml', 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)

            os.remove(filename + '.gz')

    def continue_to_next_pages(self, response):
        for next_page in response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[contains(.,">")]'):
            yield response.follow(next_page, self.parse)
