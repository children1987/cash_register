# coding: GBK
'''
Created on 2016��3��6��

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
        dst = '''***<ûǮ׬�̵�>�����嵥***
���ƣ��ɿڿ��֣�������3ƿ�����ۣ�3.00(Ԫ)��С�ƣ�6.00(Ԫ)
���ƣ�ƻ����������2����ۣ�5.50(Ԫ)��С�ƣ�10.45(Ԫ)����ʡ0.55(Ԫ)
���ƣ���ë��������6�������ۣ�1.00(Ԫ)��С�ƣ�4.00(Ԫ)
----------------------
�����һ��Ʒ��
���ƣ��ɿڿ��֣�������1ƿ
���ƣ���ë��������2��
----------------------
�ܼƣ�20.45(Ԫ)
��ʡ��5.55(Ԫ)
**********************
'''
        self.assertEquals(act, dst)

    def test02(self):
        receipt = InputParser.parse(r'input\input02.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<ûǮ׬�̵�>�����嵥***
���ƣ���ë��������6�������ۣ�1.00(Ԫ)��С�ƣ�4.00(Ԫ)
----------------------
�����һ��Ʒ��
���ƣ���ë��������2��
----------------------
�ܼƣ�4.00(Ԫ)
��ʡ��2.00(Ԫ)
**********************
'''
        self.assertEquals(act, dst)

    def test03(self):
        '''
        �������ֲ��μӻ����Ʒ
        '''
        receipt = InputParser.parse(r'input\input03.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<ûǮ׬�̵�>�����嵥***
���ƣ��ֱ�������2�飬���ۣ�30000000.00(Ԫ)��С�ƣ�60000000.00(Ԫ)
----------------------
�ܼƣ�60000000.00(Ԫ)
**********************
'''
        self.assertEquals(act, dst)

    def test04(self):
        '''
        ����ġ������һ����Ʒδ�ﵽ��������
        '''
        receipt = InputParser.parse(r'input\input04.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<ûǮ׬�̵�>�����嵥***
���ƣ���ë��������2�������ۣ�1.00(Ԫ)��С�ƣ�2.00(Ԫ)
----------------------
�ܼƣ�2.00(Ԫ)
**********************
'''
        self.assertEquals(act, dst)

    def test05(self):
        '''
        ����ġ������һ����Ʒ�ﵽ�����������ֶ�����1��
        '''
        receipt = InputParser.parse(r'input\input05.json')
        rp = ReceiptPrinter(receipt)
        act = rp.print_receipt()
        dst = '''***<ûǮ׬�̵�>�����嵥***
���ƣ���ë��������4�������ۣ�1.00(Ԫ)��С�ƣ�3.00(Ԫ)
----------------------
�����һ��Ʒ��
���ƣ���ë��������1��
----------------------
�ܼƣ�3.00(Ԫ)
��ʡ��1.00(Ԫ)
**********************
'''
        self.assertEquals(act, dst)

if __name__ == "__main__":
    unittest.main()
