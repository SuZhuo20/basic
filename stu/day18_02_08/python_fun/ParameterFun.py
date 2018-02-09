# -*- coding: utf-8 -*-
# @File  : ParameterFun.py
# @Author: Zhuozhuo.Geng
# @Date  : 18/2/9 00:25
# @Desc  : 函数参数:
#               注意：
#                   0.prama='defvalue'：定义默认参数
#                   1.*args：定义可变参数，在函数内部会转换成tuple
#                   2.**kw: 定义关键字参数，在函数内部会转换成dict
#                   3.*, param,...：定义命名参数
#                   4.使用组合参数时参数的定义顺序：
#                       必选参数、默认参数、可变参数、命名关键字、关键字参数
class ParameterFun(object):
    # 位置参数
    def parameter_position(self, num, n):
        mul = 1

        while n > 0:
            mul *= num
            n -= 1

        return mul

    # 默认参数函数
    # 设置默认参数时注意事项：
    #   1.必选参数在前，默认参数在后
    #   2.如何设置默认参数：当函数有多个参数时，把变化大的放到前面，变化小的设置成默认参数放到后面
    #   3.定义默认参数时，默认参数一定要指向不变对象
    def def_parameter(self, num, n=3):
        mul = 1

        while n > 0:
            mul *= num
            n -= 1

        return mul
    # 在定义默认参数时要注意默认参数指向不变对象
    def def_parameter_list(self, L=[]):
        L.append('END')

        return L
    def def_parameter_list2(self, L=None):
        if L is None:
            L = []
        L.append('END')

        return L

    # 可变参数,可一次传入0个或多个参数：
    # 特点：
    #   1.可变参数允许传递0或多个参数，在函数内部会将这些参数重新组成一个tuple
    def mul_param(self, *nums):
        print('type(*nums):', type(nums))
        sum = 0
        for num in nums:
            print('num=', num)
            print('type(num)=', type(num))
            sum += num
        return sum

    # 关键字参数
    # 特点：
    #   1.关键字参数允许传递0个或多个含参数名的参数，这些参数在函数内部会被封装成一个dict
    # 适用场景：
    #   1.当一个对象传递必选参数外还需要传递其他多个扩展参数
    def key_param(self, **kw):
        return kw

    # 命名关键字参数
    # 由来：
    #   1.关键字参数允许传入多个不受限制的关键字参数，我们也不知道哪些key被传入了进来
    #   2.在关键字参数的基础限制可传入参数的key
    def limit_key_param(self, **kw):
        # 判断可变参数中是否包含city和age
        if 'city' in kw:
            print('city:', kw.get('city'))
        if 'age' in kw:
            print('age:', kw.get('age'))
    # 使用命名函数限定传入进来的key
    # 注意：
    #   1.添加 * 号，* 号后面的参数为命名参数
    #   2.当调用名称参数如果命名参数没有被赋值则会报错
    def limit_key_param2(self, *, city, age):
        print(city)
        print(age)
    # 命名参数
    # 注意：
    #   1.如果名称参数前是可变参数则不需要写 * 号
    def limit_key_param3(self, *args, city, age):
        print('agrs:', args)
        print('city:', city)
        print('age:', age)
    # 命名参数和默认参数组合
    def limit_key_param4(self, *args, city='city', age):
        print('agrs:', args)
        print('city:', city)
        print('age:', age)

if __name__ == '__main__':
    paramFun = ParameterFun()

    print(paramFun.parameter_position(2, 3))

    print(paramFun.def_parameter(3))
    print(paramFun.def_parameter(3, 2))
    print(paramFun.def_parameter(n=4, num=2))
    # 调用默认参数
    print(paramFun.def_parameter_list())
    print(paramFun.def_parameter_list())
    print(paramFun.def_parameter_list())
    # 改进def_parameter_list
    print(paramFun.def_parameter_list2())
    print(paramFun.def_parameter_list2())
    print(paramFun.def_parameter_list2())

    # 可变参数
    print(paramFun.mul_param(1, 2, 3, 4))
    # 将已有的list或tuple传入到可变参数中
    listNum = [1, 2, 3, 4]
    print(paramFun.mul_param(*listNum))
    print('tupleNum...................')
    tupleNum = (1, 2, 3, 4)
    print(paramFun.mul_param(*tupleNum))

    print('key_param..................')
    # 关键字参数
    extra = {'name':'suzhuo', 'age':23, 'city':'DaLian'}
    print(paramFun.key_param(name=extra.get('name', -1), age=extra.get('age', -1)))
    # 注意：
    #   1.**extra将dict中的key-value取出来用关键字参数传递给key_param
    #   2.kw获得的dict是extra的一份拷贝，对kw的改动不会影响extra中的数据
    print(paramFun.key_param(**extra))

    print('limit_key_param............')
    # 命名参数
    paramFun.limit_key_param2(city='china', age=24)
    paramFun.limit_key_param3(city='china', age=24)
    # 命名参数和默认参数组合
    paramFun.limit_key_param4(age=24)