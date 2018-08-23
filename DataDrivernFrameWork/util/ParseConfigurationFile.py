# encoding = utf-8
from configparser import ConfigParser
from DataDrivernFrameWork.config.VarConfig import pageElementLocationPath

class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocationPath)

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section 下的所有option键值对
        # 并以字典类型返回调用者
        """注意：
        使用self.cf.items(selection) 此种方法获取到配置文件中的options 内容均被转换成小写，
        比如,loginPage.frame被转化成了loginpage.frame
        """
        optionDict = dict(self.cf.items(sectionName))
        return optionDict

    def getOptionValue(self, selectionName ,optionName):
        # 获取指定section下的指定option的值
        value = self.cf.get(selectionName, optionName)
        return value

if __name__ == "__main__":
    pc = ParseConfigFile()
    print(pc.getItemsSection("163main_login"))
    print(pc.getOptionValue("163main_login", "loginPage.frame"))