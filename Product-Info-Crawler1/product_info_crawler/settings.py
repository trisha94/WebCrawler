
BOT_NAME = 'product_info_crawler'

SPIDER_MODULES = ['product_info_crawler.spiders']
NEWSPIDER_MODULE = 'product_info_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'product_info_crawler (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# output data format
FEED_FORMAT = "csv"
FEED_URI = "tmp/%(name)s.csv"

# Enable logs to see scrapy logs in command line
LOG_ENABLED=False

# Max deptth to crawl
DEPTH_LIMIT=2
FEED_EXPORT_FIELDS=["product_name", "price", "source", "product_url","image_url"]
