from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow
!pip install -q tensorflow==2.0.0-alpha0

import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
