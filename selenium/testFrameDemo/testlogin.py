from LoginPage import LoginPage
from testcaseinfo import TestCaseInfo
from selenium import webdriver
import unittest
from time import time
from Common import cc
# 博客地址：https://www.cnblogs.com/AlwinXu/p/5836709.html
class Test_TC_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(cc.driverPath())
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1, name="Test case name", owner='xua')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_TC_Login")

    def test_A(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            # Step1: open base site
            LogUtility.Log("Open Base site" + self.base_url)
            self.driver.get(self.base_url)

            # Step2: Open Login page
            login_page = LoginPage(self.driver)

            # Step3: Enter username & password
            LogUtility.Log("Login web using username")
            login_page.set_username("username")
            login_page.set_password("password")

            time.sleep(2)
            # Checkpoint1: Check popup dialog title
            LogUtility.Log("Check whether sign in dialog exists or not")
            self.assertEqual(login_page.get_DiaglogTitle(), "Sign in")

            # time.sleep(3)
            # Step4: Cancel dialog
            login_page.click_cancel()
            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)

    def tearDown(self):
        self.driver.close()
        self.testResult.WriteHTML(self.testCaseInfo)


if __name__ == '__main__':
    unittest.main()