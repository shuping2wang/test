from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

#打开火狐浏览器
driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")
#设置隐式等待时间为10s
driver.implicitly_wait(3)
#窗口最大化
driver.maximize_window()
#访问163邮箱登陆页面
driver.get("https://mail.163.com/")
#暂停3s
sleep(3)
#切换进frame控件
driver.switch_to.frame("x-URS-iframe")
#获取用户名的输入框
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('erin_spwang@163.com')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('abc18730633065')

#发送一个回车键
driver.find_element_by_name('password').send_keys(Keys.ENTER)