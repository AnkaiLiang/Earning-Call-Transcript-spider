# -*- coding: utf-8 -*-
from scrapy.conf import settings
from scrapy import log
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):
    def __init__(self):
		self.base_addrees = settings['BASE_ADDREES']
    def mkdir(self, path):
	    import os
	    isExists=os.path.exists(path)
	 
	    os.makedirs(path)
	return

    def process_item(self, item, spider):
        path = self.base_addrees + '/' + item['symbol']
        log.msg(path, level = log.DEBUG, spider = spider)
       # print summary
        self.mkdir(path)
        f=open(path+'/'+item['timestr'], 'w')
        f.write("\n")
        f.writelines(item['content'])
        f.close();
        return item