# -*- coding:utf-8 -*-

from spiders.caixin_spider import CaixingSpider
from spiders.ft_chinese_spider import FTChineseSpider
from spiders.zaker_spider import ZakerSpider
from spiders.jiemian_spider import JieMianSpider
from spiders.tech163_spider import Tech163Spider
from spiders.fi163_spider import Fi163Spider


def run_spiders():
    caixing_spider = CaixingSpider()
    caixing_spider.run()

    ft_chinese_spider = FTChineseSpider()
    ft_chinese_spider.run()

    zaker_spider = ZakerSpider()
    zaker_spider.run()

    jiemian_spider = JieMianSpider()
    jiemian_spider.run()

    tech163_spider = Tech163Spider()
    tech163_spider.run()

    fi163_spider = Fi163Spider()
    fi163_spider.run()


run_spiders()
