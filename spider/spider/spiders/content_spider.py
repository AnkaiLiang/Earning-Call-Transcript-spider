import scrapy
from scrapy.selector import Selector
import random
from scrapy_splash import SplashRequest


class DmozSpider(scrapy.Spider):
    name = "con"
    allowed_domains = ["seekingalpha.com"]
    start_urls = [
    ]
    base_url = "https://seekingalpha.com"
    base_addree = "/Users/kk/Documents/qyk/data/"
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
        f=open(self.base_addree + '/' + "list.txt", 'r')
        for line in f:
            self.start_urls.append(line)
        f.close()

        for url in self.start_urls:
            print "++++++++++++++" + url 
            yield scrapy.Request(url, self.parse_content, dont_filter=True, meta={
                'splash': {
                    'endpoint': "render.html",
                    'args': {'wait': 0.8},
                    'magic_response': True,
                  }
            })
          #  time.sleep(5)
         #   


    def parse_content(self, response):
        page = Selector(response)
        test = page.xpath('//p[@class="p p1"]/a/text()')
        if len(test) == 0:
            print "Error"
            return
        symbol = test.extract()[0]
        symbol = symbol.replace('/','-')
        #time = page.xpath('//time[@itemprop="datePublished"]/text()').extract()[0]
        time = page.xpath('//p[@class="p p1"]/text()').extract()[3]
        time = time.replace('/','-')
        content = "\n".join(page.xpath('//div[@id="a-body"]/p[@class]/text()').extract())

        #widget = page.xpath('//div[@id="earnings-widget"]')
        #summary_title = page.xpath('//div[@class="title"]/text()').extract()[0]
       # summary_title = summary_title.replace(':', ' ');
       # summary_title = "Earning summary" + " " + time
       # summary = "  ".join(page.xpath('//div[@class="data-line"]//text()').extract())
        
        path = self.base_addree + symbol
        print path
       # print summary
        self.mkdir(path)
        f=open(path+'/'+time, 'w')
        f.write("\n")
        f.writelines(content)
        f.close();
