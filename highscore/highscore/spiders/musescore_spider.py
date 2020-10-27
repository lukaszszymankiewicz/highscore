import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest


class Musescore(scrapy.Spider):
    name = "musescore"

    def __init__(self, song="nothing else matters violin", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f"https://musescore.com/sheetmusic?text={song}"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse,
                args={
                    "wait": 0.5,
                },
            )

    def parse(self, response):
        # TODO: Beutiful soup is unnecessary! use scrapy build-in tools!
        soup = BeautifulSoup(response.text, features="lxml")

        # change it to scrapy find method!
        scores = soup.find_all(name="a", attrs={"class": "SA76l"})

        for score in scores:
            yield {
                # TODO: add number of pages!
                "source": self.name,
                "url": score.find(name="img")["data-src"]
                # "pages": score["pages_count"],
            }

        next_page = soup.find(name="a", attrs={"isnext": "true"})

        if next_page is not None:
            # TODO: this can be but into function!
            yield SplashRequest(
                url=next_page["href"],
                callback=self.parse,
                args={
                    "wait": 0.5,
                },
            )
