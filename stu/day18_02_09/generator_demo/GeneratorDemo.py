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
#       适用场景：
#           1.当某些元素可以根据指定算法推算出来时就可以使用生成器
class GeneratorDemo(object):

    # 创建生成器
    print('create_generator............................................')
    def create_generator(self):
        # 创建list
        listDemo = [x for x in range(10)]
        print('type [x for x in range(10)]:', type(listDemo))
        # 创建生成器,在generator中保存的是算法
        genDemo = (x for x in range(10))
        print('type (x for x in range(10)):', type(genDemo))
        # genDemo中元素
        print('next(generatorObj):', next(genDemo))
        # 使用for循环遍历generator中的所有元素
        for num in genDemo:
            print(num)

    # 使用生成器实现斐波那契数列，定义一个
    def fibonacci(self, max):
        a, b, n = 0, 1, 0

        while n < max:
            yield b
            a, b = b, a+b
            n += 1

if __name__ == '__main__':
    genDemo = GeneratorDemo()

    genDemo.create_generator()