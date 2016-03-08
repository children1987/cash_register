# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''
import cash_register
from one_receipt_info import OneReceiptInfo


class ReceiptPrinter(object):
    '''
    小票打印机
    仅负责打印，相当于MVC模式中的V
    '''

    _MAIN_TEMPLATE = '''***<没钱赚商店>购物清单***
{}
{}----------------------
总计：{:.2f}(元){}
**********************
'''

    _ONE_RECEIPT_TEMPLATE = '名称：{}，数量：{}{}，单价：{:.2f}(元)，小计：{:.2f}(元){}'

    _BUY_2_GET_1_TEMPLATE = '''----------------------
买二赠一商品：
{}
'''

    _ONE_BUY_2_GET_1_TEMPLATE = '名称：{}，数量：{}{}'

    def __init__(self, receipt):
        '''
        Constructor
        '''
        self.receipt = receipt

    def print_receipt(self):
        is_saved_money = False  # 是否有省钱
        sum_saved_money = 0.0
        sum_money = 0.0

        receipts = []
        buy_2_get_1_s = []
        for barcode, quantity in self.receipt.receipt_infos.iteritems():
            name = cash_register.inquire_commodity(barcode, 'name')
            unit = cash_register.inquire_commodity(barcode, 'unit')
            unit_price = cash_register.inquire_commodity(barcode, 'unit_price')

            ori = OneReceiptInfo(barcode, quantity)
            ori.calculate_final_price()
            final_price = ori.final_price
            saved_money = ori.saved_money
            is_saved_money = True if saved_money > 0 else False
            sum_saved_money += saved_money
            sum_money += final_price

            saved_str = ''
            if ori.is_discount_of_5_percent:
                saved_str = '，节省{:.2f}(元)'.format(saved_money)

            if ori.is_buy_2_get_1:
                buy_2_get_1_str = self._ONE_BUY_2_GET_1_TEMPLATE.format(
                    name, ori.quantity_get, unit)
                buy_2_get_1_s.append(buy_2_get_1_str)

            one_receipt = self._ONE_RECEIPT_TEMPLATE.format(
                name, quantity, unit, unit_price, final_price, saved_str)
            receipts.append(one_receipt)

        total_saved_str = ''
        if is_saved_money:
            total_saved_str = '\n节省：{:.2f}(元)'.format(sum_saved_money)

        all_buy_2_get_1_str = ''
        if buy_2_get_1_s:
            all_buy_2_get_1_str = self._BUY_2_GET_1_TEMPLATE.format(
                '\n'.join(buy_2_get_1_s))

        output_str = self._MAIN_TEMPLATE.format(
            '\n'.join(receipts), all_buy_2_get_1_str,
            sum_money, total_saved_str)

        print output_str
        return output_str
