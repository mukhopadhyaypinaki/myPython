#%tensorflow_version 2.x
import tensorflow as tf
# print(tf.version)

#t = tf.zeros([5, 5, 5, 5])
# print(t)


string = tf.Variable("This is a strings", tf.string)

number = tf.Variable(324, tf.int16)


rank1_tensor = tf.Variable(["Test"], tf.string)

rank2_tensor = tf.Variable([["Test", "ok"], ["Test", "ok"]], tf.string)

print(tf.rank(rank2_tensor))

print(tf.rank(rank1_tensor))


print(rank1_tensor.shape)
print(rank2_tensor.shape)


rank2_tensor = tf.Variable(
    [["Test", "ok", "1"], ["Test", "ok", "1"]], tf.string)


print(rank2_tensor.shape)

tensor1 = tf.ones([1, 2, 3])

print(tensor1)
print(tf.rank(tensor1))
#[[1,1,1],[1,1,1]]


tensor2 = tf.reshape(tensor1, [2, 3, 1])

print(tensor2)

print(tf.rank(tensor2))


import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 2.5, 3, 4]
y = [1, 4, 7, 9, 15]

plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20])

plt.show()
