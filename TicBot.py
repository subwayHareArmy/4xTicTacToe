#############################################################################################
#Random State Generator DONE!

#TakeAction function DONE!!!!!!

#Q value calculator:
    #Take State 
    #Choose rendom action
    #Loop till terminal state
    #Provide end reward and backprop

#Q matrix update
    #if state exists, calculate q value and do q += qnew
    #if new state, add state to q matrix, calculate q value and do q = qnew
    #repeat for A LOT of iterations

#FCC net train

#convert to game (MAYBE?????)
#############################################################################################

import tensorflow as tf
import numpy as np
sess = tf.Session()
working_state = tf.Variable(tf.random_uniform([4,4],0,3,dtype=tf.int32))
init = tf.global_variables_initializer()
sess.run(init)

def tf_count(t, val):
    elements_equal_to_value = tf.equal(t, val)
    as_ints = tf.cast(elements_equal_to_value, tf.int32)
    count = tf.reduce_sum(as_ints)
    return count
      
def RandomState():
    z1 = tf.Variable(tf.random_uniform([4,4],0,3,dtype=tf.int32))
    init_new_vars_op = tf.initialize_variables([z1])
    sess.run(init_new_vars_op)
    assign_op = z1.assign(tf.random_uniform([4,4],0,3,dtype=tf.int32))
    while(1):
        sess.run(assign_op)
        if sess.run(tf.count_nonzero(z1))%2==0:
            if sess.run(tf_count(z1,1))==sess.run(tf_count(z1,2)):
                if not(TermStateCheck(z1)):
                    break
    return z1
    
def TakeAction(state):
    action = tf.Variable(tf.zeros([4,4],dtype=tf.int32))
    init_new_vars_op = tf.initialize_variables([action])
    sess.run(init_new_vars_op)
    z = np.zeros((4,4),dtype=np.int32)
    while(1):
        i = np.random.randint(0,3)
        j = np.random.randint(0,3)
        if(sess.run(state)[i][j]==0):
            z[i][j] = 1
            z_tf = tf.convert_to_tensor(z,dtype=tf.int32)
            action = tf.add(z_tf,action)
            break
    return action
   
def win3(x,t):
    if x[0][0] == t and x[0][1] == t and x[0][2] == t:
        return True
    if x[1][0] == t and x[1][1] == t and x[1][2] == t:
        return True
    if x[2][0] == t and x[2][1] == t and x[2][2] == t:
        return True
    if x[1][0] == t and x[2][0] == t and x[0][0] == t:
        return True
    if x[1][1] == t and x[2][1] == t and x[0][1] == t:
        return True
    if x[1][2] == t and x[2][2] == t and x[0][2] == t:
        return True
    if x[0][0] == t and x[1][1] == t and x[2][2] == t:
        return True
    if x[0][2] == t and x[1][1] == t and x[2][0] == t:
        return True
    return False
    
    
    
def TermStateCheck(state):
    state_array = np.asanyarray(sess.run(state))
    x1 = np.empty([3,3],dtype = np.int32)
    for i in range(3):
        for j in range(3):      
            x1[i][j] = state_array[i][j]
    if win3(x1,1):
        return True
    if win3(x1,2):
        return True
    for i in range(1,4):
        for j in range(1,4):
            x1[i-1][j-1] = state_array[i][j]
    if win3(x1,1):
        return True
    if win3(x1,2):
        return True
    for i in range(3):
        for j in range(1,4):
            x1[i][j-1] = state_array[i][j]
    if win3(x1,1):        
        return True
    if win3(x1,2):
        return True
    for i in range(1,4):
        for j in range(3):
            x1[i-1][j] = state_array[i][j]
    if win3(x1,1):
        return True
    if win3(x1,2):
        return True
    return False            

def Qvalue(state):
    temp = []
    z1 = sess.run(state)
    temp.append(z1)
    while not(TermStateCheck(z1)):
        
        
working_state = RandomState()
print(sess.run(working_state))    
Qvalue(working_state)
sess.close()
