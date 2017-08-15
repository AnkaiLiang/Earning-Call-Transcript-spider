# -*- coding: utf-8 -*-
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
    
    cookies = {
        "machine_cookie" : "1597911293506",
        "__utma" : "150447540.686697416.1502292088.1502522480.1502752784.6",
        "__utmz" : "150447540.1502292088.1.1.utmc…tmccn=(direct)|utmcmd=(none)",
        "_pxvid" : "6aeaba50-7d16-11e7-9f0d-352d58bfd5c4",
        "__gads" : "ID=630c0bb8b7dd8398:T=1502292…amUWgImwYQU6H9BpIy0-kT4NFWxw",
        "_igur" : "https://seekingalpha.com/earn…gs/earnings-call-transcripts",
        "u_voc" : "61",
        "ptac" : "",
        "marketplace_author_slugs" : "",
        "a_t" : "1ebtmi:1cp4cmu:803b2ea05c7bdf815429196b48ea01cb",
        "gk_user_access_sign" : "272338d02e9bf65a7f56cc905d7bba56e3a0a61c",
        "portfolio_sort_type" : "a_z",
        "trc_cookie_storage" : "taboola%20global%3Auser-id=4b…9f40-34ab0b220536-tuct84b176",
        "_igh" : "https://seekingalpha.com/arti…lts-earnings-call-transcript",
        "_ig_nump" : "22:2:11:11:0:4",
        "_ig" : "5dca3cc2-ca4c-42e0-a3d0-d264badf914a",
        'bknx_fa' : "1502752782754",
        "bknx_ss" : "1502752782754",
        "__utmb" : "150447540.7.9.1502752964442",
        "__utmc" : "150447540",
        "_px" : "9+sd81II3S+gb/b4n8TkH9ocOej44…4ybP6nnG6QuHDylBFMuMLrLPNA==",
        "_px2"  : "eyJ1IjoiNzlkOGVjNTAtODE0Ny0xM…M2UwZTIzNGQzNjU1YTE2ODA0In0=",
        "user_id" : "48625362",
        "user_nick" : "",
        "user_remember_token" : "12884154cccb40081f20620fb0cb065b51afbcba",
        "user_devices" : "",
        "user_cookie_key" : "addfc68e747530cbdc0c9c2874ec927bee6c8a9b",
        "sapu" : "101",
        "gk_user_access" : "1**1502753502"
    }


    def start_requests(self):
        baselisturl = "https://seekingalpha.com/earnings/earnings-call-transcripts"
        for k in range(settings['START_PAGE'], settings['END_PAGE']):
            newurl = baselisturl +'/' + str(k)
            self.start_urls.append(newurl)

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_page, cookies = self.cookies)



    def parse_page(self, response):
        page = Selector(response)
        for sel in page.xpath('//li[@class="list-group-item article"]'):
            href = self.base_url + sel.xpath('h3/a/@href').extract()[0]
    #        print href
            yield scrapy.Request(href, self.parse_item, cookies = self.cookies)

    def parse_item(self, response):
        page = Selector(response)
        item = SeekingalphaItem()
        symbolg = page.xpath('//p[@class="p p1"]/a/text()').extract()
        if len(symbolg) == 0:
            print "Error"
            return
        item['symbol'] = symbolg[0].replace(':','-').replace('/','-')
        #time = page.xpath('//time[@itemprop="datePublished"]/text()').extract()[0]
        timestr = page.xpath('//time[@itemprop="datePublished"]/text()').extract()[0]
        item['timestr'] = timestr.replace('/','-').replace(':',' ').replace('.',' ')
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