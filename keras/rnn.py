import keras
from keras.datasets import mnist
from keras.layers import Activation, Dense, Reshape
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.utils import np_utils

K = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('f') / 255.0  # (60000, 28, 28)
x_test = x_test.astype('f') / 255.0
y_train = np_utils.to_categorical(y_train, K)  # int -> one-of-vector
y_test = np_utils.to_categorical(y_test, K)

model = Sequential()
model.add(Reshape((1, 28 * 28), input_shape=(28, 28)))  # tensorflow-order!!
model.add(LSTM(20, input_dim=1, input_length=28*28))
model.add(Dense(K))
model.add(Activation("softmax"))


board = keras.callbacks.TensorBoard(log_dir='.log', histogram_freq=1)

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=30, nb_epoch=10,
          callbacks=[board],
          validation_data=(x_test, y_test))
