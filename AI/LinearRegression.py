# # 代码实战解析解求解模型的方法
# # numpy是去做数值计算的
import numpy as np
# # matplotlib是关于绘图的
# import matplotlib.pyplot as plt
#
# np.random.seed(42)
# 回归，有监督的机器学习，X，y
# X1 = 2*np.random.rand(100, MLP_Handwriting_numbers)
# X2 = 3*np.random.rand(100, MLP_Handwriting_numbers)
# # 这里要模拟出来的数据y是代表真实的数据，所以也就是y_hat+error
# y = 5 + 4*X1 + 3*X2 + np.random.randn(100, MLP_Handwriting_numbers)
# 为了去求解W0截距项，我们给X矩阵一开始加上一列全为1的X0
# X_b = np.c_[np.ones((100, MLP_Handwriting_numbers)), X1, X2]
# print(X_b)
# # 实现解析解的公式来求解θ
# θ = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
# print(θ)
#
# # 使用模型去做预测
# X_new = np.array([[0, 0],
#                   [2, 3]])
# X_new_b = np.c_[np.ones((2, MLP_Handwriting_numbers)), X_new]
# print(X_new_b)
# y_predict = X_new_b.dot(θ)
# print(y_predict)
#
# # 绘图进行展示真实的数据点和我们预测用的模型
# # plt.plot(X_new[:, 0], y_predict, 'r-')
# # plt.plot(X1, y, 'b.')
# # plt.axis([0, 2, 0, 25])
# # plt.show()
#
# # 三维图
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_trisurf(X1.reshape(100), X2.reshape(100), y.reshape(100))
# plt.show()

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


X1 = 2*np.random.rand(100, 1)
X2 = 2*np.random.rand(100, 1)
X = np.c_[X1, X2]

y = 4 + 3*X1 + 5*X2 + np.random.randn(100, 1)

reg = LinearRegression(fit_intercept=True)
reg.fit(X, y)
print(reg.intercept_, reg.coef_)

X_new = np.array([[0, 0],
                  [2, 1],
                  [2, 4]])
y_predict = reg.predict(X_new)

# 绘图进行展示真实的数据点和我们预测用的模型
plt.plot(X_new[:, 0], y_predict, 'r-')
plt.plot(X1, y, 'b.')
plt.axis([0, 2, 0, 25])
plt.show()

# 三维图
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_trisurf(X1.reshape(100), X2.reshape(100), y.reshape(100))
# plt.show()
