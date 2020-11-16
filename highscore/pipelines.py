import re

from itemadapter import ItemAdapter


class MusescorePipeline(object):
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["url"] = clean_url(adapter["url"])
        adapter["n_pages"] = clean_number_of_pages(adapter["n_pages"])
        return item


def clean_url(url):
    return url.split("@")[0]


def clean_number_of_pages(string_content: str):
    return int(re.search("\d* page", string_content).group()[0:-5])
