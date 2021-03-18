# 卷积神经网络 （Convolutional Neural Network, CNN）是一种结构类似于人类或动物的 视觉系统 的人工神经网络，
# 包含一个或多个卷积层（Convolutional Layer）、池化层（Pooling Layer）和全连接层（Fully-connected Layer）。
import tensorflow as tf
import numpy as np

class MNISTLoader():
    def __init__(self):
        mnist = tf.keras.datasets.mnist
        (self.train_data, self.train_label), (self.test_data, self.test_label) = mnist.load_data()
        # MNIST中的图像默认为uint8（0-255的数字）。以下代码将其归一化到0-1之间的浮点数，并在最后增加一维作为颜色通道
        # 由于这里读入的是灰度图片，色彩通道数为 MLP_Handwriting_numbers（彩色 RGB 图像色彩通道数为 3），所以我们使用 np.expand_dims() 函数为图像数据手动在最后添加一维通道。
        # 如果图像是彩色的（例如有 RGB 三个通道）,我们可以为每个通道准备一个 3×3 的权值矩阵，即一共有 3×3×3=27 个权值。对于每个通道，均使用自己的权值矩阵进行处理，输出时将多个通道所输出的值进行加和即可。
        self.train_data = np.expand_dims(self.train_data.astype(np.float32) / 255.0, axis=-1)      # [60000, 28, 28, MLP_Handwriting_numbers]
        self.test_data = np.expand_dims(self.test_data.astype(np.float32) / 255.0, axis=-1)        # [10000, 28, 28, MLP_Handwriting_numbers]
        self.train_label = self.train_label.astype(np.int32)    # [60000]
        self.test_label = self.test_label.astype(np.int32)      # [10000]
        self.num_train_data, self.num_test_data = self.train_data.shape[0], self.test_data.shape[0]

    def get_batch(self, batch_size):
        # 从数据集中随机取出batch_size个元素并返回
        index = np.random.randint(0, self.num_train_data, batch_size)
        return self.train_data[index, :], self.train_label[index]

class CNN(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1 = tf.keras.layers.Conv2D(
            filters=32,             # 卷积层神经元（卷积核）数目
            kernel_size=[5, 5],     # 感受野大小
            # 每次卷积后的结果相比于原始图像而言，四周都会 “少一圈”。比如上面 7×7 的图像，卷积后变成了 5×5 ，
            # 这有时会为后面的工作带来麻烦。因此，我们可以设定 padding 策略。在 tf.keras.layers.Conv2D 中，
            # 当我们将 padding 参数设为 same 时，会将周围缺少的部分使用 0 补齐，使得输出的矩阵大小和输入一致。
            padding='same',         # padding策略（vaild 或 same）
            activation=tf.nn.relu   # 激活函数
        )
        self.pool1 = tf.keras.layers.MaxPool2D(pool_size=[2, 2], strides=2)
        self.conv2 = tf.keras.layers.Conv2D(
            filters=64,
            kernel_size=[5, 5],
            padding='same',
            activation=tf.nn.relu
        )
        # 池化层（Pooling Layer）的理解则简单得多，其可以理解为对图像进行降采样的过程，对于每一次滑动窗口中的所有值，
        # 输出其中的最大值（MaxPooling）、均值或其他方法产生的值。例如，对于一个三通道的 16×16 图像（即一个 16*16*3 的张量），
        # 经过感受野为 2×2，滑动步长为 2 的池化层，则得到一个 8*8*3 的张量。
        self.pool2 = tf.keras.layers.MaxPool2D(pool_size=[2, 2], strides=2)
        self.flatten = tf.keras.layers.Reshape(target_shape=(7 * 7 * 64,))
        self.dense1 = tf.keras.layers.Dense(units=1024, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)

    def call(self, inputs):
        x = self.conv1(inputs)                  # [batch_size, 28, 28, 32]
        x = self.pool1(x)                       # [batch_size, 14, 14, 32]
        x = self.conv2(x)                       # [batch_size, 14, 14, 64]
        x = self.pool2(x)                       # [batch_size, 7, 7, 64]
        x = self.flatten(x)                     # [batch_size, 7 * 7 * 64]
        x = self.dense1(x)                      # [batch_size, 1024]
        x = self.dense2(x)                      # [batch_size, 10]
        output = tf.nn.softmax(x)
        return output


if __name__ == '__main__':
    num_epochs = 5
    batch_size = 50
    learning_rate = 0.001
    model = CNN()
    data_loader = MNISTLoader()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    # 然后迭代进行以下步骤：
    # 从 DataLoader 中随机取一批训练数据；
    # 将这批数据送入模型，计算出模型的预测值；
    # 将模型预测值与真实值进行比较，计算损失函数（loss）。这里使用 tf.keras.losses 中的交叉熵函数作为损失函数；
    # 计算损失函数关于模型变量的导数；
    # 将求出的导数值传入优化器，使用优化器的 apply_gradients 方法更新模型参数以最小化损失函数（优化器的详细使用方法见 前章 ）。
    num_batches = int(data_loader.num_train_data // batch_size * num_epochs)
    for batch_index in range(num_batches):
        X, y = data_loader.get_batch(batch_size)
        with tf.GradientTape() as tape:
            y_pred = model(X)
            # 在这里，我们没有显式地写出一个损失函数，而是使用了 tf.keras.losses 中的 sparse_categorical_crossentropy （交叉熵）函数，
            # 将模型的预测值 y_pred 与真实的标签值 y 作为函数参数传入，由 Keras 帮助我们计算损失函数的值。
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=y, y_pred=y_pred)
            loss = tf.reduce_mean(loss)
            print("batch %d: loss %f" % (batch_index, loss.numpy()))
        grads = tape.gradient(loss, model.variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))


    # 最后，我们使用测试集评估模型的性能。这里，我们使用 tf.keras.metrics 中的 SparseCategoricalAccuracy 评估器来评估模型在测试集上的性能，
    # 该评估器能够对模型预测的结果与真实结果进行比较，并输出预测正确的样本数占总样本数的比例。
    # 我们迭代测试数据集，每次通过 update_state() 方法向评估器输入两个参数： y_pred 和 y_true ，即模型预测出的结果和真实结果。
    # 评估器具有内部变量来保存当前评估指标相关的参数数值（例如当前已传入的累计样本数和当前预测正确的样本数）。
    # 迭代结束后，我们使用 result() 方法输出最终的评估指标值（预测正确的样本数占总样本数的比例）。
    sparse_categorical_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
    num_batches = int(data_loader.num_test_data // batch_size)
    for batch_index in range(num_batches):
        start_index, end_index = batch_index * batch_size, (batch_index + 1) * batch_size
        y_pred = model.predict(data_loader.test_data[start_index: end_index])
        sparse_categorical_accuracy.update_state(y_true=data_loader.test_label[start_index: end_index], y_pred=y_pred)
    print("test accuracy: %f" % sparse_categorical_accuracy.result())