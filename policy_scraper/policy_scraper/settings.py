# Scrapy settings for policy_scraper project
import os

BOT_NAME = "policy_scraper"

SPIDER_MODULES = ["policy_scraper.spiders"]
NEWSPIDER_MODULE = "policy_scraper.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1  # Introduced to prevent rate-limiting
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Override the default request headers
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "policy_scraper (+https://www.example.com)",  # Customize User-Agent
}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 590,
}

# Configure item pipelines
ITEM_PIPELINES = {
    "policy_scraper.pipelines.BytesToBase64Pipeline": 300,  # Pipeline to handle bytes conversion
    "policy_scraper.pipelines.PolicyScraperPipeline": 400,  # Custom pipeline for saving files
}

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Retry settings for robustness
RETRY_ENABLED = True
RETRY_TIMES = 3  # Retry up to 3 times for failed requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# Dynamically set the root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# File storage directories updated to point to the data folder
FILES_STORE = os.path.join(BASE_DIR, "data", "raw", "files")        # Directory to save downloaded files
PDF_STORE = os.path.join(BASE_DIR, "data", "raw", "pdfs")           # Directory specifically for PDFs
POLICY_STORE = os.path.join(BASE_DIR, "data", "raw", "policies")   

# JSON output settings
FEEDS = {
    "output.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "indent": 4,
    },
}

# Logging
LOG_LEVEL = "INFO"  # Set to "DEBUG" for more detailed output during development

# Handle ignored content types
IGNORED_CONTENT_TYPES = ["image/jpeg", "image/png"]  # Add types to ignore as necessary

# Twisted reactor configuration
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Export encoding for consistent file formats
FEED_EXPORT_ENCODING = "utf-8"
