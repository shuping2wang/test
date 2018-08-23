# encoding = utf-8
from DataDrivernFrameWork.pageObjects.HomePage import HomePage
from DataDrivernFrameWork.pageObjects.AddressBookPage import AddressBookPage
import traceback
import time

class AddContactPerson(object):
    """
    添加通讯录
    """

    def __init__(self):
        print("add  contact person")

    def add(self, driver, contactName, contactEmail, isStar, contactPhone, contactComment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            # 单击通讯录链接
            hp.addressLink().click()
            time.sleep(1)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                # 非必填项
                apb.contactPersonName().send_keys(contactName)
                # 非必填项
                apb.contactPersonEmail().send_keys(contactEmail)
                if isStar == u"是":
                    # 非必填项
                    apb.starContacts().click()
                if contactPhone:
                    # 非必填项
                    apb.contactPersonMobile().send_keys(contactPhone)
                if contactComment:
                    apb.contactPersonComment().send_keys(contactComment)
                apb.saveontactPerson().click()
        except :
            print(traceback.print_exc())
            raise Exception

if __name__ == "__main__":
    from DataDrivernFrameWork.appModules.LoginAction import LoginAction
    from selenium import webdriver
    import time

    # 启动火狐浏览器
    driver = webdriver.Firefox(executable_path="C:\\devTools\\test\\geckodriver-v0.21.0-win64\\geckodriver")

    # 打开浏览器首页
    driver.get("https://mail.163.com/")
    # 因为休眠时间太长，所以报错[WinError 10053] 你的主机中的软件中止了一个已建立的连接。
    loginAction = LoginAction(driver)
    loginAction.login(userName="erin_spwang@163.com", passWorld="abc18730633065")
    addContactPerson = AddContactPerson()
    addContactPerson.add(driver, "张三", "123@qq.com", "是", "", "")
    assert "张三" in driver.page_source
    driver.quit()