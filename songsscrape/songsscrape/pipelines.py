# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from ..download import DownloadAndSave

class SongsscrapePipeline:
    def process_item(self, item, spider):
        # name = self.get_name(item['url'])
        # d = DownloadAndSave(item['url'], item['text'])
        return item
       
