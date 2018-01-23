import scrapy
import urllib
import urlparse
import ntpath
import gzip
import os


class Shufersal(scrapy.Spider):

    name = 'shufersal-spider'
    start_urls = ['http://prices.shufersal.co.il']
    allowed_domains = ['prices.shufersal.co.il'];

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

        for fileLink in self.links:
            fileSavePath = './files/shufersal/' + ntpath.basename(urlparse.urlsplit(fileLink).path)
            filename = os.path.splitext(fileSavePath)[0]

            testfile = urllib.URLopener()
            testfile.retrieve(fileLink, filename + '.gz')

            with gzip.open(fileSavePath, 'rb') as infile:
                with open(filename + '.xml', 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)

            os.remove(filename + '.gz')

        for next_page in response.xpath('//*[@id="gridContainer"]/table/tfoot/tr/td/a[contains(.,">")]'):
            yield response.follow(next_page, self.parse)