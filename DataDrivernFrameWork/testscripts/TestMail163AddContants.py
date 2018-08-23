# encoding utf-8
from selenium import webdriver
from time import sleep
from DataDrivernFrameWork.pageObjects.LoginPage import LoginPage

def TestmailLogin():
    try:
        # 启动火狐浏览器
        driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")

        # 打开浏览器首页
        driver.get("https://mail.163.com/")

        # 等待30秒
        driver.implicitly_wait(30)
        # 窗口最大化
        driver.maximize_window()
        # 实例化登录类
        loginPage = LoginPage(driver)
        # 讲当前的焦点切换到登录模块的iframe中
        loginPage.switchToFrame()
        # 输入用户名
        loginPage.userNameObj().send_keys("erin_spwang@163.com")
        # 输入密码
        loginPage.passwordObj().send_keys("abc18730633065")
        # 点击登录的按钮
        loginPage.loginButton().click()
        #停留2秒
        sleep(2)
        # 切换到默认窗体，以便兼容火狐浏览器
        loginPage.switchToDefaultFrame()
    except :
        print("登录跑出异常了")
    finally:
        driver.quit()
if __name__ == "__main__":
    TestmailLogin()
    print("恭喜你，登录成功了")