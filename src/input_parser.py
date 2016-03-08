# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''
import json

from one_receipt_info import OneReceiptInfo
from receipt import Receipt


class InputShoppingListError(Exception):
    pass


class InputParser(object):
    '''
    ���������
    '''

    _DEFAULT_INPUT_FILE = r'input\input.json'

    @staticmethod
    def parse_line(s):
        '''
        ����һ��������Ϣ
        '''
        if '-' not in s:
            return s, 1

        try:
            barcode, quantity = s.split('-')
            quantity = int(quantity)
        except:
            raise InputShoppingListError('Input format err: {}'.format(s))
        return barcode, quantity

    @classmethod
    def parse(cls, input_file=_DEFAULT_INPUT_FILE):

        f = open(input_file)

        shopping_list = json.load(f, encoding='GBK')

        receipt = Receipt()

        for each in shopping_list:
            barcode, quantity = cls.parse_line(each)
            one_receipt_info = OneReceiptInfo(barcode, quantity)
            receipt.add(one_receipt_info)
        return receipt
