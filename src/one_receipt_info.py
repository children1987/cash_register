# coding: GBK
'''
Created on 2016年3月6日

@author: Administrator
'''
import cash_register


class OneReceiptInfo(object):
    '''
    购物小票中的一条购物信息
    '''

    def __init__(self, barcode, quantity):
        '''
        Constructor
        '''
        self.barcode = barcode  # 商品的条形码
        self.quantity = quantity  # 数量。注意：目前仅仅考虑它室整数的情况！
        self.unit_price = cash_register.get_commodity_unit_price(barcode)
        self.final_price = None  # 为了避免重复计算，以提高效率，初始化时先不乘出结果
        self.saved_money = 0  # 初始化为int，以方便判断是否有省钱
        self.quantity_get = 0
        self.is_discount_of_5_percent = False  # 是否为95折商品
        self.is_buy_2_get_1 = False  # 是否为买二赠一商品

    @staticmethod
    def _is_in_buy_2_get_1(barcode):
        return barcode in cash_register.on_sale_info["buy_2_get_1"]

    @staticmethod
    def _is_in_discount_of_5_percent(barcode):
        return barcode in cash_register.on_sale_info["discount_of_5_percent"]

    def _do_buy_2_get_1(self):
        '''
        按照买二赠一的规则，对本购物信息进行转换
        '''
        remainder = self.quantity % 3
        self.quantity_get = (self.quantity-remainder) / 3
        self.quantity = self.quantity - self.quantity_get
        self.final_price = self.quantity * self.unit_price
        self.saved_money = self.quantity_get * self.unit_price

    def _do_discount_of_5_percent(self):
        '''
        按照95折的规则，对本购物信息进行转换
        '''
        self.final_price = self.unit_price * self.quantity
        final_price = self.final_price * 0.95
        self.saved_money = self.final_price - final_price
        self.final_price = final_price

    def calculate_final_price(self):
        '''
        获取最终实际应该支付的钱数
        '''
        # barcode 是否参加买二赠一活动
        if self._is_in_buy_2_get_1(self.barcode):
            self._do_buy_2_get_1()
            self.is_buy_2_get_1 = True
            return
        
        # barcode 是否参加95折活动
        if self._is_in_discount_of_5_percent(self.barcode):
            self._do_discount_of_5_percent()
            self.is_discount_of_5_percent = True
            return
        
        # 两种优惠都不满足时， self.final_price 还未被赋有效值，所以这里计算一把
        self.final_price = self.unit_price * self.quantity
