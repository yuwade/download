import scrapy
from download.items import DownloadItem
class HereYouGo(scrapy.Spider):
    name = 'hereyougo'
    start_urls = ['https://hereyougo.fr/features']
    def parse(self, response):
        for sel in response.xpath('//*[@id="features5"]/div//img'):
            item = DownloadItem()
            src = sel.xpath('@src').extract()
            item['src'] = 'https://hereyougo.fr'+src[0]
            yield item
