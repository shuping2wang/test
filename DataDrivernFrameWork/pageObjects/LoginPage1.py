# encoding = utf -8
from DataDrivernFrameWork.util.ObjectMap import *
from DataDrivernFrameWork.util.ParseConfigurationFile import ParseConfigFile

class LoginPage1(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions =self.parseCF.getItemsSection("163main_login")
        print(self.loginOptions)

    def swichToFrame(self):
        try:
            # 从定位表达式配置文件中读取frame的定位表达式
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(locatorExpression)
        except :
            print("读取frame 异常了")

    def swichToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except:
            print("默认的frame异常了")

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取userName的定位表达式
            locateType, locatorExpression = self.loginOptions["loginPage.userName".lower()].split(">")
            # 获取登陆页面的用户名输入框页面对象，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except :
            print("读取userName 异常了")

    def passwordObj(self):
        try:
            # 从定位表达式配置文件中读取passwordObj的定位表达式
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            # 获取登陆页面的用户名输入框页面对象，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("读取passwordObj 异常了")

    def loginButton(self):
        try:
            # 从定位表达式配置文件中读取登陆按钮的定位表达式
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            # 获取登陆页面的用户名输入框页面对象，并返回调用者
            elementObj = getElment(self.driver, locateType, locatorExpression)
            return elementObj
        except:
            print("读取登陆按钮 异常了")
if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")
    driver.get("https://mail.163.com/")
    import time

    time.sleep(3)
    login =LoginPage1(driver)
    login.swichToFrame()
    login.userNameObj().send_keys("Erin_spwang@163.com")
    login.passwordObj().send_keys("abc18730633065")
    login.loginButton().click()
    login.swichToDefaultFrame()