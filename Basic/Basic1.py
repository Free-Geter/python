# 标识用于唯一标识对象，通常对应于对象在计算机内存中的地址。
# 使用内置函数id(obj)可返回对象 obj 的标识。
x = 10
print(id(x))

# 类型用于表示对象存储的“数据”的类型。类型可以限制对象的取值范围以及可执行的操作。
# 可以使用 type(obj)获得对象的所属类型。
print(type(x))

# Python 提供了三元运算符，三元运算符是条件语句中比较简练的一种赋值方式，用来在某些简单双分支赋值情况。
num = int(input('请输入一个整数:'))
print(num if num < 10 else '整数过大')

# 分支语句：
score = int(input("请输入分数"))
grade = ''
if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
elif score <= 100:
    grade = "优秀"
else:
    grade = "作弊"

print("分数是{0},等级是{1}".format(score, grade))

# while循环语句
# Python 可以遍历的对象有序列(字符串、列表、元组)、字典、迭代器对象(iterator)、生成器函数文件对象。
num = 0
while num <= 10:
    print(num)
    num += 1

# for循环语句
for i in range(5):
    for j in range(5):
        print(i, end='\t')
    print()  # 使用此语句换行，不需要print('\n')

# 切片操作
a = [10, 20, 30, 40, 50, 60, 70]
print(a[:])  # 默认从列表的开始到列表结束 ，步长为 1
print(a[1:])  # 从列表的索引 1 开始到结束，步长为 1
print(a[:2])  # 从开始到索引 1，步长为 1
print(a[1:3])  # 从列表索引 1 开始到索引 2，步长为 1
print(a[1:6:2])  # 从列表索引 1 开始到索引 5，步长为 2
# 切片的实用操作
a = [10, 20, 30, 40, 50, 60, 70]
print(a[-3:])  # 从列表的倒数第 3 个开始到列表结束
print(a[-5:-3])  # 从倒数第 5 个开始到倒数第 4 个
print(a[::-1])  # 从右到左反向提取


# 类型转换

# 转换为 int
print('int()默认情况下为：', int())
print('str 字符型转换为 int：', int('010'))
print('float 浮点型转换为 int：', int(234.63))     # 强制类型转换，直接去尾
# 十进制数 10，对应的 2 进制，8 进制，10 进制，16 进制分别是：1010,12,10,0xa
print('int(\'0xa\', 16) = ', int('0xa', 16))
print('int(\'10\', 10) = ', int('10', 10))
print('int(\'12\', 8) = ', int('12', 8))
print('int(\'1010\', 2) = ', int('1010', 2))

# 转换为 float
print('float()默认情况下为：', float())
print('str 字符型转换为 float：', float('123.01'))
print('int 浮点型转换为 float：', float(32))

# 转换为 complex
print('创建一个复数(实部+虚部)：', complex(12, 43))
print('创建一个复数(实部+虚部)：', complex(12))

# 转换为 str 字符串
print('str()默认情况下为：', str())
print('float 字符型转换为 str：', str(232.33))
print('int 浮点型转换为 str：', str(32))
lists = ['a', 'b', 'e', 'c', 'd', 'a']
print('列表 list 转换为 str:', ''.join(lists))       # 这里如果直接使用str(list)，结果为‘['a', 'b', 'e', 'c', 'd', 'a']’
Tuple = ('a', 'b', 'e', 'c', 'd', 'a')
print('列表 list 转换为 str:', ''.join(lists))       # 这里如果直接使用str(Tuple)，结果为‘('a', 'b', 'e', 'c', 'd', 'a')’

# 转换为 list
strs = 'hongten'
print('序列 strs 转换为 list:', list(strs))

# 转换为 tuple
print('列表 list 转换为 tuple:', tuple(lists))

# 字符和整数之间的转换
print('整数转换为字符 chr:', chr(67))
print('字符 chr 转换为整数:', ord('C'))

print('整数转 16 进制数:', hex(12))
print('整数转 8 进制数:', oct(12))
