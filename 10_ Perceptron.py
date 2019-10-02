# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


def tanh(x):
    return np.tanh(x)


def tanhDerivate(x):
    # return 1.0 - np.tanh(x) ** 2
    return 1.0 - x ** 2


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoidDerivate(y):
    # return sigmoid(x) * (1 - sigmoid(x))
    return y * (1 - y)


class MyPerceptron:
    def __init__(self, activation='sigmoid'):
        self.W = []
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activationDerivate = sigmoidDerivate
        if activation == 'tanh':
            self.activation = sigmoid
            self.activationDerivate = sigmoidDerivate

    # 训练函数，X矩阵，每行是一个实例 ，y是每个实例对应的结果，
    # learning_rate学习率
    # epochs进行更新的最大次数
    def fit(self, X, Y, learning_rate=0.1, epochs=100):
        #将偏置项b对应的1加入到X中
        temp = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0:-1] = X
        X = temp
        #初始化权重W
        self.W = (np.random.random(X.shape[1]) - 0.5) * 2

        for i in range(epochs):
            y = self.activation(np.dot(X, self.W.T))
            lost = 0.5*(Y-y).dot((Y-y))
            print("第", i, "次迭代后权重", self.W, "输出结果", y, "损失", lost)
            if (y == Y).all():
                print("在第", i, "次终止")
                break
            newW = self.W + learning_rate * \
                (((Y - y)*self.activationDerivate(y)).dot(X))
            self.W = newW

    # 绘图
    def show(self, X, Y):
        k = -self.W[0] / self.W[1]
        b = -self.W[2] / self.W[1]
        print("斜率：", k)
        print("截距：", b)
        xdata = np.linspace(0, 5)
        plt.figure()
        plt.plot(xdata, xdata * k + b, 'r')
        for i in range(X.shape[0]):
            if(1 == Y[i]):
                plt.plot(X[i][0], X[i][1], 'bo')
            else:
                plt.plot(X[i][0], X[i][1], 'yo')
        plt.show()

    # 预测函数
    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        x = temp
        y = self.activation(np.dot(x, self.W.T))
        return y


def main():
    X = np.array([[1,   1], [ 2,  1],
                  [-1, -1], [-2, -1]])
    Y = np.array([0, 0, 1, 1])
    pt = MyPerceptron('sigmoid')
    pt.fit(X, Y, 0.1, 400)
    pt.show(X, Y)
    for i in X:
        print("输入：", i, " 输出：", pt.predict(i))


if __name__ == "__main__":
    main()
