BOT_NAME = "highscore"
SPLASH_URL = "http://localhost:8050"
SPIDER_MODULES = ["highscore.spiders"]
NEWSPIDER_MODULE = "highscore.spiders"
FEED_FORMAT = "json"
FEED_URI = "result.json"

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
# ITEM_PIPELINES = {"highscore.pipelines.HighscorePipeline": 1}
