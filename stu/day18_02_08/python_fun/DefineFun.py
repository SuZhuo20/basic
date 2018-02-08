# -*- coding: utf-8 -*-
# @File  : DefineFun.py
# @Author: Zhuozhuo.Geng
# @Date  : 18/2/9 00:04
# @Desc  : 定义函数
class DefineFun(object):

    # 自定义abs()函数
    def my_abs(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('type error, value is not (int, float)')
        if value < 0:
            return -value

        return value

    # 返回多个值
    def return_mul_value(self):
        return 2, 'A', True

if __name__ == '__main__':
    defineFun = DefineFun()

    print(defineFun.my_abs(-4.5))
    # print(defineFun.my_abs('-4.5'))
    returnVal = defineFun.return_mul_value()
    print(returnVal)
    print(type(returnVal))

    num, num2, num3 = defineFun.return_mul_value()
    print(num, num2, num3)

