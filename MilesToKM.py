import tensorflow as tf
import numpy as np

#input data
input = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)

#output for model
output = np.array([1.6, 3.2, 4.8, 6.4, 8.0, 9.7, 11.3, 12.9, 14.5, 16.1], dtype=float)

#define model
model = tf.keras.models.Sequential()

#Layers for neural  network
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compile model
model.compile(loss='mean_squared_error', optimizer='adam')

#train model
model.fit(input, output, epochs=10000)

#predict with model with Miles input
predictions = model.predict([20])

#print predicted KM
print(predictions)