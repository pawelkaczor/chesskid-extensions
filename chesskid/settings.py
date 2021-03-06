# Scrapy settings for chesskid project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'chesskid'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['chesskid.spiders']
NEWSPIDER_MODULE = 'chesskid.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'chesskid.pipelines.DuplicatesPipeline'
    # 'chesskid.pipelines.CsvExportPipeline'
]