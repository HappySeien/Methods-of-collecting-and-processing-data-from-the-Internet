"""Spiders manual runner."""

import sys
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from books_scrape import settings
from books_scrape.spiders.labirintru import LabirintruSpider



def _main():
    """Entry point."""
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabirintruSpider)

    process.start()


if __name__ == '__main__':
    sys.exit(_main())