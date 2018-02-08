# -*- coding: utf-8 -*-
# @File  : DataType.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/8
# @Desc  : python基本数据类型
class DataType(object):

    # 整数
    def intDemo(self):
        print('intDemo............')

        #str转换成int
        intVal = int('23')

        print(intVal)
    # 浮点数
    def floatDemo(self):
        print('floatDemo............')

        floatVal = float(23)

        print(floatVal)

    # 字符串
    def strDemo(self):
        print('strDemo............')

        strVal = str(23)

        print(strVal)
        print(type(strVal))
        print('isinstance(strVal, str)：',isinstance(strVal, str))

        # r标示''中的转义字符不转义
        print('\\\t\t')
        print(r'\\\t\t')

        # '''content'''代替\n进行文本内容换行
        print('''
                line1
                line2 
                line3
            ''')

        # 将ascii转换成对应的int
        print('ord(\'A\'):', ord('A'))
        # 将int值转换成对应的char
        print('chr(65)：', chr(65))

        # 将str转换成byte类型，中文可以通过utf-8编码转换成byte，str可通过b'ABC'转换成byte
        enVal = '中文'.encode('utf-8')
        print('\'中文\'.encode(\'utf-8\'):', enVal)
        # 使用指定编码类型进行解码
        enValDecode = enVal.decode('utf-8')
        print('enVal.decode(\'utf-8\'):', enValDecode)

        # len计算str中字符个数
        print('len(\'ABC\'):', len('ABC'))


    # True   False
    # and or not
    def booleanDemo(self):
        print('booleanDemo............')

        # 与运算 代替java中的 &&
        print("True and True：",True and True)

        # 或运算代替java中的 ||
        print("True or False：",True or False)

        # 非运算代替java中的 !
        print('not True：', not True)

    # None -- 空值
    def noneDemo(self):
        pass


if __name__ == '__main__':
    dataType = DataType()
    dataType.intDemo()
    dataType.floatDemo()
    dataType.strDemo()
    dataType.booleanDemo()


    print(dir(dataType))