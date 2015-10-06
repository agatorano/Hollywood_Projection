from scrapy.exceptions import DropItem


class DuplicatePipeline(object):

    def __init__(self):
        self.dir_seen = set()

    def process_item(self, item, spider):
        if item['name'] in self.dir_seen:
            raise DropItem("Duplicate director found: %s" % item)
        else:
            self.dir_seen.add(item['name'])
            return item
