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

    # 将单词首字母大写，其余单词小写
    def str_change(self):
        listStr = ['adam', 'LISA', 'barT']

        print(isinstance(map(lambda x: x.capitalize(), listStr), Iterator))
        print(list(map(lambda x: x.capitalize(), listStr)))

    # filter函数
    # filter(funObj, IterableObj), funObj:函数对象，IterableObj:Iterable对象
    #   1.作用：把传入的函数作用于Iterable中的每个元素，然后根据返回值是True或False决定保留还是丢弃该元素
    def fileter_demo(self):
        listDemo = list(range(1,10))
        print(type(range(1, 10)))
        print(isinstance(range(1, 10), Iterator))
        print(isinstance(range(1, 10), tuple))
        print(isinstance(range(1, 10), set))
        print(isinstance(range(1, 10), range))

        # 筛选出偶数
        print(type(filter(lambda x: x%2==0, listDemo)))
        print(isinstance(filter(lambda x: x%2==0, listDemo), Iterator))
        print(list(filter(lambda x: x%2==0, listDemo)))

    # 把list中空值和空字符串删除
    def not_empty(self):
        listStr = ['A', ' ', None, ' ABC ']
        print('filter(lambda x: x and x.strip()):', list(filter(lambda x: x and x.strip(), listStr)))

    # # 求素数
    # # 1.构造一个奇数序列
    # @staticmethod
    # def odd_iter(self):
    #     n = 1
    #     while True:
    #         n += 2
    #         yield n
    # # 2.过滤函数
    # @staticmethod
    # def not_divisible(self, n):
    #     return lambda x: x%n > 0
    #
    # def primes(self):
    #     # 第一个素数是2
    #     yield 2
    #     # 构造一个奇数序列
    #     oddIter = HighFunction.odd_iter()
    #
    #     while True:
    #         n = next(oddIter)
    #         yield n
    #         # 过滤掉集合中n的倍数
    #         oddIter = filter(HighFunction.not_divisible(self, n), oddIter)


if __name__ == '__main__':
    highFun = HighFunction()

    highFun.map_demo()
    highFun.reduce_demo()
    highFun.map_reduc_demo()
    highFun.str_change()
    highFun.fileter_demo()
    highFun.not_empty()

    # for n in highFun.primes():
    #     if n < 100:
    #         print(n)
    #     else:
    #         break
