import tensorflow as tf

X = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])


class Linear(tf.keras.Model):
    def __init__(self):
        super().__init__()
        # Keras的全连接层：线性变换 + 激活函数
        self.dense = tf.keras.layers.Dense(
            # 输出张量的维度；
            units=1,
            # 激活函数，对应于 f(AW + b) 中的 f ，默认为无激活函数（ a(x) = x ）。
            # 常用的激活函数包括 tf.nn.relu 、 tf.nn.tanh 和 tf.nn.sigmoid ；
            activation=None,
            # 是否加入偏置向量 bias ，即 f(AW + b) 中的 b。默认为 True ；
            use_bias = True,
            # 权重矩阵 kernel 和偏置向量 bias 两个变量的初始化器。默认为 tf.glorot_uniform_initializer MLP_Handwriting_numbers 。
            # 设置为 tf.zeros_initializer 表示将两个变量均初始化为全 0；
            kernel_initializer=tf.zeros_initializer(),
            bias_initializer=tf.zeros_initializer()
        )

    def call(self, input):
        output = self.dense(input)
        return output


# 以下代码结构与前节类似
model = Linear()
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
for i in range(100):
    with tf.GradientTape() as tape:
        y_pred = model(X)      # 调用模型 y_pred = model(X) 而不是显式写出 y_pred = a * X + b
        loss = tf.reduce_mean(tf.square(y_pred - y))
    grads = tape.gradient(loss, model.variables)    # 使用 model.variables 这一属性直接获得模型中的所有变量
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
print(model.variables)