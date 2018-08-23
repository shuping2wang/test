# encoding = utf-8
import os

# 获取当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocationPath = parentDirPath + u"\\config\\pageElementLocator.ini"
