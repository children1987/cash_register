# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''


class Commodity(object):
    '''
    商品
    '''

    def __init__(self, barcode, name, unit, unit_price, classification):
        '''
        Constructor
        '''
        self.barcode = barcode  # 条形码
        self.name = name  # 名称
        self.unit = unit  # 单位
        self.unit_price = unit_price  # 单价
        self.classification = classification  # 类别
