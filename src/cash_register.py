# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''
import json

from commodity import Commodity


# ����ģʽ
# ˵����python�У�ģ�飨module����ȫ��Ψһ�ģ���˿�������һ����ʵ��һ������ģʽ��
# ������Ҫɶ���ԡ�������ֱ�Ӹ��ȫ�ֵľͿ�����
# �����ļ�Ĭ��·��
DEFAULT_CFG_FILE = r'cfg\cfg.json'

# ȫ����Ʒ��Ϣ
commodities = {}

# ȫ��������Ϣ
on_sale_info = {
    "buy_2_get_1": [],  # �����һ�����ȼ�����
    "discount_of_5_percent": []  # 95�ۣ����ȼ�����
}

# ������Ϣ
_cfg_info = None


def set_cfg_file(f):
    global DEFAULT_CFG_FILE
    DEFAULT_CFG_FILE = f
    _read_cfg_info(DEFAULT_CFG_FILE)


def _read_cfg_info(cfg_file=None):
    '''
    ��ȡ������Ϣ
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
    ��ȡ��Ʒ�ĵ�����Ϣ
    '''
    return commodities[barcode].unit_price


def inquire_commodity(barcode, attr):
    '''
    ��ѯ������Ϊ barcode ����Ʒ�� attr ����
    '''
    return getattr(commodities[barcode], attr)


def _init():
    '''
    ģ���ʼ����������������ʼ��
    '''
    _read_cfg_info()


# ��ʼ������ģ��
_init()
