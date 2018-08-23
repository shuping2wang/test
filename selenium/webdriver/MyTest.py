# encoding = utf-8
import unittest
from testCalc import Calc
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(u"单元测试前，创建testCalc类的实例")
        cls.c = Calc()

    # 具体的测试用例，一定要以test开头
    def test_add(self):
        print("run add()")
        self.assertEqual(MyTest.c.add(1, 2, 12), 15, "test add fail")

    def test_sub(self):
        print("run sub()")
        self.assertEqual(MyTest.c.sub(2, 1, 3), -2, "test sub fail")

    def test_mul(self):
        print("run mul()")
        self.assertEqual(Calc.mul(2, 3, 5), 30, "test mul fail")

    def test_div(self):
        print("run div()")
        self.assertEqual(Calc.div(8, 2, 4), 1, "test div fail")

if __name__ == '__main__':
    # unittest.main()
    # 启动单元测试
    # 获取TestSuite的实例对象
    suite = unittest.TestSuite()
    #将测试用例加载到测试容器中
    suite.addTest(MyTest("test_mul"))
    suite.addTest(MyTest("test_add"))
    suite.addTest(MyTest("test_div"))
    suite.addTest(MyTest("test_sub"))

    #创建TextTestRunner类的实例对象
    runner = unittest.TextTestRunner()
    runner.run(suite)

