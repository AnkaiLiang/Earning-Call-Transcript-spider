# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
RETRY_TIMES = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
BASE_ADDREES = '/User/kk/newdata'
ROBOTSTXT_OBEY = True
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5

ITEM_PIPELINES = {
    'spider.pipelines.SpiderPipeline': 300,
}

START_PAGE = 1075
END_PAGE = 4539
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 3
#CONCURRENT_REQUESTS_PER_IP = 3
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spider.middlewares.MyCustomSpiderMiddleware': 543,
#}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {  
#	        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,  
 #		'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : 810,  
 		'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 800,
#
#		'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 120,
 #		'scrapyjs.SplashCookiesMiddleware': 723,
  		'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware' : 722,
#		'scrapy_splash.SplashCookiesMiddleware': 723,
 #  		'scrapy_splash.SplashMiddleware': 725,
        	'spider.rotate_useragent.RotateUserAgentMiddleware' : 100,
 #     		'spider.proxyMiddleware.ProxyMiddleware' : 110,
#       'scrapyjs.SplashMiddleware': 725, 
   	} 

PROXY_LIST = [
	"69.161.24.54:3128",
	"192.95.18.162:8080",
	"104.196.226.56:80",
	"66.70.191.215:1080",
	"96.239.193.114:8080",
	"47.89.185.47:80",
	"47.52.24.117:80",
	"52.11.203.152:8083",
	"47.88.102.116:8118",
	"13.56.40.133:80",
	"168.128.29.75:80",
]
 
SPLASH_URL = 'http://localhost:8050'
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}
DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapyjs.SplashAwareFSCacheStorage'
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'