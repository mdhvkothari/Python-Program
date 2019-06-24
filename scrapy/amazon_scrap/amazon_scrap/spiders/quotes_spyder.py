import scrapy
from ..items import AmazonScrapItem


class QuoetSpider(scrapy.Spider):
        name ='quotes'
        start_urls =[
            'http://quotes.toscrape.com/'
        ]

        def parse(self,response):
            item = AmazonScrapItem()


            all_div_class = response.css('div.quote')

            for quotes in all_div_class:

                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tags = quotes.css('.tag::text').extract()

                item['title'] = title
                item['author'] = author
                item['tags'] = tags

                yield item

            #get the value of next page
            next_page = response.css('li.next a::attr(href)').get()

            if next_page is not None:
                yield response.follow(next_page,callback = self.parse)
