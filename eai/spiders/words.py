# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WordsSpider(CrawlSpider):
    name = 'words'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/']

    rules = (Rule(LinkExtractor(allow=()), callback="parse_item",follow=True),)

    words = {
        "virtue": False,
        "signalling": False,
        "is": False,
        "society's": False,
        "version": False,
        "of": False,
        "proof": False,
        "of": False,
        "stake": False
    }

    def parse_item(self, response):
        self.find(str(response.body))

        if self.check():
            print('All words found')
            return


    def check(self):
        for k, v in self.words.items():
            if not v:
                return False
        return True

    def find(self, text):
        for k, v in self.words.items():
            if not v:
                if k in text:
                    self.words[k] = True
                    print('Found word: ', k)
