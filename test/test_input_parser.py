# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''
import unittest

from input_parser import InputParser


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testParse01(self):
        receipt = InputParser.parse()
        print "�ϲ�������ӡ:"
        print receipt


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()