#advanced MNIST tutorial
#https://www.tensorflow.org/get_started/mnist/pros
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

import tensorflow as tf
sess = tf.InteractiveSession()