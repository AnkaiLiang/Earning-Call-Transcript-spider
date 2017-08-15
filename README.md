# Web Crawler Scrapy of Earning-Call-Transcript
## Description
	This spider will crawl the content of Earning-Call-Transcript in "seekingalpha.com", and make a file with the published time in a folder named by 'symbor' for each Earning-Call-Transcript.
## Usage
1. Install Scrapy
  - [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)
2. Download this program

	```
	git clone https://github.com/AnkaiLiang/Earning-Call-Transcript-spider.git'
	```
3. Setting the attribute in setting.py

	```python
	DOWNLOAD_DELAY = 1
	BASE_ADDREES = '/home/ubuntu/newdata'
	START_PAGE = 1075
	END_PAGE = 4539	
	```
4. This scrapy crawler used cookie and proxy ip to login. If this cookie lose efficacy， you should modify 'cookie' in `ect_spider.py`. If the proxy ip lose efficacy, modify it in `setting.py`

5. Run the spider under the directory '/spider'

	```
	scrapy crawl ect
	```