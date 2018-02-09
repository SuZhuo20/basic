# -*- coding: utf-8 -*-
# @File  : GeneratorDemo.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 生成器
#       问题：
#           1.列表生成器可直接创建一个列表，但是收到内存限制列表中元素个数肯定是有限的，当创建一个大列表时可能会占用很大一部分内存，并且我们
#                   使用到的元素往往很少，从而造成内存浪费
#       解决办法：
#           1.记录列表中数据推算的算法，这样就不需要创建出完整的list，从而节约了内存，python中将这种一遍循环一个推算下个元素的机制成为生成器（generator）
class GeneratorDemo(object):
    pass

if __name__ == '__main__':
    genDemo = GeneratorDemo()