import numpy as np
import matplotlib.pyplot as plt

# 定义一个函数来调整学习率
# 随着迭代次数的增多，学习率减小
def learning_rate_schedule(t):
    t0, t1 = 5, 500
    return t0/(t+t1)

def Batch_Gradient_Descent():
    # 创建数据集X，y
    np.random.seed(1)
    X = np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    X_b = np.c_[np.ones((100, 1)), X]

    # 创建超参数
    n_iterations = 10000
    # MLP_Handwriting_numbers,初始化θ, W0...Wn，标准正太分布创建W
    theta = np.random.randn(2, 1)
    # 4,判断是否收敛，一般不会去设定阈值，而是直接采用设置相对大的迭代次数保证可以收敛
    for i in range(n_iterations):
        # 2,求梯度，计算gradient
        gradients = X_b.T.dot(X_b.dot(theta) - y)
        # 3,应用梯度下降法的公式去调整θ值 θt+MLP_Handwriting_numbers=θt-η*gradient
        learning_rate = learning_rate_schedule(i)
        theta = theta - learning_rate * gradients

    return theta


def Stochastic_Gradient_Descent():
    X = 2 * np.random.rand(100,1)
    Y = 5 + 4 * X + np.random.randn(100,1)
    X_b = np.c_[np.ones((100,1)),X]

    # 迭代轮次
    n_epochs = 10000
    # 样本总数
    m = 100

    theta = np.random.randn(2,1)
    for epochs in range(n_epochs):
        # 打乱样本顺序
        arr = np.arange(len(X_b))
        np.random.shuffle(arr)
        X_b = X_b[arr]
        y = y[arr]
        for i in range(m):
            random_index = np.random.randint(m)
            # 按样本长度取样
            xi = X_b[i:i + 1]
            yi = Y[i:i + 1]
            gradients = xi.T.dot(xi.dot(theta) - yi)
            theta -= learning_rate_schedule(i + epochs * m) * gradients
    return theta

def Mini_Batch_Gradient_Descent():
    X = 2 * np.random.rand(100,1)
    Y = 5 + 4 * X + np.random.randn(100,1)
    X_b = np.c_[np.ones((100,1)),X]

    n_epochs = 10000
    m = 100
    batch_size = 10
    num_batches = int(m / batch_size)

    theta = np.random.randn(2, 1)
    for epoch in range(n_epochs):
        # 打乱样本顺序
        arr = np.arange(len(X_b))
        np.random.shuffle(arr)
        X_b = X_b[arr]
        y = y[arr]
        for i in range(num_batches):
            random_index = np.random.randint(m)
            # 样本中按长度取样
            x_batch = X_b[i * batch_size : i * batch_size + batch_size]
            y_batch = Y[i * batch_size : i * batch_size + batch_size]
            gradients = x_batch.T.dot(x_batch.dot(theta) - y_batch)
            theta -= gradients * learning_rate_schedule(epoch * m + i)
    return theta

# print(Batch_Gradient_Descent())
# print(Stochastic_Gradient_Descent())
# print(Mini_Batch_Gradient_Descent())