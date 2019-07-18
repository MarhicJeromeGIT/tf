from __future__ import absolute_import, division, print_function, unicode_literals

import os

!pip install -q tensorflow==2.0.0-alpha0
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

tf.__version__


model = models.Sequential()
model.add(layers.Convolution2D(64, 3, 3,
                        input_shape=(3, 32, 32)))
model.output_shape

model.add(layers.Flatten())
