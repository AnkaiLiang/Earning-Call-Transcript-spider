# -*- coding: utf-8 -*-
"""
This a simple proxy for scrapy. 

The proxy host format like: `http://host:port` or `http://username:password@host:port`
"""

import random
from settings import PROXY_LIST

class ProxyMiddleware(object):
    """Custom ProxyMiddleware."""
#    def __init__(self, settings):
#        self.proxy_list = settings.get('PROXY_LIST')
#        with open(self.proxy_list) as f:
#            self.proxies = [ip.strip() for ip in f]

    def parse_request(self, request, spider):
        request.meta['proxy'] = 'http://{}'.format(random.choice(PROXY_LIST))