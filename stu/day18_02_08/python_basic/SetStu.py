# -*- coding: utf-8 -*-
# @File  : SetStu.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/8
# @Desc  : python中常用集合：list、tuple、dict、set
# 可变对象和不可变对象区别：
#   对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
class SetStu(object):

    # list集合 []:
    # 特点：
    #   1.可变的有序列表
    # 优点：
    #   1.
    # 缺点：
    #   1.查找速度慢
    # 适用场景:
    #   1.
    def listDemo(self):
        print('list 下表从0开始....................................................................................')
        listDemo = [1, 'A', True, [1, 'B'], 12.3]

        # len(list) 计算list集合的元素个数
        print('len(list)：', len(listDemo))

        # 获取指定下标的元素
        print('listDemo[1]:', listDemo[1])
        print('listDemo[-1]:', listDemo[-1])

        # 在list末尾追加元素
        print('list.append()：')
        listDemo.append('appendEle')

        # 将元素插入到指定位置
        print('list.insert(index, value)：')
        listDemo.insert(2, 'new2')
        print(listDemo)

        # 删除list中元素，不加参数时删除末尾元素
        print('list.pop([index])：')
        listDemo.pop()
        listDemo.pop(3)

        # list.sort()对list中的元素进行排序
        # print(listDemo.sort())

    # tuple元组 ()
    # 特点：
    #   1.不可变的有序列表，tuple中的元素不可变（当定义一个tuple时tuple中的元素就不可变)
    # 优点：
    #   1.
    # 缺点：
    #   1.
    # 适用场景:
    #   1.
    # 和list的区别：
    #   1.tuple在定义时需要确定tuple中的元素，元素一旦确定则不可修改，tuple没有list中的append、insert方法
    def tupleDemo(self):
        print('tuple demo....................................................................................')

        classmates = ('zhangsan', 'lisi', 'wangwu')
        print('classmates[0]:', classmates[0])

        classList = ('zhqng', ['wangwu', 'lisi'])
        classList[1].append(True)
        print(classList)

    # dict字典 {}
    # 特点：
    #   0.无序
    #   1.key:value对相当于java中的Map，这种以key-value方式存储，在放入时需要根据key计算出存储的位置(使用哈希算法计算)，所以在dict中作为key的对象值不能改变(比如：str、int)
    #   2.每个key只能对应一个value，同一个key放入多个value只会记录最后一个value
    # 优点：
    #   1.有极快的查找速度
    # 缺点：
    #   1.耗费内存
    # 适用场景:
    #   1.
    # 和list比较：
    #   1.dict查找和插入速度极快，不会随着key的增加而变慢
    #   2.dict需要占用大量的内存，内存浪费多
    #   1.list查找和插入速度会随着元素的增加而变慢
    #   2.占用空间少，内存浪费少
    def dictDemo(self):
        print('dict demo....................................................................................')

        dictDemo = {'name':'suzhuo', 'age':24}

        print(dictDemo)
        # 根据key取值
        print('dictDemo[\'name\']:', dictDemo['name'])
        # 根据key取值如果此key不存在则返回defValue（默认值）
        print('dictDemo.get(\'key\', [defValue]):', dictDemo.get('age', -1))

        # 判断某个key是否存在dict中
        print('\'name\' in dictDemo:', 'name' in dictDemo)

        # 删除dict中的某个key时对应的value也会被删除 pop('key')->返回被删除key对应的value
        print('dictDemo.pop(\'name\'):', dictDemo.pop('name'))

        # 判断某个变量是否是dict类型
        print('isinstance(dictDemo, dict):', isinstance(dictDemo, dict))

    # set集合 ([])
    # 特点：
    #   0.无序
    #   1.和dict类似，但是set中只存储key
    #   2.set中的key也是不能重复，set中使用hash算法计算key是否重复，因此key中的值也是不可变对象
    # 优点：
    #   1.
    # 缺点：
    #   1.
    # 适用场景:
    #   1.相当于数学中无序、无重复元素的集合
    def setDemo(self):
        print('set demo....................................................................................')
        # set集合在定义的时候需要使用list初始set集合中的元素
        setDemo = set([1, 'A'])
        setDemo1 = set([2, 'b'])

        # 使用set.add(ele)方法向set中添加元素
        print('setDemo.add(\'b\'):', setDemo.add('b'))

        # 使用set.remove(key)删除元素
        print('setDemo.remove(key)：', setDemo.remove(1))
        # 取setDemo 和 setDemo1公共元素
        print('setDemo & setDemo1：', (setDemo & setDemo1))

        # 取setDemo 和 setDemo1 所有不重复元素
        print('setDemo | setDemo1：', (setDemo | setDemo1))
        print(setDemo)

if __name__ == '__main__':
    setStu = SetStu()

    setStu.listDemo()
    setStu.tupleDemo()
    setStu.dictDemo()
    setStu.setDemo()