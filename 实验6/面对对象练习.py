class student(object):
    def __int__(self,name,age,no):
        # 私有属性
        self.name=name
        self.age=age
        self.no = no
    def eat(self):
        pass
    def sleep(self):
        pass
    def __study(self):
        pass

class groupleader(student):
    def __init__(self,name,age,no,zhiwu):
        student.__int__(self,name,age,no)
        self.zhiwu =zhiwu

    def __study(self):
        pass
    def guanli(self):
        pass

class Teacher(groupleader):
    def __init__(self,name,age,zhiwu):
        groupleader.__int__(self,name,age,zhiwu)
    def teach(self):
        pass

one = Teacher()

x = {1,2}
print(x*2)