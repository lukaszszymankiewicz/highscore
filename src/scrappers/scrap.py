import json
import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from highscore.spiders import Musescore

results = []

SONG = "nothing else matters cello"


def scrap_pages(song: str = None):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(Musescore, song=song)
    process.start()

    with open("result.json") as file:
        data = json.load(file)

    file.close()

    return data


# damn, delete file if exist!
try:
    os.remove("result.json")
except OSError:
    pass

results = scrap_pages(song=SONG)
