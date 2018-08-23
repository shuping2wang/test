from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")

driver.get("http://www.51zxw.net/")
driver.maximize_window()
sleep(2)

driver.get("http://www.51zxw.net/list.aspx?cid=615")
driver.set_window_size(200, 400)
driver.refresh()
sleep(2)

driver.back()
sleep(2)

driver.forward()

sleep(2)
driver.quit()