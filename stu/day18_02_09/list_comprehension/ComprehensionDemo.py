# -*- coding: utf-8 -*-
# @File  : ComprehensionDemo.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/9
# @Desc  : 列表生成式
# (ele for ele in 列表生成器 [if ele..])
import os

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
        print('type(rangeDemo2):', type(rangeDemo2))
        print(len(rangeDemo2))
        print(rangeDemo2)

    # 使用列表生成式罗列出某个目录下所有的文件注意需要导入os模块
    print('list_all_dir...........................................')
    def list_all_dir(self):
        allDir = list(d for d in os.listdir('.'))

        print(allDir)

    # 使用dict实现列表生成器
    def compreDict(self):
        dictVal = {'name':'suzhuo', 'age':24, 'city':'China'}
        # dictVal.items()解析：
        #   1.dictVal.items()返回一个数组类型的元组list中每个元素是一个元组每个元组包含key和value两个元素值
        listDictParse = list(k +'='+ v for k, v in list([('name', 'suzhuo'), ('age', '24'), ('city', 'China')]))
        print(listDictParse)
        listDict = list(k+'='+str(v) for k, v in dictVal.items())
        print(listDict)

if __name__ == '__main__':
    comDemo = ComprehensionDemo()

    comDemo.list_compre()
    comDemo.list_all_dir()
    comDemo.compreDict()