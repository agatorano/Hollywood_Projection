from datetime import datetime

from scrapy.spiders import Spider
from scrapy.selector import Selector

from hollywood_crawler.items import HollywoodItem

class BoxofficeSpider(Spider):

    name = "boxoffice"
    allowed_domains = ["boxofficemojo.com"]
    start_urls = ["http://www.boxofficemojo.com/people/chart/?view=Director&id=stevenspielberg.htm"]

    def parse(self, response):
        """

        Scrapy Spider to scrape boxofficemojo.com for director
        data. 

        follows links through director profiles and their respective
        films.

        """
        item = HollywoodItem()
        sel = Selector(response)
        item['name'] = itemresponse.xpath('//td/h1/text()').extract_first()
        
        ave_gross = response.xpath('//td[1]/font/b').re(r'Average: (\S*\d)')[0]
        ave_gross = int(ave_gross.replace("$","").replace(",",""))

        dates = response.xpath('//table[1]/tr/td/font/a/text()|//table[1]/tr/td/font/text()').re(r'^\d+/\S*')
        first_d = datetime.strptime(dates[0],"%m/%d/%y")
        last_d = datetime.strptime(dates[-1],"%m/%d/%y")

        years = (first_d-last_d)

        years = years.days/365



        
