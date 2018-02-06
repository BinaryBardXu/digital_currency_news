# -*- coding:utf-8 -*-

from spiders.caixin_spider import CaixingSpider
from spiders.ft_chinese_spider import FTChineseSpider
from spiders.zaker_spider import ZakerSpider
from spiders.jiemian_spider import JieMianSpider

caixing_spider = CaixingSpider()
caixing_spider.run()

ft_chinese_spider = FTChineseSpider()
ft_chinese_spider.run()

zaker_spider = ZakerSpider()
zaker_spider.run()

jiemian_spider = JieMianSpider()
jiemian_spider.run()
