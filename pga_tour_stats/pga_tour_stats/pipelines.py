# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PgaTourStatsPipeline:

    def tratando_dados(self, item):
        df = pd.read_json(item)
        print(df)

    def process_item(self, item, spider):
        return item
