# -*- coding: utf-8 -*-
from house_renting.spider_settings import lianjia, a58

BOT_NAME = 'house_renting'

COMMANDS_MODULE = 'house_renting.commands'
SPIDER_MODULES = ['house_renting.spiders']
NEWSPIDER_MODULE = 'house_renting.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 ' \
             'Safari/605.1.15 '

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 10

CONCURRENT_REQUESTS_PER_DOMAIN = 1

COOKIES_ENABLED = True

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# SPIDER_MIDDLEWARES = {
#    'house_renting.middlewares.HouseRentingSpiderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    'house_renting.middlewares.MyCustomDownloaderMiddleware': 543,
# }

ITEM_PIPELINES = {
    'house_renting.pipelines.HouseRentingPipeline': 100,
    'house_renting.pipelines.DuplicatesPipeline': 200,
    'scrapy.pipelines.images.ImagesPipeline': 300,
    'house_renting.pipelines.ESPipeline': 400,
}
IMAGES_STORE = '/house-renting/data/images'
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_LEVEL = 'DEBUG'

SPIDER_SETTINGS = {
    'lianjia': {
        'cities': lianjia.cities,
        'available_cities': lianjia.available_cities,
        'available_cities_map': lianjia.available_cities_map,
    },
    '58': {
        'cities': a58.cities,
        'available_cities': a58.available_cities,
        'available_cities_map': a58.available_cities_map,
    },
}
