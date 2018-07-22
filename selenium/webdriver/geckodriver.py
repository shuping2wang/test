# encoding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").clear()

driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")

driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
