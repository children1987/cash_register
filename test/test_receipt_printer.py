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
名称：苹果，数量：2斤，单价：5.50(元)，小计：10.45(元)，节省0.55(元)
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

    def test03(self):
        '''
        仅仅单种不参加活动的商品
        '''
        receipt = InputParser.parse(r'input\input03.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<没钱赚商店>购物清单***
名称：手表，数量：2块，单价：30000000.00(元)，小计：60000000.00(元)
----------------------
总计：60000000.00(元)
**********************
'''
        self.assertEquals(act, dst)

    def test04(self):
        '''
        购买的“买二送一”商品未达到赠送条件
        '''
        receipt = InputParser.parse(r'input\input04.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<没钱赚商店>购物清单***
名称：羽毛球，数量：2个，单价：1.00(元)，小计：2.00(元)
----------------------
总计：2.00(元)
**********************
'''
        self.assertEquals(act, dst)

    def test05(self):
        '''
        购买的“买二送一”商品达到赠送条件后，又多买了1个
        '''
        receipt = InputParser.parse(r'input\input05.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<没钱赚商店>购物清单***
名称：羽毛球，数量：4个，单价：1.00(元)，小计：3.00(元)
----------------------
买二赠一商品：
名称：羽毛球，数量：1个
----------------------
总计：3.00(元)
节省：1.00(元)
**********************
'''
        self.assertEquals(act, dst)

if __name__ == "__main__":
    unittest.main()
