# -*- coding: utf-8 -*-
# @File  : ComprehensionDemo.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 列表生成式
class ComprehensionDemo(object):

    # 列表生成式
    print('list_compre............................................')
    def list_compre(self):
        rangeDemo = list(x*x for x in range(10))
        print(rangeDemo)

        rangeDemo1 = list(x*x for x in range(10) if x%2 == 0)
        print(rangeDemo1)

        # 使用两层循环
        rangeDemo2 = list(m + n for m in 'ABC' for n in 'CDE')
        print(len(rangeDemo2))
        print(rangeDemo2)

if __name__ == '__main__':
    comDemo = ComprehensionDemo()

    comDemo.list_compre()