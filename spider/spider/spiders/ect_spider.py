import scrapy
from scrapy.selector import Selector
import random
import time


class DmozSpider(scrapy.Spider):
    name = "epo"
    allowed_domains = ["seekingalpha.com"]
    start_urls = ["https://seekingalpha.com/earnings/earnings-call-transcripts"
    ]
    base_url = "https://seekingalpha.com"
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def mkdir(self, path):
        import os
        isExists=os.path.exists(path)
     
        if not isExists:
            os.makedirs(path)
        return

    def start_requests(self):
        baselisturl = "https://seekingalpha.com/earnings/earnings-call-transcripts"
        for k in range(5, 500):
            newurl = baselisturl +'/' + str(k)
            self.start_urls.append(newurl)

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_page)



    def parse_page(self, response):
        page = Selector(response)
        for sel in page.xpath('//li[@class="list-group-item article"]'):
            href = self.base_url + sel.xpath('h3/a/@href').extract()[0]
    #        print href
            yield scrapy.Request(href, self.parse_content, meta={
                'splash': {
                    'endpoint': "render.html",
                    'args': {'wait': 0.8},
                    'magic_response': True,
                  }
            })

    def parse_content(self, response):
        page = Selector(response)
        symbolg = page.xpath('//p[@class="p p1"]/a/text()').extract()
        if len(symbolg) == 0:
            print "Error"
            time.sleep(5)
            return
        symbol = symbolg[0].replace('/','-')
        #time = page.xpath('//time[@itemprop="datePublished"]/text()').extract()[0]
        timestr = page.xpath('//p[@class="p p1"]/text()').extract()[3]
        timestr = timestr.replace('/','-')
        content = "\n".join(page.xpath('//div[@id="a-body"]/p[@class]/text()').extract())

        #widget = page.xpath('//div[@id="earnings-widget"]')
        #summary_title = page.xpath('//div[@class="title"]/text()').extract()[0]
       # summary_title = summary_title.replace(':', ' ');
       # summary_title = "Earning summary" + " " + time
       # summary = "  ".join(page.xpath('//div[@class="data-line"]//text()').extract())
        
        base_addree = "/Users/kk/Documents/qyk/data"
        path = base_addree + '/' + symbol
        print path
       # print summary
        self.mkdir(path)
        f=open(path+'/'+timestr, 'w')
        f.write("\n")
        f.writelines(content)
        f.close();

      #  p=open(path+'/'+summary_title, 'w')
       # p.write("\n")
       # p.writelines(summary)
       # p.close();

