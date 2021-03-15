import functools
import math
from operator import itemgetter

import numpy as np


def question1():
    a = np.zeros(10)
    a[4] = 1
    print(a)


def question2():
    a = np.arange(10, 50)
    print(a)
    return a


def question3():
    a = question2()
    print(a[::-1])


def question4():
    a = np.random.random(size=(10, 10))
    print(type(a))
    print("最大值：", np.max(a))
    print("最小值：", np.min(a))


def question5():
    a = np.zeros((10, 10))
    a[:, 0] = a[:, -1] = a[0, :] = a[-1, :] = 1
    print(a)


def question6():
    my_list = [0, 1, 2, 3, 4] * 5
    print(my_list)
    a = np.array(my_list).reshape(5, 5)
    print(a)


def question7():
    a = np.linspace(0, 1, 12, endpoint=True, retstep=True)
    print(a)


# import math
#
#
# def compare(str1,str2):
#     int1 = str1
#     int2 = str2
#     len1 = len(str(str1))
#     len2 = len(str(str2))
#     length = min(len1,len2)
#     i = 1
#     while i <= length:
#         num1 = int(int1 / math.pow(10,(len1 - i)))
#         num2 = int(int2 / math.pow(10,(len2 - i)))
#         if  num1 > num2:
#             return 1
#         elif num1 < num2:
#             return -1
#         else:
#             int1 %= math.pow(10,len1-i)
#             int2 %= math.pow(10,len2-i)
#             i += 1
#             if i > length:
#                 if len1 > len2:
#                     if int(int1 / math.pow(10,(len1 - i))) > num2:
#                         return 1
#                     else:
#                         return -1
#                 elif len1 < len2:
#                     if int(int2 / math.pow(10,(len2 - i))) > num1:
#                         return -1
#                     else:
#                         return  1
#     return 0
#
# my_list = sorted([3, 30, 34, 5, 9])
# # sorted_list = sorted([str(num) for num in my_list], key=functools.cmp_to_key(compare))
# for i in range(len(my_list)-1):
#     for j in range(i,len(my_list)):
#         if  compare(my_list[i],my_list[j]) == -1:
#             my_list[i],my_list[j] = my_list[j],my_list[i]
#             j += 1
#         else:
#             j += 1
#     i += 1
#
# print(my_list)
#
# for i in range(len(my_list)):
#     my_list[i] = str(my_list[i])
#
# print(''.join(my_list))

import re
import operator


def check_password():
    My_list = input("请输入密码字符串：")
    password_list = My_list.split(',')
    re_az = re.compile(r'[a-z]+')
    re_AZ = re.compile(r'[A-Z]+')
    re_09 = re.compile(r'[0-9]+')
    re_sp = re.compile(r'[@#$]+')
    for i, element in enumerate(password_list):
        if ((re_az.search(element) != None) & (re_AZ.search(element) != None) & (re_09.search(element) != None) &
                (re_sp.search(element) != None) & (len(element) < 12) & (len(element) > 6)):
            print(element)


def people_Sort():
    num = int(input("请输入待比较人数："))
    people_list = []
    people_tuple = ()
    for i in range(num):
        people_Str = input("请输入第{0}人的信息：".format(i + 1))
        people_tuple = tuple(people_Str.split(','))
        people_list.append(people_tuple)
    people_list = sorted(people_list, key=lambda x: (x[0], int(x[1]), int(x[2])))
    print(people_list)



def num_generator(n):
    # n = input("请输入数值范围的上限：")
    i = 0
    while i <= n:
        if i % 7 == 0:
            yield i
            i += 1
        else:
            i += 1

for i in num_generator(21):
    print(i)


def word_times():
    # str = input("请输入待操作的字符串:")
    string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
    word_list = re.findall(r'[\w?]+', string)
    word_set = set(word_list)
    word_set = list(word_set)
    word_set.sort()
    time_list = []
    for i in range(len(word_set)):
        time_list.append(word_list.count(word_set[i]))
    word_dict = dict(zip(word_set, time_list))
    print("word_set", word_set)
    print(len(word_set))
    print("time_list", time_list)
    print("word_dict:", word_dict)
