# -*- coding: utf-8 -*-
# @File  : HighFunction.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/11
# @Desc  : 高阶函数
from collections import Iterator, Iterable

from functools import reduce

class HighFunction(object):

    # map函数:
    # map(funObj, IteralbeObj):funObj：函数对象，IterableObj：Iterable对象
    #   1.作用：将传入的函数依次作用于iterable中的每个元素，然后返回一个新的Iterable对象
    #   2.map的返回值是Iterator类型，Iterator是一个惰性序列，因此可以通过list(IteratorObj)函数把它的整个序列计算出来并返回一个list
    def map_demo(self):
        # 求list中每个元素的平方
        listDemo = list(range(1, 5))
        print(listDemo)
        listDemoRes = map(lambda x: x*x, listDemo)

        print('map(lambda x: x*x, isinstance(IterableObj, Iterable)):', isinstance(listDemoRes, Iterable))
        print('map(lambda x: x*x, isinstance(listDemoRes, Iterator)):', isinstance(listDemoRes, Iterator))
        print('map(lambda x: x*x, type(listDemoRes)):', type(listDemoRes))
        print('map(lambda x: x*x, list(listDemoRes)):', list(listDemoRes))

    # reduce函数:
    # reduce(funObj, IterableObj),funObj：函数对象，IterableObj：Iterable对象
    #   1.作用：合并，根据fun函数将集合中元素进行合并
    #   2.
    def reduce_demo(self):
        listDemo = list(range(1, 5))
        reduceVal = reduce(lambda x, y: x+y, listDemo)
        reduceRes = reduce(lambda x, y: x*10+y, listDemo)

        print('reduce(lambda x, y: x+y, IterableObj):', reduceVal)
        print('type(reduce(lambda x, y: x+y)):', type(reduceVal))
        print(reduceRes)

    # 将一个str类型转换成int
    def map_reduc_demo(self):
        str = '1234'
        strInt = reduce(lambda x, y: x*10+y, map(lambda x: int(x), str))

        print('type(str):', type(str))
        print('type(strInt):', type(strInt))
        print('strInt:', strInt)

if __name__ == '__main__':
    highFun = HighFunction()

    highFun.map_demo()
    highFun.reduce_demo()
    highFun.map_reduc_demo()