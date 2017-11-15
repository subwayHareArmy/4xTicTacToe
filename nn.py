# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:42:18 2017

@author: Parth
"""
import tensorflow as tf
session = tf.Session()
def new_weights(shape):
    return tf.Variable(tf.truncated_normal(shape,stddev = 0.5))
def new_biases(length):
    return tf.Variable(tf.constant(0.05,shape = [length]))

def new_fc_layer(inputs,num_inputs,num_outputs,use_relu=True):
    weights = new_weights(shape=[num_inputs,num_outputs])
    biases = new_biases(length = num_outputs)
    layer = tf.matmul(inputs,weights)+biases
    if use_relu:
        layer = tf.nn.relu(layer)
    return layer
x = tf.zeros([100,100])
y_true = tf.zeros([100,100])    
layer_fc1 = new_fc_layer(input = x,num_inputs = 16,num_outputs = 100)
layer_fc2 = new_fc_layer(input = layer_fc1,num_inputs = 100,num_outputs = 16,use_relu = False)

y_pred = tf.nn.softmax(layer_fc2)
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits = layer_fc2,labels = y_true)
loss = tf.reduce_mean(cross_entropy)
optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(loss)

total_iterations = 0

def optimize(num_iterations):
    global total_iterations

    for i in range(total_iterations,
                   total_iterations + num_iterations):
        x_batch, y_true_batch = 0,0
        feed_dict_train = {x: x_batch,
                           y_true: y_true_batch}
        session.run(optimizer, feed_dict=feed_dict_train)
        if i % 100 == 0:
            acc = session.run(accuracy, feed_dict=feed_dict_train)
            msg = "Optimization Iteration: {0:>6}, Training Accuracy: {1:>6.1%}"
            print(msg.format(i + 1, acc))
    total_iterations += num_iterations

session.close()