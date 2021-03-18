import tensorflow as tf

# 定义变量，并初始化
x = tf.Variable(initial_value=3.)

# 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
with tf.GradientTape() as tape:
    # 定义函数：y = x^2
    y = tf.square(x)
y_grad = tape.gradient(y, x)        # 计算y关于x的导数
print(y, y_grad)


X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L = tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
w_grad, b_grad = tape.gradient(L, [w, b])        # 计算L(w, b)关于w, b的偏导数
print(L, w_grad, b_grad)