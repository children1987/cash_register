# coding: GBK
'''
Created on 2016年3月7日

@author: Administrator
'''
import unittest

from one_receipt_info import OneReceiptInfo
import cash_register


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_calculate_final_price_buy_2_get_1_01(self):
        '''
        满足买2赠1
        '''
        barcode = "ITEM000001"
        quantity = 3
        ori = OneReceiptInfo(barcode, quantity)
        ori.calculate_final_price()
        final_price = ori.final_price
        delta = 0.001
        aim_final_price = cash_register.get_commodity_unit_price(barcode) * 2
        self.assertTrue(final_price < aim_final_price+delta)
        self.assertTrue(final_price > aim_final_price-delta)

    def test_calculate_final_price_buy_2_get_1_02(self):
        '''
        不满足买2赠1
        '''
        barcode = "ITEM000001"
        quantity = 2
        ori = OneReceiptInfo(barcode, quantity)
        ori.calculate_final_price()
        final_price = ori.final_price
        delta = 0.001
        aim_final_price = cash_register.get_commodity_unit_price(barcode) * 2
        self.assertTrue(final_price < aim_final_price+delta)
        self.assertTrue(final_price > aim_final_price-delta)


    def test_calculate_final_price_buy_2_get_1_03(self):
        '''
        买2赠1后有余数
        '''
        barcode = "ITEM000001"
        quantity = 4
        ori = OneReceiptInfo(barcode, quantity)
        ori.calculate_final_price()
        final_price = ori.final_price
        delta = 0.001
        aim_final_price = cash_register.get_commodity_unit_price(barcode) * 3
        self.assertTrue(final_price < aim_final_price+delta)
        self.assertTrue(final_price > aim_final_price-delta)

    def test_calculate_final_price_discount_of_5_percent_01(self):
        '''
        95折
        '''
        barcode = "ITEM000003"
        quantity = 7
        ori = OneReceiptInfo(barcode, quantity)
        ori.calculate_final_price()
        final_price = ori.final_price
        delta = 0.001
        aim_final_price = cash_register.get_commodity_unit_price(barcode) * quantity * 0.95
        self.assertTrue(final_price < aim_final_price+delta)
        self.assertTrue(final_price > aim_final_price-delta)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()