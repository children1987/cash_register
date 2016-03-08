# coding: GBK
'''
Created on 2016年3月8日

@author: Administrator
'''
import cash_register
from input_parser import InputParser
from receipt_printer import ReceiptPrinter


if __name__ == '__main__':
    receipt = InputParser.parse()
    rp = ReceiptPrinter(receipt)
    rp.print_receipt()
