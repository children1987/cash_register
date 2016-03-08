# coding: GBK
'''
Created on 2016��3��6��

@author: Administrator
'''
import cash_register


class OneReceiptInfo(object):
    '''
    ����СƱ�е�һ��������Ϣ
    '''

    def __init__(self, barcode, quantity):
        '''
        Constructor
        '''
        self.barcode = barcode  # ��Ʒ��������
        self.quantity = quantity  # ������ע�⣺Ŀǰ�����������������������
        self.unit_price = cash_register.get_commodity_unit_price(barcode)
        self.final_price = None  # Ϊ�˱����ظ����㣬�����Ч�ʣ���ʼ��ʱ�Ȳ��˳����
        self.saved_money = 0  # ��ʼ��Ϊint���Է����ж��Ƿ���ʡǮ
        self.quantity_get = 0
        self.is_discount_of_5_percent = False  # �Ƿ�Ϊ95����Ʒ
        self.is_buy_2_get_1 = False  # �Ƿ�Ϊ�����һ��Ʒ

    @staticmethod
    def _is_in_buy_2_get_1(barcode):
        return barcode in cash_register.on_sale_info["buy_2_get_1"]

    @staticmethod
    def _is_in_discount_of_5_percent(barcode):
        return barcode in cash_register.on_sale_info["discount_of_5_percent"]

    def _do_buy_2_get_1(self):
        '''
        ���������һ�Ĺ��򣬶Ա�������Ϣ����ת��
        '''
        remainder = self.quantity % 3
        self.quantity_get = (self.quantity-remainder) / 3
        self.quantity = self.quantity - self.quantity_get
        self.final_price = self.quantity * self.unit_price
        self.saved_money = self.quantity_get * self.unit_price

    def _do_discount_of_5_percent(self):
        '''
        ����95�۵Ĺ��򣬶Ա�������Ϣ����ת��
        '''
        self.final_price = self.unit_price * self.quantity
        final_price = self.final_price * 0.95
        self.saved_money = self.final_price - final_price
        self.final_price = final_price

    def calculate_final_price(self):
        '''
        ��ȡ����ʵ��Ӧ��֧����Ǯ��
        '''
        # barcode �Ƿ�μ������һ�
        if self._is_in_buy_2_get_1(self.barcode):
            self._do_buy_2_get_1()
            self.is_buy_2_get_1 = True
            return
        
        # barcode �Ƿ�μ�95�ۻ
        if self._is_in_discount_of_5_percent(self.barcode):
            self._do_discount_of_5_percent()
            self.is_discount_of_5_percent = True
            return
        
        # �����Żݶ�������ʱ�� self.final_price ��δ������Чֵ�������������һ��
        self.final_price = self.unit_price * self.quantity
