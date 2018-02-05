# -*- coding:utf-8 -*-

from spiders.caixin_spider import CaixingSpider
from spiders.wsj_spider import WSJSpider
from spiders.ft_chinese_spider import FTChineseSpider

caixing_spider = CaixingSpider()
caixing_spider.run()

wsj_spider = WSJSpider()
wsj_spider.run()

ft_chinese_spider = FTChineseSpider()
ft_chinese_spider.run()
