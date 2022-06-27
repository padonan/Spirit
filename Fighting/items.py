# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FightingItem(scrapy.Item):
    COMPANY = scrapy.Field()
    TITLE = scrapy.Field()
    CARRER = scrapy.Field()
    ACADEMIC_ABILILTY = scrapy.Field()
    EMPLOYMENT_TYPE = scrapy.Field()
    AREA = scrapy.Field()
    #RECUITMENT_TYPE = scrapy.Field()
    RECUITMENT_PERIOD = scrapy.Field()
    OTHER_CONTENTS = scrapy.Field()
    URL = scrapy.Field()
