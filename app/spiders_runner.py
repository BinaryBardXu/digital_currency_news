# -*- coding:utf-8 -*-

from app.spiders.caixin_spider import CaixingSpider
from app.spiders.ft_chinese_spider import FTChineseSpider
from app.spiders.zaker_spider import ZakerSpider
from app.spiders.jiemian_spider import JieMianSpider
from app.spiders.tech163_spider import Tech163Spider
from app.spiders.fi163_spider import Fi163Spider
from app.spiders.wallstreetcn_spider import WSJCNSpider
from app.spiders.infzm_spider import NFZMSpider


def run():
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

    wallstreetcn_spider = WSJCNSpider()
    wallstreetcn_spider.run()

    infzm_spider = NFZMSpider()
    infzm_spider.run()


run()
