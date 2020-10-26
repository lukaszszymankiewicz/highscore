import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest


# just a scratch (TODO)
# it should be an scrapy.Item instance!
class Result:
    source = "page"  # obviously "musescore" in this case
    url = "url"  # adress to best possible firest page of score
    number_of_pages = 2  # not really? (but it is a cool feature!)


class Musescore(scrapy.Spider):
    name = "musescore"

    # TODO: don`t use Nothing Else Matters as default paramter!
    def __init__(self, search_result="sheetmusic?text=nothing else matters", **kwargs):
        self.start_urls = [f"https://musescore.com/{search_result}"]
        super().__init__(**kwargs)

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
            # TODO: add number of pages!
            yield {
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

    def clean_score_image_path(self):
        # TODO
        pass
