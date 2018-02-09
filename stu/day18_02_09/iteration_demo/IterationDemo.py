# -*- coding: utf-8 -*-
# @File  : IterationDemo.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 迭代
#           注意：
#               1.在python中迭代不仅仅可以用在list和tuple上，只要是迭代对象无论是有无下标都可以进行迭代操作如dict也可以进行迭代操作
#               2.判断某个对象是否是Iterable对象，使用collections中的Iterable isinstance(obj, Iterable)

from collections import Iterable

class IterationDemo(object):

    # list使用迭代
    def iteration_list(self):
        listDemo = list(range(10))
        for num in listDemo:
            print(num)

    # 对tuple使用迭代
    def iteration_tuple(self):
        tupleDemo = tuple(range(10))
        for num in tupleDemo:
            print(num)

    # 对dict使用迭代
    def iteration_dict(self):
        dictDemo = {'name':'suzhuo', 'age':24, 'city':'DaLian'}

        if not isinstance(dictDemo, Iterable):
            raise TypeError('dict isn\'t Iterable type')
        # 遍历dict所有的key
        print('dict key .....................................')
        for eleKey in dictDemo:
            print(eleKey)

        # 遍历dict所有的value
        print('dict value....................................')
        for eleVal in dictDemo.values():
            print(eleVal)

        # 已key-value形式遍历dict
        print('key-value.....................................')
        itemsVal = dictDemo.items()
        print('itemsVal:', itemsVal)
        print('type(dictObj.items()):', type(dictDemo.items()))
        for eleKey, eleVal in dictDemo.items():
            print(eleKey, ' ', eleVal)

        listTuple = [('name', 'suzhuo'), ('age', 24), ('city', 'DaLian')]
        print('listTuple.....................................')
        for key, val in listTuple:
            print(key, '=', val)

        strVal = 'ABCD'
        print('str...........................................')
        if not isinstance(strVal, Iterable):
            raise TypeError('str is\'t Iterable type')
        for chVal in strVal:
            print(chVal)

        # 打印出list中元素对应的下标及内容(index-value)
        print('enumerate.....................................')
        listNums = ['name', 'age', 'city']
        enumList = enumerate(listNums)
        print(type(enumList))
        for eleIndex, eleVal in enumerate(listNums):
            print(eleIndex, '-', eleVal)

    # 对set使用迭代
    print('set_iteration.....................................')
    def iteration_set(self):
        setVal = (1, 2, 4)
        for val in setVal:
            print(val)

    # 使用迭代获取list中最大值和最小值，并以元组返回
    def get_max_min(self):
        listDemo = [0, 4, 9, 24]
        maxVal = listDemo[0]
        minVal = listDemo[0]

        for num in listDemo:
            if maxVal < num:
                maxVal = num
            if minVal > num:
                minVal = num

        return (maxVal, minVal)

if __name__ == '__main__':
    iterationDemo = IterationDemo()

    iterationDemo.iteration_dict()
    print(iterationDemo.get_max_min())
    iterationDemo.iteration_set()