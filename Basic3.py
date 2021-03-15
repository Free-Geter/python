# 元组和列表一样，也是一种序列。不同的是元组不能修改，
# 也就是说，元组是只读的不能对元组进行增加、删除、修改。定义元组非常简单，只需要用逗号(，)分隔值即可。


print('#######################################################################################')
# enumerate() 函数: enumerate(sequence, [start=0])
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标,组织成一个元组。一般用在 for 循环当中
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

print('#######################################################################################')
# 序列解包
# 序列解包可以用于元组、列表、字典。序列解包可以让我们方便的对多个变量赋值
x, y, z = (20, 30, 10)
print('x:', x)
print('y:', y)
print('z:', z)
(a, b, c) = (9, 8, 10)
print('a:', a)
print('b:', b)
print('c:', c)
[a, b] = ['hello', 'python']
print('a:', a)
print('b:', b)

print('#######################################################################################')
# 生成器对象
# 生成器的使用
s = (x * 2 for x in range(5))
print(s)  # 生成器对象
print(tuple(s))  # 使用 tuple函数构造一个元组
print(tuple(s))  # 输出一个空的元组，因为生成器只能访问一次元素。第二次就为空了。需要再生成一次
s = (x * 2 for x in range(5))
print('next 方法获取元素：', s.__next__())
print('next 方法获取元素：', s.__next__())
print('next 方法获取元素：', s.__next__())

print('#######################################################################################')
# 元组的基本增删改查操作

# 元组的创建
# 1.通过()创建元组，小括号可以省略。（注意：若元组只有一个元素，需要在该元素后面添加','）
test = (1)
print(type(test))  # 此时test的类型为int
test_tuple = 1,
print(type(test_tuple))  # 此时test_tuple的类型为元组(tuple)

# 2.通过tuple()创建元组（与list函数的功能基本一致）
test_list = list(x for x in 'google')
a = tuple('ABCDE')
b = tuple(range(1, 15, 2))
c = tuple((1, 15, 2))
d = tuple(test_list)
e = tuple(x * x for x in range(1, 5, 1))
print(a)
print(b)
print(c)
print(d)
print(e)

print('#######################################################################################')
# 元组的增删改查

# 元组是只读的，无法对内容进行修改
# test_tuple[1]=10          # TypeError: 'tuple' object does not support item assignment

# 元组的切片
test_tuple1 = test_tuple[:]
print(test_tuple1)
print(type(test_tuple1))

# 元组的排序（不能使用sort函数，会对元组进行修改，只能使用sorted函数，重新生成一个元组）
sorted_tuple = sorted(d)
print(sorted_tuple)

print('#######################################################################################')
# 使用zip函数对tuple进行打包
zipped = zip(a, b, c)
print('zipped', list(zip(a, b, c)))
i = zip(*zipped)
print('unzip', list(i))

# 使用zip函数对list进行打包
test_list2 = list(range(1, 15, 1))
zip_list = zip(test_list, test_list2)
print('zip_list', list(zip_list))

print('#######################################################################################')
# Python字典：使用键值对存储，可以存储任何类型的对象，是一种可变容器模型
# 列表中通过“下标数字”找到对应的对象。字典中通过“键对象”找到对应的“值对象”。
# “键”是任意的不可变数据，比如：整数、浮点数、字符串、元组。但是：列表、字典、集合这些可变对象，不能作为“键”。并且“键”不可重复。
# “值”可以是任意的数据，并且可重复。

# 字典的基本操作
# 字典的创建
# a) 通过{}、 dict()来创建字典对象
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
b = dict(name='gaoqi', age=18, job='programmer')
c = dict([("name", "gaoqi"), ("age", 18), ("job", 'programmer')])
d = {}  # 空的字典对象
e = dict()  # 空的字典对象
print('字典 a：', a)
print('字典 b：', b)
print('字典 c：', c)
print('字典 d：', d)
print('字典 e：', e)

# b) 通过 zip()创建字典对象
k = ['name', 'age', 'job']
v = ['gaoqi', 18, 'techer']
a = dict(zip(k, v))
print('字典 a：', a)

# C) 通过 fromkeys 创建值为空的字典
a = dict.fromkeys(['name', 'age', 'job'])
print('值为空的字典 a:', a)

# 字典的访问
# 1.通过'键'获得‘值’
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
print('name:', a['name'])
print('age:', a['age'])
print('job:', a['job'])
print('sex', a['sex'])  # 若键不存在，则抛出异常

# 2.使用get方法从字典中获取 key 对应的 value。
# 优点是：指定键不存在，返回 None；也可以设定指定键不存在时默认返回的对象。推荐使用 get()获取“值对象”。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
print('name:', a.get('name'))
print('age:', a.get('age'))
print('job:', a.get('job'))
print('sex:', a.get('sex'))

# 字典的常见操作
# 向字典添加元素,如果“键”已经存在，则覆盖旧的键值对；如果“键”不存在，则新增“键值对”。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
a['address'] = '北京'  # address 的键不存在，则新增
a['age'] = 28  # age 的键存在，则进行修改
print(a)

# update 方法可以用一个字典中的元素更新另外一个字典。该方法接收一个参数。该参数表示用作更新数据的字典数据源。如果 key 有重复，则直接覆盖。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
b = {'name': 'gaoxixi', 'money': 1000, 'sex': '男的'}
a.update(b)
print(a)

# 字典中元素的删除，可以使用 del()方法；或者 clear()删除所有键值对；pop()删除指定键值对，并返回对应的“值对象”。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
del (a['name'])  # del 删除元素
print(a)
b = a.pop('age')  # pop 删除元素，返回对应的值
print(b)
print(a)
a.clear()  # 清空字典元素
print(a)

# popitem()方法用于随机删除和返回该键值对。字典是“无序可变序列”，因此没有第一个元素、最后一个元素的概念；
# popitem 弹出随机的项，因为字典并没有"最后的元素"或者其他有关顺序的概念。若想一个接一个地移除并处理项，这个方法就非常有效（因为不用首先获取键的列表）。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
while len(a):
    b = a.popitem()
    print(b)

# print(a.popitem())
# print(a.popitem())
# print(a.popitem())

# item,keys,values方法
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
print(a.items())  # 字典中所有的 key-value 对
print(a.keys())  # 字典中所有的 keys
print(a.values())  # 字典中所有的 value
# 通过遍历 key，根据 key 获取值
for key in a.keys():
    print(key, ':', a.get(key))

print('#######################################################################################')
# 集合，集合是无序可变，元素不能重复。实际上，集合底层是字典实现，集合的所有元素都是字典中的“键对象”，因此是不能重复的且唯一的。

# 集合的创建
# a) 使用{}创建集合对象
a = {3, 5, 7}  # 集合存储整数
b = {'hello', 'python'}  # 集合存储字符串
c = {3, 4, True, 'abc', 56.4}  # 集合存储不同类型的数据
print(a)
print(b)
print(c)

# b) 使用 set()，将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保留一个。
a = ['a', 'b', 'c', 'b']
b = set(a)  # 将列表转换为集合
print(b)
c = (1, 2, 3, 4, 5)
d = set(c)  # 将元组转换为集合
print(d)

# 集合的添加操作
# 使用 add()实现集合添加元素
a = {3, 5, 7}
a.add('hello')  # add 方法添加元素
print(a)

# 集合的删除操作
# 使用 remove()实现集合删除指定元素、clear()清空整个集合
a = {10, 20, 30, 40, 50}
a.remove(20)  # 删除集合中的元素
print(a)
a.clear()  # 将集合清空
print(a)

# 集合的其他操作
a = {1, 3, 'sxt'}
b = {'he', 'it', 'sxt'}
print('并集：', a | b)  # 并集
print('并集：', a.union(b))  # 并集
print('交集：', a & b)  # 交集
print('交集：', a.intersection(b))  # 交集
print('差集：', a - b)  # 差集
print('差集：', a.difference(b))  # 差集
