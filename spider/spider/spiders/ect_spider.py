import scrapy
from scrapy.selector import Selector
from spider.items import SeekingalphaItem
import random
from scrapy.conf import settings
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


    def start_requests(self):
        baselisturl = "https://seekingalpha.com/earnings/earnings-call-transcripts"
        for k in range(settings['START_PAGE'], 4537):
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
                    'args': {'wait': 0.5},
                    'magic_response': True,
                  }
            })

    def parse_content(self, response):
        page = Selector(response)
        item = SeekingalphaItem()
        symbolg = page.xpath('//p[@class="p p1"]/a/text()').extract()
        if len(symbolg) == 0:
            print "Error"
            return
        item['symbol'] = symbolg[0].replace('/','-')
        #time = page.xpath('//time[@itemprop="datePublished"]/text()').extract()[0]
        timestr = page.xpath('//p[@class="p p1"]/text()').extract()[3]
        item['timestr'] = timestr.replace('/','-')
        item['content'] = "\n".join(page.xpath('//div[@id="a-body"]/p[@class]/text()').extract())
        yield item
        #widget = page.xpath('//div[@id="earnings-widget"]')
        #summary_title = page.xpath('//div[@class="title"]/text()').extract()[0]
       # summary_title = summary_title.replace(':', ' ');
       # summary_title = "Earning summary" + " " + time
       # summary = "  ".join(page.xpath('//div[@class="data-line"]//text()').extract())
        

      #  p=open(path+'/'+summary_title, 'w')
       # p.write("\n")
       # p.writelines(summary)
       # p.close();

