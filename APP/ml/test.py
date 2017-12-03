import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard
from keras.layers import Dense, Activation, Flatten
from keras.layers import MaxPooling2D
from keras.layers.convolutional import Conv2D
from keras.models import Sequential
from keras.utils import np_utils
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

batch_size = 100
nb_classes = 15
nb_epoch = 2

img_rows, img_cols = 256, 256
channels = 1
nb_filters = 32
kernel_size = (2, 2)

# Import data
labels = pd.read_csv("/home/chik/Downloads/images/newcsv.csv")
X = np.load("/home/chik/Downloads/images/X_sample.npy")

y = labels.Finding_Labels
# y = np.array(pd.get_dummies(y))
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
y = y.reshape(-1, 1)

print("Splitting data into test/ train datasets")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Reshaping Data")
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, channels)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, channels)

print("X_train Shape: ", X_train.shape)
print("X_test Shape: ", X_test.shape)

input_shape = (img_rows, img_cols, channels)

print("Normalizing Data")
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)
print("y_train Shape: ", y_train.shape)
print("y_test Shape: ", y_test.shape)

model = Sequential()



model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1]),
                 padding='valid',
                 strides=1,
                 input_shape=(img_rows, img_cols, channels)))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))


nb_filters = 64
kernel_size = (4, 4)

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))


nb_filters = 128
kernel_size = (8, 8)

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
print("Model flattened out to: ", model.output_shape)

model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print(model.summary())

stop = EarlyStopping(monitor='acc',
                     min_delta=0.001,
                     patience=2,
                     verbose=0,
                     mode='auto')

tensor_board = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

model.fit(X_train, y_train, batch_size=batch_size, epochs=nb_epoch,
          verbose=1,
          validation_split=0.2,
          class_weight='auto',
          callbacks=[stop, tensor_board]
          )

model.evaluate(X_test, y_test)