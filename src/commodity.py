# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''


class Commodity(object):
    '''
    ��Ʒ
    '''

    def __init__(self, barcode, name, unit, unit_price, classification):
        '''
        Constructor
        '''
        self.barcode = barcode  # ������
        self.name = name  # ����
        self.unit = unit  # ��λ
        self.unit_price = unit_price  # ����
        self.classification = classification  # ���
