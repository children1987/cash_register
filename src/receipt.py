# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''


class Receipt(object):
    '''
    СƱ
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.receipt_infos = {}  # һ��СƱ�е�����ԭʼ������Ϣ��{��Ʒ: ����}

    def add(self, one_receipt_info):
        barcode = one_receipt_info.barcode
        if barcode in self.receipt_infos:
            self.receipt_infos[barcode] += one_receipt_info.quantity
        else:
            self.receipt_infos[barcode] = one_receipt_info.quantity

    def __str__(self):
        return str(self.receipt_infos)
