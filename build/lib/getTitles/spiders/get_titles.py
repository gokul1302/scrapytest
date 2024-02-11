import scrapy
import os

class TitleSpider(scrapy.Spider):
    name = "title"
    #get the list of domains from the file
    with open('data/domains.txt', 'r') as f:
        start_urls = f.readlines()
    #add the http:// to each domain
    start_urls = ['http://' + url.strip() for url in start_urls]


    def parse(self, response):
        self.log('Visited %s' % response.url)
        yield {
            'title': response.css('title::text').extract_first(),
            'url': response.url
        }

