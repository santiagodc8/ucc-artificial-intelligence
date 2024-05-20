import tensorflow as tf
from keras import layers,models
import os
import numpy as np
import cv2
import random

width = 300
height = 300
ruta_train = 'cats_and_dogs/train/'
ruta_predict = 'cats_and_dogs/predit'

'''
train_x = []
train_y = []


for i in os.listdir(ruta_train):
    for j in os.listdir(ruta_train + i):
        img = cv2.imread(ruta_train+i+'/'+j)
        resized_image = cv2.resize(img, (width, height))

        train_x.append(resized_image)

        #for x,y in enumerate(labels):
        if i == 'cats':
            train_y.append([0,1])
        else:
            train_y.append([1,0])

x_data = np.array(train_x)
y_data = np.array(train_y)

model = tf.keras.Sequential([
    layers.Conv2D(32, 3,3, input_shape=(width, height, 3)),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Conv2D(32, 3,3),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Conv2D(64, 3,3),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Flatten(),
    layers.Dense(64),
    layers.Activation('relu'),
    layers.Dropout(0.5),
    layers.Dense(2),
    layers.Activation('sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 100

model.fit(x_data, y_data, epochs = epochs)

models.save_model(model, 'mimodelo.keras')
'''


model = models.load_model('mimodelo.keras')


my_image = cv2.imread('cats_and_dogs/test/27.jpg')
my_image = cv2.resize(my_image, (width, height))

result = model.predict(np.array([my_image]))[0]
print(result)

print(max(result))
if result.argmax()==0:
    print("perro")
else:
    print("gato")

porcentaje = max(result)*100
print(porcentaje)
