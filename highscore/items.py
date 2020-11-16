import scrapy


class HighscoreItem(scrapy.Item):
    source = scrapy.Field(serializer=str)
    url = scrapy.Field(serializer=str)
    link = scrapy.Field(serializer=str)
    n_pages = scrapy.Field(serializer=int)
