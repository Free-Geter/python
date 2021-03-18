# def foo(num):
#     print("starting...")
#     while num<10:
#         num=num+MLP_Handwriting_numbers
#         yield num
# for n in foo(0):
#     print(n)


# from datetime import datetime
#
#
# week = datetime.strptime('2021-03-07', "%Y-%m-%d").weekday()
# print(week)
#
# print(week)

import numpy as np
import operator


class point:
    def __init__(self, x, y, price=None, d=None):
        self.x = x
        self.y = y
        self.price = price
        self.d = d

    def dist(self, p):
        if isinstance(p, point):
            d = ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5
            self.d = d
            return d
        else:
            print("is not instance!")
            return

    def __lt__(self, other):
        if isinstance(other, point):
            return self.d < other.d
        else:
            print("is not instance!")

    def __gt__(self, other):
        if isinstance(other, point):
            return self.d > other.d
        else:
            print("is not instance!")


def knn_class(k=3, test=[3, 2]):
    X = np.array([[1, 1], [1, 1.5], [2, 2], [4, 3], [4, 4]])
    Y = np.array(['A', 'A', 'A', 'B', 'B'])
    point_list = []
    dist_list = []
    test_point = point(test[0], test[1])
    for i in range(len(X)):
        temp = point(X[i][0], X[i][1], Y[i])
        point_list.append(temp)
        dist_list.append(temp.dist(test_point))
    list = sorted(point_list)
    class_count = {}
    for i in range(k):
        label = list[i].price
        class_count[label] = class_count.get(label,0) + 1
    return sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)[0][0]


print(knn_class())
