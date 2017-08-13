import scrapy
from scrapy.selector import Selector
import random
import time


class DmozSpider(scrapy.Spider):
    name = "list"
    allowed_domains = ["seekingalpha.com"]
    start_urls = ["https://seekingalpha.com/earnings/earnings-call-transcripts"
    ]
    base_url = "https://seekingalpha.com"
    time = ""
    company = ""
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    base_addree = "/Users/kk/Documents/qyk/data/"

    def mkdir(self, path):
        import os
        isExists=os.path.exists(path)
     
        if not isExists:
            os.makedirs(path)
        return

    def start_requests(self):
        baselisturl = "https://seekingalpha.com/earnings/earnings-call-transcripts"
        for k in range(1, 10):
            newurl = baselisturl +'/' + str(k)
            self.start_urls.append(newurl)

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_page)



    def parse_page(self, response):
        
        f=open(self.base_addree + '/' + "list.txt", 'a')
        page = Selector(response)
        for sel in page.xpath('//li[@class="list-group-item article"]'):
            href = self.base_url + sel.xpath('h3/a/@href').extract()[0]
            f.write(href+"\n")
        f.close();

      #  p=open(path+'/'+summary_title, 'w')
       # p.write("\n")
       # p.writelines(summary)
       # p.close();

