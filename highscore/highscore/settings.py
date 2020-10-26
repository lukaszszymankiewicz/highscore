BOT_NAME = "highscore"
SPLASH_URL = "http://192.168.43.209:8050"

SPIDER_MODULES = ["highscore.spiders"]
NEWSPIDER_MODULE = "highscore.spiders"

SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
    "highscore.middlewares.HighscoreSpiderMiddleware": 543,
}

DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

HTTPCACHE_STORAGE = "scrapy_splash.SplashAwareFSCacheStorage"
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
