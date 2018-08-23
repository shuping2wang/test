# encoding = utf-8
from DataDrivernFrameWork.util.ObjectMap import *
from DataDrivernFrameWork.util.ParseConfigurationFile import ParseConfigFile

class AddressBookPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.addContactsOptions = self.parseCF.getItemsSection("163mail_addContactPage")
        print(self.addContactsOptions)

    def createContactPersonButton(self):
        # 获取联系人按钮
        try:
            # 从定位表达式配置文件中读取定位新建联系人按钮得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.createContactsBtn".lower()].split(">")
            # 获取新建联系人按钮页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取联系人按钮抛异常了")

    def contactPersonName(self):
        # 获取联系人名字输入框
        try:
            # 从定位表达式配置文件中读取定位新建联系人得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonName ".lower()].split(">")
            # 获取新建联系人姓名页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取联系人姓名抛异常了")

    def contactPersonEmail(self):
        # 获取联系人电子邮件输入框
        try:
            # 从定位表达式配置文件中读取定位新建电子邮件得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonEmail".lower()].split(">")
            # 获取新建联系人电子邮件页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取联系人电子邮件抛异常了")

    def starContacts(self):
        # 获取联系人界面中的星标联系人选择框
        try:
            # 从定位表达式配置文件中读取定位星标联系人选择框得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.starContacts".lower()].split(">")
            # 获取星标联系人选择框页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取星标联系人选择框抛异常了")

    def contactPersonMobile(self):
        # 获取联系人界面中的联系人手机号输入框
        try:
            # 从定位表达式配置文件中读取联系人手机号输入框得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonMobile".lower()].split(">")
            # 获取星标联系人手机号输入框页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取星标联系人输入框抛异常了")

    def contactPersonComment(self):
        # 获取联系人界面中的联系人备注信息输入框
        try:
            # 从定位表达式配置文件中读取联系人备注信息输入框得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.createPersonComment".lower()].split(
                ">")
            # 获取星标联系人备注信息输入框页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取星标联系人备注信息抛异常了")

    def saveontactPerson(self):
        # 获取联系人界面中的保存联系人按钮
        try:
            # 从定位表达式配置文件中读取联系人保存按钮得定位方式和表达式
            locateType, locatorExpression = self.addContactsOptions["addContactPage.saveContactPerson".lower()].split(
                ">")
            # 获取星标联系人保存按钮页面元素，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("获取星标联系人保存按钮抛异常了")