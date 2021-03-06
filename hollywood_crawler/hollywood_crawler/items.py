from scrapy.item import Item, Field


class HollywoodItem(Item):

    name = Field()
    years_active = Field()
    average_gross = Field()
    movie_count = Field()
    budgets = Field()
    stop = Field()
