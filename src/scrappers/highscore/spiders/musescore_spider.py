import scrapy
from scrapy_splash import SplashRequest


class Musescore(scrapy.Spider):
    SPLASH_REQUEST_ARGS = {"wait": 0.5}
    name = "musescore"

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
    }

    def __init__(self, song="nothing else matters violin", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f"https://musescore.com/sheetmusic?text={song}"]

    def _get_splash_request(self, url):
        return SplashRequest(url=url, callback=self.parse, args=self.SPLASH_REQUEST_ARGS)

    def start_requests(self):
        for url in self.start_urls:
            yield self._get_splash_request(url)

    def parse(self, response):
        scores = response.xpath('//div[@class="_3B6rQ _1QTgP"]//img//@data-src').getall()

        for score in scores:
            yield {"source": self.name, "url": score}

        next_page = response.xpath('//a[@isnext="true"]//@href').get()

        if next_page is not None:
            yield self._get_splash_request(next_page)
