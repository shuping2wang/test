class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s" %(name,city))
    def talk(self):
        print("hello")
stu1 = Student("jack", "北京")
print(stu1)

def Max_num(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

result=Max_num(15,10)
print(result)

sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
