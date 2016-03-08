# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''
import unittest

from input_parser import InputParser
from receipt_printer import ReceiptPrinter


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test01(self):
        receipt = InputParser.parse()
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<没钱赚商店>购物清单***
名称：可口可乐，数量：3瓶，单价：3.00(元)，小计：6.00(元)
名称：苹果，数量：2斤，单价：5.50(元)，小计：10.45(元)，节省：0.55(元)
名称：羽毛球，数量：6个，单价：1.00(元)，小计：4.00(元)
----------------------
买二赠一商品：
名称：可口可乐，数量：1瓶
名称：羽毛球，数量：2个
----------------------
总计：20.45(元)
节省：5.55(元)
**********************
'''
        self.assertEquals(act, dst)

    def test02(self):
        receipt = InputParser.parse(r'input\input02.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<没钱赚商店>购物清单***
名称：羽毛球，数量：6个，单价：1.00(元)，小计：4.00(元)
----------------------
买二赠一商品：
名称：羽毛球，数量：2个
----------------------
总计：4.00(元)
节省：2.00(元)
**********************
'''
        self.assertEquals(act, dst)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
