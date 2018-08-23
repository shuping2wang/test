# encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElment(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except :
        print("获取单个页面元素对象时抛出了异常")

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except :
       print("获取多个相同页面元素对象时抛出了异常")
if __name__ == '__main__':
    from selenium import webdriver
    #进行单元测试
    driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")
    driver.get("http://www.baidu.com")
    searchBox = getElment(driver, "id", "kw")
    #打印页面对象的标签名
    print(searchBox.tag_name)
    alist = getElements(driver, "tag name", "a")
    print(alist)
    driver.quit()