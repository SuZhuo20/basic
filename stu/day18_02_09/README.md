## 迭代对象和迭代器：
### 1.迭代对象：
        1.集合数据类型，list、tuple、dict、set、str
        2.生成器和带yield的generator function
        3.这些可直接作用于for循环的对象统称为可迭代对象：Iterable
        4.可使用isinstance判读一个对象是否是迭代对象：isinstance([],Iterable)
### 2.迭代器：
        1.生成器对象不但可以通过for遍历，而且还能通过next(generatorObj)不断调用并返回
            下一个值，知道抛出异常－－StopIteration
        2.象1中可以被next函数调用并不断返回下一个值的对象称为迭代器：Iterator
        3.可以使用isinstance判断一个对象是否是一个Iterator：isinstance(obj, Iterator)
        4.生成器都是Iterator对象，但是list、tuple、dict、set、str是Iterable但是它们都
            不是Iterator
        5.可以通过iter()函数将list、tuple、dict、set、str变成Iterator：iter([])