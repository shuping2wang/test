# encoding = utf-8
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_choice(self):
        #从序列中随机选取一个元素
        element = random.choice(self.seq)
        #验证随机元素确实在列表中
        self.assertTrue(element in self.seq)

    def test_sample(self):
        #验证执行的语句是否抛出了异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in  random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def tearDown(self):
        pass

    def test_shuffle(self):
        #随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle,(1, 2, 3))

if __name__ == '__main__':
    #根据给定的测似类，获取其中以test开头的测试方法，并返回一个测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    #将多个类加载到测试套件中
    suite = unittest.TestSuite([testCase1, testCase2])
    #设置verbosity=2打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)
#testLoader类。测试用例加载器。返回一个测试用例集合
#loadTestFormTestCase类。根据定义的测试类。获取其中的所有以test开头的测试方法，返回一个测试集合
#testsuite类 组装测试用例的实例，支持添加和删除用例，最后将传递给testrunner 进行测试执行
#TextTestRunner 类，测试用例执行类，其中以Text表示文本形式输出测试结果