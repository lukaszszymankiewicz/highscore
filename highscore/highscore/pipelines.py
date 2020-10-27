from itemadapter import ItemAdapter


class HighscorePipeline(object):
    results = []

    def process_item(self, item, spider):
        self.results.append(dict(item))
