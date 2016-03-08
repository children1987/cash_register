# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''
import json

from commodity import Commodity


# 单例模式
# 说明：python中，模块（module）是全局唯一的，因此可利用这一点来实现一个单例模式，
# 即，需要啥属性、方法，直接搞成全局的就可以了
# 配置文件默认路径
DEFAULT_CFG_FILE = r'cfg\cfg.json'

# 全部商品信息
commodities = {}

# 全部打折信息
on_sale_info = {
    "buy_2_get_1": [],  # 买二赠一，优先级：高
    "discount_of_5_percent": []  # 95折，优先级：低
}

# 配置信息
_cfg_info = None


def set_cfg_file(f):
    global DEFAULT_CFG_FILE
    DEFAULT_CFG_FILE = f
    _read_cfg_info(DEFAULT_CFG_FILE)


def _read_cfg_info(cfg_file=None):
    '''
    读取配置信息
    '''
    if cfg_file is None:
        cfg_file = DEFAULT_CFG_FILE

    try:
        f = open(cfg_file)
    except IOError:
        print 'info: get cfg file failed!'
        print 'cash_register.set_cfg_file() must be called later!'
        return

    global _cfg_info
    _cfg_info = json.load(f, encoding='GBK')

    global on_sale_info
    on_sale_info = _cfg_info["on_sale_info"]

    global commodities
    for each in _cfg_info["commodities"]:
        commodity = Commodity(
            each['barcode'].encode('GBK'),
            each['name'].encode('GBK'),
            each['unit'].encode('GBK'),
            float(each['unit_price']),
            each['classification'].encode('GBK')
        )
        commodities[each['barcode']] = commodity


def get_commodity_unit_price(barcode):
    '''
    获取商品的单价信息
    '''
    return commodities[barcode].unit_price


def inquire_commodity(barcode, attr):
    '''
    查询条形码为 barcode 的商品的 attr 属性
    '''
    return getattr(commodities[barcode], attr)


def _init():
    '''
    模块初始化，即，收银机初始化
    '''
    _read_cfg_info()


# 初始化单例模块
_init()
