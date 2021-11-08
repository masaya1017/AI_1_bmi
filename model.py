

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizer_v2.rmsprop import RMSProp
from keras.optimizers import rmsprop_v2

in_size = 2
nb_classes = 6

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSProp(),
    metrics=['accuracy']
)
model.save('hw_model.h5')
print("saved")
