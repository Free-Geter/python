import numpy as np

# numpy.around() 函数返回指定数字的四舍五入值。
# numpy.around(a,decimals)
# 参数说明：
# a: 数组。
# decimals: 舍入的小数位数。 默认值为 0。 如果为负，整数将四舍五入到小数点左侧的位置。
# numpy.floor() 返回数字的下舍整数。
# numpy.ceil() 返回数字的上入整数。
import numpy as np
a = np.array([1.0,4.55, 123, 0.567, 25.532])
print ('原数组：')
print (a)
print ('around 舍入后：')
print (np.around(a))
print (np.around(a, decimals = 1))
print (np.around(a, decimals = -1))
print('floor 向下取整：')
print(np.floor(a))
print('ceil 向上取整：')
print(np.ceil(a))


print('#######################################################################################')
# 数组的创建
# 使用array 创建
# numpy 模块的 array 函数可以生成多维数组。例如，如果要生成一个二维数组，需要向 array 函数传递一个列表类型的参数。
# 每一个列表元素是一维的 ndarray 类型数组，作为二维数组的行。另外，通过 ndarray 类的 shape 属性可以获得数组每一维的元素个数（元组形式），
# 也可以通过 shape[n]形式获得每一维的元素个数，其中 n 是维度，从 0 开始。
# 创建一维数组
b = np.array([1, 2, 3, 4, 5, 6])
print(b)
print(type(b))
print('b 数组的维度：', b.shape)

# 创建二维数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print('a 数组的维度:', a.shape)

# ndmin参数的作用
c = np.array([1, 2, 3, 4, 5, 6], ndmin=3)
print(c)
print('c 数组的维度:', c.shape)

# dtype参数的作用
a = np.array([1, 2, 3, 4, 5, 6], dtype=complex)
print(a)

string = np.array(['A', 'B'], dtype=str)
print(string)
print(type(string[1]))
print(string[1])

print('#######################################################################################')
# 使用arange创建数组
# 使用arange函数创建数值范围并返回ndarray对象，函数语法格式如下：
# numpy.arange(start, stop, step, dtype)
x = np.arange(10, 20, 2, dtype=float)
print(x)

# arange创建二维数组
b = np.array([np.arange(1, 4), np.arange(4, 7), np.arange(7, 10)])
print(b)
print(b[1][1])
print(type(b[1][1]))
print('b 数组的维度：', b.shape)

print('#######################################################################################')
# 生成随机数

# numpy.random.random(size=None)
# 返回[0.0, 1.0)范围的随机数
import numpy as np

print('生成一维（4，）的随机数组：')
x = np.random.random(size=4)
print(x)
print('生成二维（3,4）的随机数组：')
y = np.random.random(size=(3, 4))
print(y)

# numpy.random.randint()的使用
# 生成 [0,low)范围的随机整数
x = np.random.randint(5, size=10)
print(x)
# 生成[low,high)范围的随机整数
y = np.random.randint(5, 10, size=10)
print(y)
# 生成[low,high)范围的 2*4 的随机整数
z = np.random.randint(5, 10, size=(2, 4))
print(z)

# randn 函数返回一个或一组样本，具有标准正态分布
x = np.random.randn()
print(x)
y = np.random.randn(2, 4)
print(y)
z = np.random.randn(2, 3, 4)
print(z)

# 正态分布（高斯分布）loc：期望 scale：方差 size 形状
print(np.random.normal(loc=3, scale=4, size=(2, 2, 3)))

# ndarry的属性
# NumPy 最重要的一个特点是其N维数组对象ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
# ndarray 对象是用于存放同类型元素的多维数组。
# ndarray 中的每个元素在内存中都有相同存储大小的区域。
# ndarray 内部由以下内容组成：
# • 一个指向数据（内存或内存映射文件中的一块数据）的指针。
# • 数据类型或 dtype，描述在数组中的固定大小值的格子。
# • 一个表示数组形状（shape）的元组，表示各维度大小的元组。
import numpy as np

x1 = np.random.randint(10, size=6)
print(x1)
x2 = np.random.randint(10, size=(3, 4))
print(x2)
x3 = np.random.randn(3, 4, 5)
print('ndim 属性'.center(20, '*'))
print('ndim:', x1.ndim, x2.ndim, x3.ndim)
print('shape 属性'.center(20, '*'))
print('shape:', x1.shape, x2.shape, x3.shape)
print('dtype 属性'.center(20, '*'))
print('dtype:', x1.dtype, x2.dtype, x3.dtype)
print('size 属性'.center(20, '*'))
print('size:', x1.size, x2.size, x3.size)
print('itemsize 属性'.center(20, '*'))  # 一个字节是 8 位
print('itemsize:', x1.itemsize, x2.itemsize, x3.itemsize)

print('#######################################################################################')
# 其他方法创建数组

# zeros 创建指定大小的数组，数组元素以 0 来填充：
x = np.zeros(5)
print(x)
# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)
z = np.zeros((2, 2))
print(z)

# numpy.ones 创建指定形状的数组，数组元素以 1 来填充：
import numpy as np

x = np.ones(5)
print(x)
y = np.ones((3, 4), dtype=int)
print(y)

# numpy.empty() 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组，里面的元素的值是之前内存的值：
x = np.empty([3, 2], dtype=int)
print(x)

# linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
import numpy as np

x = np.linspace(10, 20, 5, endpoint=True, retstep=True)
print(x)

# numpy.logspace 函数用于创建一个于等比数列。格式如下：
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
import numpy as np

x = np.logspace(0, 9, 10, base=2)
print(x)

# 其他函数
# numpy.zeros_like(arr)
# numpy.ones_like(arr)

print('#######################################################################################')

# 数组的切片和索引

# 切片:
# 一维数组的切片
x = np.arange(10)
print('原数组：', x)
y = x[2:7:2]
z = x[2:]
print('对数组进行[2:7:2]切片：', y)
print('对数组进行[2:]切片：', z)

# 二维数组切片
x = np.arange(1, 13)
a = x.reshape(4, 3)
print('数组元素')
print(a)
print('所有行的第二列')
print(a[:, 1])
print('奇数行的第一列')
print(a[::2, 0])

# 索引:
# 一维数组的索引
x = np.arange(1, 13)
a = x.reshape(4, 3)
print('数组元素')
print(a)
print('获取第二行')
print(a[1])
print('获取第三行第二列')
print(a[2][1])

# 二维数组的索引
a = np.arange(1, 13).reshape(4, 3)
print('数组元素')
print(a)
print('获取第三行第二列的结果：', a[2, 1])
print('同时获取第三行第二列，第四行第一列')
print('分别获取：', np.array((a[2, 1], a[3, 0])))
print('第一个元组是行索引，第二个元组是列索引获取：', a[(2, 3), (1, 0)])

# 负索引的使用
x = np.arange(1, 13).reshape(4, 3)
print('数组元素')
print(x)
print('获取最后一行')
print(a[-1])
print('行进行倒序')
print(a[::-1])
print('行列都倒序')
print(a[::-1, ::-1])

# copy()函数实现数组的复制
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
sub_array = a[:2, :2]
sub_array[0][0] = 1000
print(a)
print(sub_array)
print('copy' * 20)
sub_array = np.copy(a[:2, :2])
sub_array[0][0] = 2000  # 这里的sub_array不再是原数组的视图，此修改不会影响原数组
print(a)
print(sub_array)

# 改变数组的维度
import numpy as np

# 创建一维的数组
a = np.arange(24)
print(a)
print('数组 a 的维度：', a.shape)
print('-' * 30)
# 使用 reshape 将一维数组变成三维数组
b = a.reshape(2, 3, 4)
print(b)
print('数组 b 的维度：', b.shape)
print('-' * 30)
# 将 a 变成二维数组
c = a.reshape(3, 8)
print(c)
print('数组 c 的维度：', c.shape)
print('-' * 30)
# 使用 ravel 函数将三维的 b 变成一维的数组
a1 = b.ravel()
print(a1)
print('-' * 30)
# 使用 flatten 函数将二维的 c 变成一维的数组
a2 = c.flatten()
print(a2)
print('-' * 30)

print('#######################################################################################')
# 数组的拼接
# 水平拼接：使用 hstack 函数将两个数组水平组合的代码：hstack(A,B)。
# 数组水平组合必须要满足一个条件，就是所有参与水平组合的数组的行数必须相同，否则进行水平组合会抛出异常。
# 垂直拼接：通过 vstack 函数可以将两个或多个数组垂直组合起来形成一个数组
# numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：
# numpy.concatenate((a1, a2, ...), axis)
# 其中参数 a1, a2, ...指相同类型的数组；axis 指沿着它连接数组的轴，默认为 0。
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.array([['a','b','c'],['d','e','f']])
print(b)
print('默认垂直拼接')
print(np.concatenate([a,b]))
print('垂直方向拼接 相当于 vstack')
print(np.concatenate([a,b],axis=0))
print('水平方向拼接 相当于 hstack')
print(np.concatenate([a,b],axis=1))
# vstack、hstack
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.array([['a','b','c'],['d','e','f']])
print(b)
print('x 轴方向及垂直堆叠')
print(np.vstack([a,b]))
print('y 轴方向及水平堆叠')
print(np.hstack([a,b]))

print('#######################################################################################')
# 数组的分割
# numpy.split 函数 沿特定的轴将数组分割为子数组，格式如下：
# numpy.split(ary, indices_or_sections, axis)
# 参数说明：
# • arry：被分割的数组。
# • indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置。
# • axis：沿着哪个维度进行切分，默认为 0，横向切分。为 1 时，纵向切分。

# 分割一维数组
x=np.arange(1,9)
a=np.split(x,4)
print(type(a))
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
#传递数组进行分隔
b=np.split(x,[3,5])
print(b)

# 分割二维数组
#创建两个数组
a=np.array([[1,2,3],[4,5,6],[11,12,13],[14,15,16]])
print('axis=0 垂直方向 平均分隔')
r=np.split(a,2,axis=0)
print(r[0])
print(r[1])
print('axis=1 水平方向 按位置分隔')
r=np.split(a,[2],axis=1)
print(r)

print('#######################################################################################')
# 数组的转置
#transpose 进行转置
#二维转置
import numpy as np
a=np.arange(1,13).reshape(2,6)
print('原数组 a')
print(a)
print('转置后的数组')
print(a.transpose())
#多维数组转置
aaa=np.arange(1,37).reshape(1,3,3,4)
#将 1,3,3,4 转换为 3,3,4,1
print(np.transpose(aaa,[1,2,3,0]).shape)

print('#######################################################################################')
# 数组的算数运算
a=np.arange(9,dtype=np.float).reshape(3,3)
b=np.array([10,10,10])
print('两数组进行加法运算 add 或+的结果：')
print(np.add(a,b))
print('两数组进行减法运算 substract 或-的结果：')
print(a-b)
print('两数组进行乘法运算 multiply 或*的结果：')
print(np.multiply(a,b))
print('两数组进行除法运算 divide 或/的结果：')
print(np.divide(a,b))

# 通用函数指定输出结果的用法
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)


print('#######################################################################################')
# NumPy 提供了很多统计函数，用于从数组中查找最小元素，最大元素，百分位标准差和方差等。 具体如下表所示：
# https://cdn.nlark.com/yuque/0/2021/png/12418439/1613286285803-6f43bc62-3675-4e81-bc3c-4495ebbd5ec9.png?x-oss-process=image%2Fresize%2Cw_1264

# numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
import numpy as np
a=np.arange(12).reshape(3,4)
print('原来的数组')
print(a)
print('power(a,2)的结果：')
print(np.power(a,2))

# median ()函数的使用一
a=np.array([4,2,1,5])
#计算偶数的中位数
print('偶数的中位数：',np.median(a))
a=np.array([4,2,1])
print('奇数个的中位数：',np.median(a))
a=np.arange(1,16).reshape(3,5)
print('原来的数组')
print(a)
print('调用 median 函数')
print(np.median(a))
print('调用 median 函数，axis=1 行的中值')
print(np.median(a,axis=1))
print('调用 median 函数，axis=0 列的中值')
print(np.median(a,axis=0))

