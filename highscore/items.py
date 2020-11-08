import scrapy


class HighscoreItem(scrapy.Item):
    pass


class Score(scrapy.Item):
    source = scrapy.Field()
    url = scrapy.Field()
