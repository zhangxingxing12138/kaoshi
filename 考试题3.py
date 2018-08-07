class Person(object):
    def __init__(self,age):
        self.__age = age
        print('我的年龄是%d'%self.__age)
    def change_age(self):
        if self.__age>=18 and self.__age<=60:
            print('可以修改年龄')
            a = int(input('请输入修改后的年龄：'))
            if a != self.__age:
                self.__age=a
                print('修改后的年龄为:%d'%a)
        else:
            print('不可修改')
        return self.__age
xiaohong = Person(17)#可以修改年龄大于18
print(xiaohong.change_age())
        
