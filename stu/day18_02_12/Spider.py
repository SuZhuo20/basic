# -*- coding: utf-8 -*-
# @File  : Spider.py
# @Author: Zhuozhuo.Geng
# @Date  : 2018/2/12
# @Desc  :
from urllib import request
import chardet
import re

if __name__ == '__main__':
    response = request.urlopen('http://fanyi.baidu.com')

    htmlPage = response.read()
    # 获取网页的编码格式
    chardetRes = chardet.detect(htmlPage)
    encodeHtml = chardetRes.get('encoding', -1)

    chardetRes = htmlPage.decode(encodeHtml)

    REGX = r'href="(.*?)"'
    urlSet = re.findall(REGX, chardetRes, re.S)

    # print(chardetRes)
    print(urlSet)
