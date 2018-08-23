
class BasePage(object):
    print("描述类")

    # webdriver实例
    def __init__(self, driver):
        self.driver = driver