# encoding utf-8
from DataDrivernFrameWork.util.ObjectMap import *

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def switchToFrame(self):
        self.driver.switch_to.frame("x-URS-iframe")

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def userNameObj(self):
        try:
            # 获取登陆页面的用户名输入框页面对象，并返回调用者
            elementObj = getElment(self.driver, "xpath", '//input[@name = "email"]')
            return elementObj
        except:
           print("获取登陆页面的用户名输入框页面对象时异常了")
    def passwordObj(self):
        try:
            # 获取登陆页面的密码输入框页面对象，并返回调用者
            elementObj = getElment(self.driver, "xpath", '//input[@name = "password"]')
            return elementObj
        except :
            print("获取登陆页面的密码输入框页面对象时异常了")
    def loginButton(self):
        try:
            # 获取登陆页面的登陆按钮页面对象，并返回调用者
            elementObj = getElment(self.driver, "id", "dologin")
            return elementObj
        except :
            print("获取登陆页面的登陆按钮页面对象时异常了")

if __name__ == '__main__':
    # 测试代码
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")
    driver.get("https://mail.163.com/")
    import time
    time.sleep(3)
    login = LoginPage(driver)
    login.switchToFrame()
    # 或者：LoginPage.switchToFrame(login)
    # 输入登陆名
    login.userNameObj().send_keys("erin_spwang@163.com")
    # 输入密码
    login.passwordObj().send_keys("abc18730633065")
    login.loginButton().click()
    login.switchToDefaultFrame()
   # driver.quit()