# -*- coding: utf-8 -*-
import scrapy


class TrailersSpider(scrapy.Spider):
    name = "trailers"
    allowed_domains = ["http://www.imdb.com/trailers"]
    start_urls = (
        'http://www.imdb.com/trailers/',
    )

    def parse(self, response):
        #logging.getLogger('scrapy').setLevel(logging.ERROR)
        movies=response.xpath(".//*[@id='popTab']/div/div[position()]")
        for movie in movies:
            trailerLink=movie.xpath('div[1]/a/@href').extract_first()
            movieName=movie.xpath('div[2]/a/text()').extract_first()
            print movieName,trailerLink
