from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from highscore.spiders import Musescore

results = []


def scrap_pages(song: str = None):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(Musescore, song=song)
    process.start()


scrap_pages(song="nothing else matters cello")
