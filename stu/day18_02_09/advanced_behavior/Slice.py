# -*- coding: utf-8 -*-
# @File  : Slice.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 切片
class Slice(object):
    # 取list中元素
    def slice_get(self):
        listDemo = ['zhangsan', 'lisi', 'wangwu', 'xiaoer']
        listNum = list(range(10))

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


if __name__ == '__main__':
    sliceDemo = Slice()

    sliceDemo.slice_get()