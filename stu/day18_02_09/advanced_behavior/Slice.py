# -*- coding: utf-8 -*-
# @File  : Slice.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 切片
# 注意：
#   1.tuple也是一种list，只不过tuple中的元素不可变，在tuple中同样也可以使用切片
#   2.list使用切片后返回的依然是list，tuple使用切片后返回的依然是tuple
#   3.可以将str（字符串）看成一个list进行切片操作,返回值还是一个str,原str没有变只是返回了一个新的str
#           Python没有针对字符串的截取函数，只需要切片一个操作就可以完成
class Slice(object):
    # 取list中元素
    def slice_get(self):
        listDemo = ['zhangsan', 'lisi', 'wangwu', 'xiaoer']
        listNum = list(range(15))

        # listDemo
        print(listDemo)
        # 取list前三个元素
        print(listDemo[0], listDemo[1], listDemo[2])
        # 取list前n个元素
        tmp = []
        for index in range(3):
            tmp.append(listDemo[index])
        print('tmp:', tmp)
        print('*tmp:', *tmp)

        # 使用切片取list中元素
        print(listDemo[0:3])
        print(listDemo[0:])
        print(listDemo[:3])
        print(listDemo[-2:])
        print(listDemo[-2:-1])
        print(listDemo[-1])
        print('copy one list by listDemo[:]:', listDemo[:])

        # 隔一个元素取一次
        print('listNum[::2]:',listNum[::2])
        print('listNum[1:12:3]:', listNum[1:12:3])

        # tuple也是一种list，只不过tuple中的元素不可变，在tuple中同样也可以使用切片，list使用切片后返回的依然是list，tuple使用切片后返回的依然是tuple
        tupleDemo = tuple(range(10))
        print(tupleDemo)
        print('tupleDemo[::2]:', tupleDemo[::2])
        print('tupleDemo[-2:]:', tupleDemo[-2:])

        strVal = 'ABCDE'
        print('strVal[-2:]:', strVal[-2:])
        print('strVal:', strVal)
        print('type(strVal[-2:]):', type(strVal[-2:]))

if __name__ == '__main__':
    sliceDemo = Slice()

    sliceDemo.slice_get()