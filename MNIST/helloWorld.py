#hello world for Tensorflow

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(55)
b = tf.constant(90)
print(sess.run(a+b))
