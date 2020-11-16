import scrapy
from scrapy_splash import SplashRequest

from ..items import HighscoreItem


class Musescore(scrapy.Spider):
    SPLASH_REQUEST_ARGS = {"wait": 1.0}
    name = "musescore"
    source = "musescore.com"

    custom_settings = {
        "SPIDER_MIDDLEWARES": {
            "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
            "highscore.middlewares.HighscoreSpiderMiddleware": 543,
        },
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_splash.SplashCookiesMiddleware": 723,
            "scrapy_splash.SplashMiddleware": 725,
            "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
        },
        "HTTPCACHE_STORAGE": "scrapy_splash.SplashAwareFSCacheStorage",
        "DUPEFILTER_CLASS": "scrapy_splash.SplashAwareDupeFilter",
        "ITEM_PIPELINES": {
            "highscore.pipelines.MusescorePipeline": 99,
        },
    }

    def __init__(self, song="xxx yyy zzz", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f"https://musescore.com/sheetmusic?text={song}"]

    def _get_splash_request(self, url):
        return SplashRequest(url=url, callback=self.parse, args=self.SPLASH_REQUEST_ARGS)

    def start_requests(self):
        for url in self.start_urls:
            yield self._get_splash_request(url)

    def parse(self, response):
        no_results = response.xpath('//h1[@class="_2M8z2 _2OGD_"]//text()').get()
        if no_results:
            raise scrapy.exceptions.CloseSpider("no results found")

        urls = response.xpath('//div[@class="_3B6rQ _1QTgP"]//img//@data-src').getall()
        links = response.xpath(
            '//a[@class="_36lU2 _3qfU_ _38TLP _1Us9e _1OS6i _15kzJ"]//@href'
        ).getall()
        pages = response.xpath('//div[@class="_72a_M QgXg4"]//text()').getall()
        next_page = response.xpath('//a[@isnext="true"]//@href').get()

        for url, link, n_pages in zip(urls, links, pages):
            yield HighscoreItem(
                source=self.source,
                url=url,
                link=link,
                n_pages=n_pages,
            )

        if next_page is not None:
            yield self._get_splash_request(next_page)
