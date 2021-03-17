# python中的类和对象
# 对于一个类来说，一般有三种常见的成员：属性、方法、构造器。
# 定义 Student 类
class Student:
    def __init__(self, name, score):  # 构造方法第一个参数必须为
        self
        self.name = name  # 实例属性
        self.score = score

    # 方法的定义：
    # def 方法名(self [, 形参列表])：
    #     方法体
    # 方法的调用：
    # 对象.方法名([实参列表])
    def say_score(self):  # 实例方法
        print(self.name, '的分数是：', self.score)


s1 = Student('张三', 80)  # s1 是实例对象，自动调用__init__()方法
s1.say_score()


# 实例的属性、方法的调用
s1 = Student('张三', 80)  # s1 是实例对象，自动调用__init__()方法
s1.say_score()  # 调用实例方法
# 给已有实例属性重新赋值
s1.name = '李四'
s1.score = 98
print(s1.name, '的分数是:', s1.score)

# 类属性的定义和调用
class Student:
    company = "极客营"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):  # 实例方法
        print("我的公司是：", Student.company)
        print(self.name, '的分数是：', self.score)


s1 = Student('武松', 80)  # s1 是实例对象，自动调用__init__()方法
s1.say_score()
print('一共创建{0}个 Student 对象'.format(Student.count))

# 类方法的定义和使用
class Student:
    company = "SXT"  # 类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)


Student.printCompany()
print('#######################################################################################')


