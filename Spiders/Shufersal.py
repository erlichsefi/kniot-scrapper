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

        pages_extracted = response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/text()').extract()
        pages_nums = []
        for element in pages_extracted:
            if element != ' ':
                pages_nums.append(element)
        page_num = int(pages_nums[0])

        self.links = []
        for link in response.xpath('//*[@id="gridContainer"]/table/tbody/tr/td[1]/a/@href').extract():
            self.links.append(link)

        total_pages = self.get_total_pages(response)

        self.start_progress_bar(total_pages)

        for index, fileLink in enumerate(self.links):
            self.bar.update(1)

            fileSavePath = './files/shufersal/' + ntpath.basename(urlsplit(fileLink).path)
            filename = os.path.splitext(fileSavePath)[0]

            urlretrieve(fileLink, filename + '.gz')

            with gzip.open(fileSavePath, 'rb') as infile:
                with open(filename + '.xml', 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)

            os.remove(filename + '.gz')

        for next_page in response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[contains(.,">")]'):
            yield response.follow(next_page, self.parse)

    def start_progress_bar(self, total_pages):
        if self.bar:
            return 0
        self.bar = tqdm(total=total_pages * 20)

    def get_total_pages(self, response):
        last_page_link = response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[last()]/@href').extract()[0]
        regex = r"[0-9]+"
        matches = re.search(regex, last_page_link)
        return int(matches.group())
