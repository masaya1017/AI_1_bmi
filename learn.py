from numpy.lib.function_base import append
import os
import sqlite3
import numpy as np
import keras
import tensorflow
from keras.models import load_model
from tensorflow.keras.utils import to_categorical


db_path = "./hw.sqlite3"
select_sql = "SELECT * FROM person ORDER BY id DESC LIMIT 100"

x = []
y = []

with sqlite3.connect(db_path) as conn:
    for row in conn.execute(select_sql):
        id, height, weight, type_no = row
        height = height/200
        weight = weight/150
        x.append(np.array([height, weight]))
        y.append(type_no)

model = load_model('hw_model.h5')

if os.path.exists('hw_weights.h5'):
    model.load_weights('hw_weights.h5')

nb_classes = 6
y = to_categorical(y, nb_classes)

model.fit(np.array(x), y, batch_size=50, epochs=200)

model.save_weights('hw_weights.h5')
