from keras.models import load_model
import numpy as np

model = load_model('hw_model.h5')
model.load_weights('hw_weights.h5')

labels = ['低体重', '普通体重', '肥満(１度)', '肥満(2度)', '肥満(3度)', '肥満(4度)']

# テストデータ
height = 160
weight = 50
test_x = [height/200, weight/150]

pre = model.predict(np.array([test_x]))
idx = pre[0].argmax()
print(labels[idx], '/可能性:', pre[0][idx])
