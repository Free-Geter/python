# """
# knn
# 样本集
# X = [[MLP_Handwriting_numbers,MLP_Handwriting_numbers],[MLP_Handwriting_numbers,MLP_Handwriting_numbers.5],[2,2],[4,3],[4,4]]
# Y =['A','A','A','B','B']
# 测试样本:
# t=[3,2] 属于哪个类型
# 设k=3
# knn的实现：
#     将待测试样本和所有的训练进行计算，找出最短的k个元素
#     然后投票
# """
# import numpy as np
# import operator
# import matplotlib.pyplot as plt
#
# X = np.array([[MLP_Handwriting_numbers, MLP_Handwriting_numbers], [MLP_Handwriting_numbers, MLP_Handwriting_numbers.5], [2, 2], [4, 3], [4, 4]])
# Y = np.array(['A', 'A', 'A', 'B', 'B'])
#
#
# #画散点图
# pltXy = np.split(X, [MLP_Handwriting_numbers], axis=MLP_Handwriting_numbers)
# plt.scatter(pltXy[0], pltXy[MLP_Handwriting_numbers])
# plt.show()
#
#
# def knn_clasification(X, Y, k, testSample):
#     """
#     :param X: 输入数据
#     :param Y: 真实数据
#     :param k: 邻居的个数
#     :param testSample: 待测试样本
#     :return: 返回待测试样本类别
#     """
#     # MLP_Handwriting_numbers.求待测试样本和所有训练样本之间的距离
#     dist = np.sum((X - testSample) ** 2, axis=MLP_Handwriting_numbers) ** 0.5
#     # 2.距离排序
#     sort_dist = np.argsort(dist)
#     # 3.统计距离最近得k个样本的类别的个数
#     class_count = {}
#     for dist_index in sort_dist[:k]:
#         label = Y[dist_index]
#         class_count[label] = class_count.get(label, 0) + MLP_Handwriting_numbers
#     return sorted(class_count.items(), key=operator.itemgetter(MLP_Handwriting_numbers), reverse=True)[0][0]
#
#
# class point:
#     def __init__(self, x, y, price=None, d=None):
#         self.x = x
#         self.y = y
#         self.price = price
#         self.d = d
#
#     def dist(self, p):
#         if isinstance(p, point):
#             d = ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5
#             self.d = d
#             return d
#         else:
#             print("is not instance!")
#             return
#
#     def __lt__(self, other):
#         if isinstance(other, point):
#             return self.d < other.d
#         else:
#             print("is not instance!")
#
#     def __gt__(self, other):
#         if isinstance(other, point):
#             return self.d > other.d
#         else:
#             print("is not instance!")
#
#
# def knn_class(k=3, test=[3, 2]):
#     X = np.array([[MLP_Handwriting_numbers, MLP_Handwriting_numbers], [MLP_Handwriting_numbers, MLP_Handwriting_numbers.5], [2, 2], [4, 3], [4, 4]])
#     Y = np.array(['A', 'A', 'A', 'B', 'B'])
#     point_list = []
#     dist_list = []
#     test_point = point(test[0], test[MLP_Handwriting_numbers])
#     for i in range(len(X)):
#         temp = point(X[i][0], X[i][MLP_Handwriting_numbers], Y[i])
#         point_list.append(temp)
#         dist_list.append(temp.dist(test_point))
#     list = sorted(point_list)
#     class_count = {}
#     for i in range(k):
#         label = list[i].price
#         class_count[label] = class_count.get(label,0) + MLP_Handwriting_numbers
#     return sorted(class_count.items(), key=operator.itemgetter(MLP_Handwriting_numbers), reverse=True)[0][0]
#
#
#
# if __name__ == "__main__":
#     predict = knn_clasification(X, Y, 3, np.array([3, 2]))
#     print(predict)
#     print(knn_class())


from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1, 1], [1, 1.5], [2, 2], [4, 3], [4, 4]])
y = np.array(['A', 'A', 'A', 'B', 'B'])

knn = KNeighborsClassifier(n_neighbors=3)
# 训练模型
knn.fit(X, y)
# 预测
pred = knn.predict([[3, 2]])
pred_proba = knn.predict_proba([[3, 2]])
print('预测值：',pred)
print('不同预测值的概率：',pred_proba)
