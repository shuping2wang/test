# encoding = utf-8
from DataDrivernFrameWork.util.ObjectMap import *
from DataDrivernFrameWork.util.ParseConfigurationFile import ParseConfigFile
import traceback

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()

    def addressLink(self):
        try:
            # 从定位表达式配置文件中读取定位通讯录按钮的定位方式和表达式
            locateType, locatorExpression =self.parseCF.getOptionValue("163mail_homePage", "homePage.addressbook").split(">")
            # 获取登陆成功页面的通讯录页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return  elementObj
        except:
            print(traceback.print_exc())
            print("添加地址异常了")