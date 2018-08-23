# encoding utf-8
from DataDrivernFrameWork.pageObjects.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self, driver):
        self.driver = driver
        print("login")

    def login(self, userName, passWorld):
        try:
            loginPageObj = LoginPage(self.driver)
            loginPageObj.switchToFrame()
            loginPageObj.userNameObj().send_keys(userName)
            loginPageObj.passwordObj().send_keys(passWorld)
            loginPageObj.loginButton().click()
            loginPageObj.switchToDefaultFrame()
        except Exception as eee:
            print("登录出异常啦！！！")
            print(eee)

if __name__ == "__main__":
    from selenium import webdriver
    from time import sleep

    # 启动火狐浏览器
    driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")

    # 打开浏览器首页
    driver.get("https://mail.163.com/")
    # 因为休眠时间太长，所以报错[WinError 10053] 你的主机中的软件中止了一个已建立的连接。
    # sleep(5)
    loginAction = LoginAction(driver)
    loginAction.login(userName="erin_spwang@163.com", passWorld="abc18730633065")