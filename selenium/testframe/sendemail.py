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

#driver.switch_to.frame("x - URS - iframe")

#获取用户名的输入框

#userName=driver.find_element_by_xpath('//input[@name = "email"]')
driver.find_element_by_name("email").send_keys("erin_spwang")

#输入用户名
#userName.send_keys("erin_spwang")

pwd = driver.find_element_by_xpath('//input[@name = "password"]')
#输入密码
pwd.send_keys("abc18730633065")

#发送一个回车键
pwd.send_keys(Keys.ENTER)

#等待5s
sleep(5)

#点击通讯录
driver.find_element_by_xpath("//div[text() = '通讯录']").click()
#等待2s
sleep(2)
#单机创建联系人按钮
driver.find_element_by_xpath("//span[text() = '新建联系人']").click()

#暂停2s
sleep(2)

#输入联系人姓名

driver.find_element_by_xpath("//a[@title = '编辑详细姓名']/preceding - sibling::div/input").send_keys("何世元")

#输入邮箱

driver.find_element_by_xpath("//*[@id = '_mail_link_35_352']//input").send_keys("1334849803@qq.com")
#设为星标联系人
driver.find_element_by_xpath("//span[text() = '设为星标联系人']/preceding - sibling::span/b").click()

sleep(2)
#输入手机号
driver.find_element_by_xpath("//*[@id = '_mail_link_35_352']//dd//input").send_keys("13651345454")

sleep(2)

#输入备注信息
driver.find_element_by_xpath("//texterea").send_keys("朋友")

sleep(2)
#单击确认按钮

driver.find_element_by_xpath("//span[text() = '确定']").click()

sleep(5)

driver.quit()
