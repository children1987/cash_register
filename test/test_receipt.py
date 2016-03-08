# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''
import unittest

from one_receipt_info import OneReceiptInfo
from receipt import Receipt


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceipt_add(self):
        receipt = Receipt()

        barcode = "ITEM000001"
        one_receipt_info = OneReceiptInfo(barcode, 2)

        receipt.add(one_receipt_info)
        self.assertEquals(receipt.receipt_infos[barcode], 2)
        receipt.add(one_receipt_info)
        self.assertEquals(receipt.receipt_infos[barcode], 4)

if __name__ == "__main__":
    unittest.main()
