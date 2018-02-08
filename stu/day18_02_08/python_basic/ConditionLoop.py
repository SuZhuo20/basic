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
    def loopDemo(self):
        pass


if __name__ == '__main__':
    conLoop = ConditionLoop()

    conLoop.conditionDemo(100)