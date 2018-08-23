from selenium import webdriver
from time import sleep
#打开火狐浏览器的驱动
driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")
#打开保利首页
#driver.get("https://blpw.polyt.cn/")
#点击登录
#driver.find_element_by_link_text("登录").click()
#sleep(2)

#点击全部演出https://blpw.polyt.cn/toSearchView
#sleep(5)
driver.get("https://blpw.polyt.cn/toSearchView")
# driver.find_element_by_id("searchNoClass").click()
# driver.find_element_by_partial_link_text("保利亲子艺术节原创剧目").click()
sleep(5)
driver.get("https://blpw.polyt.cn/show/19030000000001700")
driver.find_element_by_id("chooseSeat").click()
# 输入账号和密码
driver.find_element_by_name("username").send_keys(("13651357608"))
driver.find_element_by_name("password").send_keys(("123456"))
# 点击登录按钮即用户就登录成功了
driver.find_element_by_class_name("login-submit").click()
sleep(3)
driver.find_element_by_id("15_27").click()
driver.find_element_by_id("commitSeat").click()
driver.find_element_by_id("submit").click()