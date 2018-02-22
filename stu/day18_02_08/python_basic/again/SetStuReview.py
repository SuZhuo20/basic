# -*- coding: utf-8 -*-
# @File  : SetStuReview.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/22
# @Desc  : python集合复习
class SetStuReview(object):

    def listDemo(self):
        listDemo = [1, 'A', 'BCD', 12.9, True]

        print(len(listDemo))
        print(listDemo[1])
        print(listDemo[-1])
        print(listDemo.append(False))
        print(dir(listDemo))
        print(listDemo.insert(2, 'newVal'))
        print(listDemo.pop())
        print(listDemo.pop(2))

    def tupleDemo(self):
        classmates = ('suzhuo', 'lisi', 2, True, 12.9)

        print(classmates[0])
        print(classmates.count(3))
        print(classmates.index(2))

    def dictDemo(self):
        dictDemo = {'name':'suzhuo', 'age':24}

        print(dictDemo)
        print(dictDemo['age'])
        print(dictDemo.get('name2', -1))
        print(dictDemo.pop('age'))
        print(dictDemo)
        print(type(dictDemo))
        print(isinstance(dictDemo, dict))

    def setDemo(self):
        setDemo = set([1, 'A'])
        setDemo2 = set([2, 'b', 'A'])

        print(setDemo & setDemo2)
        print(setDemo | setDemo2)

if __name__ == '__main__':
    setStuReview = SetStuReview()

    setStuReview.listDemo()
    setStuReview.tupleDemo()
    setStuReview.dictDemo()
    setStuReview.setDemo()
