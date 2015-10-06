from datetime import datetime

from scrapy.spiders import Spider
from hollywood_crawler.items import HollywoodItem
import scrapy


class BoxofficeSpider(Spider):

    name = "boxoffice"
    allowed_domains = ["boxofficemojo.com"]
    start_urls = [
        "http://www.boxofficemojo.com/people/?view=Director&sort=sumgross"
        ]

    def parse(self, response):
        """

        Scrapy Spider to scrape boxofficemojo.com for director
        data.

        follows links through director profiles and their respective
        films.

        """

        links = response.xpath('//td/font/a[contains(@href,"chart")]/@href').extract()
        for href in links:
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_director_page)

    def parse_director_page(self, response):

        item = HollywoodItem()
        item['name'] = get_name(response)
        item['years_active'] = get_years(response)
        item['average_gross'] = get_ave_gross(response)
        item['movie_count'] = get_count(response)

        yield item


def get_name(response):

    name = response.xpath('//td/h1/text()').extract_first()

    return name


def get_count(response):

    dates = response.xpath('//table[1]/tr/td/font/a/text()|//table[1]/tr/td/font/text()').re(r'^\d+/\S*')
    count = len(dates)

    return count


def get_years(response):

    dates = response.xpath('//table[1]/tr/td/font/a/text()|//table[1]/tr/td/font/text()').re(r'^\d+/\S*')
    first_d = datetime.strptime(dates[0], "%m/%d/%y")
    last_d = datetime.strptime(dates[-1], "%m/%d/%y")
    years = (first_d-last_d)
    years = years.days/365

    return years


def get_ave_gross(response):

    ave_gross = response.xpath('//div/font/b[contains(.,"Average")]').re(r'Average: (\S*\d)')[0]
    ave_gross = int(ave_gross.replace("$", "").replace(",", ""))

    return ave_gross

        
