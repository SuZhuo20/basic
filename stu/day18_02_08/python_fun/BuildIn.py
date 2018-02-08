# -*- coding: utf-8 -*-
# @File  : BuildIn.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/8
# @Desc  : 内置函数
class BuildIn(object):

    # python内置函数
    def buildInFun(self):
        print('abs(-1):', abs(-1))
        a = abs
        print(a(-4))

        print('max(val...):', max([1, 3, 9]))

        print('min(val...):', min([3, 1, 0, -4]))

        print('int(\'23\'):', int('23'))

        print('float(\'23\'):', float(23))

        print('str(23):', str(23))

        print('bool(\'\'):', bool(''))

        print('bool(\'1\'):', bool(1))

        print('bool(None):', bool(None))

        print('type(1):', type(1))

        print('isinstance(1, int):', isinstance(1, int))

        print('打印一个对象或类中的内容dir(object/Class):', dir(BuildIn))

if __name__ == '__main__':
    buildIn = BuildIn()

    buildIn.buildInFun()