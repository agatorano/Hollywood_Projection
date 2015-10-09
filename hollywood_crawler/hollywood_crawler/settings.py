BOT_NAME = 'hollywood_crawler'

SPIDER_MODULES = ['hollywood_crawler.spiders']
NEWSPIDER_MODULE = 'hollywood_crawler.spiders'

DOWNLOAD_HANDLERS = {
    's3': None,
    }

ITEM_PIPELINES = {
    'hollywood_crawler.pipelines.DuplicatesPipeline': 300,
    'hollywood_crawler.pipelines.Drop_Negative_Year': 400,
    'hollywood_crawler.pipelines.Drop_No_Budget': 500,
}
