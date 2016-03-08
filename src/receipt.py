# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''


class Receipt(object):
    '''
    小票
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.receipt_infos = {}  # 一个小票中的所有原始购物信息，{商品: 数量}

    def add(self, one_receipt_info):
        barcode = one_receipt_info.barcode
        if barcode in self.receipt_infos:
            self.receipt_infos[barcode] += one_receipt_info.quantity
        else:
            self.receipt_infos[barcode] = one_receipt_info.quantity

    def __str__(self):
        return str(self.receipt_infos)
