# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''
import unittest

import cash_register


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSingleton02(self):
        self.assertEquals(len(cash_register.commodities), 4)


if __name__ == "__main__":
    unittest.main()
