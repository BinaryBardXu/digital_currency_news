# -*- coding:utf-8 -*-

from spiders.caixin_spider import CaixingSpider
from spiders.wsj_spider import WSJSpider

caixingSpider = CaixingSpider()
caixingSpider.run()

wsjSpider = WSJSpider()
wsjSpider.run()
