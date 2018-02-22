## 迭代对象和迭代器：
### 1.迭代对象：
        1.集合数据类型，list、tuple、dict、set、str
        2.生成器和带yield的generator function
        3.这些可直接作用于for循环的对象统称为可迭代对象：Iterable
        4.可使用isinstance判读一个对象是否是迭代对象：isinstance([],Iterable)
### 2.迭代器：
        1.生成器对象(Iterator)不但可以通过for遍历，而且还能通过next(generatorObj)不断调用并返回
            下一个值，知道抛出异常－－StopIteration
        2.在1中可以被next函数调用并不断返回下一个值的对象称为迭代器：Iterator
        3.可以使用isinstance判断一个对象是否是一个Iterator：isinstance(obj, Iterator)
        4.生成器都是Iterator对象，但是list、tuple、dict、set、str是Iterable但是它们都
            不是Iterator
        5.可以通过iter()函数将list、tuple、dict、set、str变成Iterator：iter([])
        6.迭代器说明：
            为什么list、dict、str等数据类型不是Iterator？
                这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()
                函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这
                个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()
                函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数
                据时它才会计算。
                Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能
                存储全体自然数的   －－引用廖雪峰python3教程
### 3.总结：
        1.凡是可以作用于for循环的对象都是Iterable类型；
        2.凡是可作用于next()函数的对象都是Iterator对象，它们表示一个惰性计算的序列；
        3.集合数据类型如list、tuple、dict、set、str是Iterable类型，但它们不是Iterator类型，
            不过可以通过iter()函数获得一个Iterator对象；

