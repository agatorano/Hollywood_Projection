from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):

    def __init__(self):
        self.dir_seen = set()

    def process_item(self, item, spider):
        if item['name'] in self.dir_seen:
            raise DropItem("Duplicate director found: %s" % item)
        else:
            self.dir_seen.add(item['name'])
            return item


class Drop_Negative_Year(object):

    def process_item(self, item, spider):

        if item['years_active'] < 0:
            raise DropItem("Negative Year Found: %s" % item)
        else:
            return item
