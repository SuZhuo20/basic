# -*- coding: utf-8 -*-
# @File  : ParameterFun.py
# @Author: Zhuozhuo.Geng
# @Date  : 18/2/9 00:25
# @Desc  : 函数参数
class ParameterFun(object):
    # 位置参数
    def parameter_position(self, num, n):
        mul = 1

        while n > 0:
            mul *= num
            n -= 1

        return mul

    # 默认参数函数
    # 设置默认参数时注意事项：
    #   1.必选参数在前，默认参数在后
    #   2.如何设置默认参数：当函数有多个参数时，把变化大的放到前面，变化小的设置成默认参数放到后面
    def def_parameter(self, num, n=3):
        mul = 1

        while n > 0:
            mul *= num
            n -= 1

        return mul

if __name__ == '__main__':
    paramFun = ParameterFun()

    print(paramFun.parameter_position(2, 3))

    print(paramFun.def_parameter(3))
    print(paramFun.def_parameter(3, 2))
    print(paramFun.def_parameter(n=4, num=2))