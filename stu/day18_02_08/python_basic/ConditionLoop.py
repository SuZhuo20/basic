# -*- coding: utf-8 -*-
# @File  : ConditionLoop.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/8
# @Desc  : python中条件和循环练习
class ConditionLoop(object):

    # 条件练习
    def conditionDemo(self, age):
        if age > 80:
            print('>80')
        elif age >  60:
            print('>60')
        else:
            print('<=60')

    # 循环练习
    def loopDemo(self, maxVal):
        print('for.............')
        # range(5):生成5以内的数字不包含5
        forDemo = list(range(5))
        for intVal in forDemo:
            if intVal % 2 == 0:
                continue
            print(intVal)

        print('while.............')
        num = 0
        while num < 5:
            if num == 3:
                break
            print(num)
            num += 1

        # 斐波那契数列
        print('斐波那契数列........')
        a, b, n = 0, 1, 0
        while n < maxVal:
            print(b)
            a, b = b, a+b
            n += 1



if __name__ == '__main__':
    conLoop = ConditionLoop()

    conLoop.conditionDemo(100)
    conLoop.loopDemo(5)