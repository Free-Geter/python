# os 模块-调用操作系统命令
# os.system 可以直接调用系统的命令

# os.system 调用 windows 系统的记事本程序
import math
import os

os.system("notepad.exe")

# os.system 调用 windows 系统中 ping 命令

os.system("ping www.baidu.com")

# 文件的读写
# 打开文件
f = open('testFile.txt', 'r')
# 读取文件内容
print(f.read(5))  # 读取到hello
print(f.read(1))  # 读取到空格
print(f.read(6))  # 读取到 python
# 关闭文件
f.close()

# 写文件
f = open('testWrite.txt', 'w')
f.write('hello python')
f.close()

print('#######################################################################################')


# python函数的定义
# def 函数名 ([参数 1,参数 2…]) :
#     代码
#     [return 表达式]
# 定义函数
def printInfo(name, age):
    print('我叫{0},今年{1}岁，是一名大学生'.format(name, age))


# 调用函数
printInfo('李四', 19)


# 通过函数参数传入斐波那切数列长度，使用 return 语句返回计算结果
# 定义函数
def fibs(n):  # n 代码斐波那切数列的长度
    # 定义斐波那切数列的初识列表
    result = [0, 1]
    # 通过循环计算，将结果添加到列表中
    for x in range(n - 2):
        result.append(result[-1] + result[-2])
    # 将计算结果返回
    return result


# 调用函数
re = fibs(10)
print('斐波那切数列:', re)

print('#######################################################################################')
# global 关键字
# 全局变量的作用范围是所有的函数都可用使用此变量，函数内要改变全局变量的值，使用 global 关键字。
a = 100  # 全局变量


def fun1():
    global a  # 如果要在函数内改变全局变量的值，增加 global 关键字声明
    print(a)  # 打印全局变量 a 的值
    a = 300  # 修改全局变量的值


# 调用函数
fun1()
print(a)

print('#######################################################################################')


# 在 Python 中，参数传递不仅仅可以按照声明函数时参数的顺序进行传递，还可以按照形参的名称传递参数，称为“命名参数”，也称“关键字参数”。
# 使用按形参的名称传递参数的方式调用函数时，要在调用函数名后的圆括号里为函数的所有参数赋值，赋值的顺序可以不必按照函数声明时的参数顺序。
def fun1(a, b, c):
    print(a, b, c)


fun1(8, 9, 19)  # 位置参数
fun1(c=10, a=20, b=30)  # 命名参数，参数顺序可以和声明时的顺序不一致


# 可变参数
# 在 Python 中，函数可以具有任意个参数，而不必在声明函数时对所有参数进行定义。
# 声明函数时，如果在参数名前加上一个星号“*”，则表示将多个参数收集到一个“元组”对象中；
# 如果在参数名前加上两个星“**”，则表示将多个参数收集到一个“字典”对象中。
def fun1(a, b, *c):  # 函数参数前添加一个"*",可变参数以元组形式体现
    print(a, b, c)


fun1(8, 9, 19, 20)


def fun2(a, b, **c):  # 函数参数前添加两个"**",可变参数以字典形式体现
    print(a, b, c)


fun2(8, 9, name='gaoqi', age=18)


def fun3(a, b, *c, **d):
    print(a, b, c, d)


fun3(8, 9, 20, 30, name='gaoqi', age=18)

print('#######################################################################################')


# 高阶函数：所谓高阶函数，就是不光可以传递变量，还可以传递函数
# 面向函数编程，说白了就是把函数传来传去，函数是第一要素
# 面向对象编程，说白了就是把对象传来传去，对象是第一要素

# 1.map函数
# map()函数接收两个参数，一个是函数，一个是序列，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 list 返回。
def f(x):
    return x * x


L = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(L))  # 返回值为map类型，需要转换为list类型进行print输出

# 2.reduce
# reduce 把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算，
from functools import reduce


def add(x, y):
    return x + y


sum = reduce(add, [1, 3, 5, 7, 9])
print(sum)


# 3.filter
# Python 内建的 filter()函数用于过滤序列。和 map()类似，filter()也接收一个函数和一个序列。
# 和 map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。
# 在一个 list 中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


L = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(list(L))

# 4.sorted
sorter1 = sorted([1, 3, 6, -20, 34])
print("升序排列:", sorter1)

# 4.1 sorted()函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序
sorter2 = sorted([1, 3, 6, -20, -70], key=abs)
print("自定义排序:", sorter2)
sorter2 = sorted([1, 3, 6, -20, -70], key=abs, reverse=True)
print("自定义反向排序:", sorter2)

# 4.2 字符串排序依照 ASCII
sorter3 = sorted(["ABC", "abc", "D", "d"])
print("字符串排序:", sorter3)

# 4.3 忽略大小写排序
sorter4 = sorted(["ABC", "abc", "D", "d"], key=str.lower)
print("忽略字符串大小写排序:", sorter4)

# 4.4 要进行反向排序，不必改动 key 函数，可以传入第三个参数 reverse=True：
sorter5 = sorted(["ABC", "abc", "D", "d"], key=str.lower, reverse=True)
print("忽略字符串大小写反向排序:", sorter5)


# 5.匿名函数
# lambda 表达式就是一个简单的函数。使用 lambda 声明的函数可以返回一个值，在调用函数时，直接使用 lambda 表达式的返回值。使用 lambda 声明函数的语法格式如下:
# lambda arg1,arg2,arg3... : <表达式>
class Student:
    def __init__(self, age, name):
        self.name = name
        self.age = age


stu1 = Student(11, 'aaa')
stu2 = Student(21, 'ccc')
stu3 = Student(31, 'bbb')
student_list = sorted([stu1, stu2, stu3], key=lambda x: x.age)
# student_list=sorted([stu1,stu2,stu3],key=lambda x:x.name)
for stu in student_list:
    print('name:', stu.name, 'age:', stu.age)


# 6.闭包
# 使用闭包求两点之间的距离
def getDisOut(x1, y1):
    def getDisIn(x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return getDisIn


# 求点(1,1)距离原点(0,0)的距离 #调用外部函数
getDisIn = getDisOut(0, 0)
result = getDisIn(1, 1)
print('点(1,1)距离原点(0,0)的距离', result)
# 求点(2,2)距离原点(0,0)的距离 r
esult = getDisIn(2, 2)
print('点(2,2)距离原点(0,0)的距离', result)
