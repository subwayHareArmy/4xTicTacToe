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
tf.reset_default_graph()
sess = tf.Session()
working_state = tf.Variable(tf.random_uniform([4,4],0,3,dtype=tf.int32))  
Qtable = []
init = tf.global_variables_initializer()
sess.run(init)

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

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
    
def TakeAction(state,playernum):
    action = tf.Variable(tf.zeros([4,4],dtype=tf.int32))
    init_new_vars_op = tf.initialize_variables([action])
    sess.run(init_new_vars_op)
    z = np.zeros((4,4),dtype=np.int32)
    while(1):
        i = np.random.randint(0,3)
        j = np.random.randint(0,3)
        if(sess.run(state)[i][j]==0):
            z[i][j] = playernum
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
                 

    
def QvalueReward(state):
    temp = []
    while not(TermStateCheck(state)):
        temp.append(sess.run(state))
        action = TakeAction(state,1)
        temp.append(sess.run(action))
        temp.append(0)
        state = tf.add(state,action)
        temp.append(sess.run(state))
        action = TakeAction(state,2)
        temp.append(sess.run(action))
        temp.append(0)
        state = tf.add(state,action)
    length = len(temp)
    reward1 = 1
    reward2 = -1
    for i in range(length-1,0,-6):
        temp[i] = reward1
        temp[i-3] = reward2
        reward1*=0.9
        reward2*=0.9
    return temp
            
working_state = RandomState()

'''this part is for updating the Q table using the Q table algorithm, but I dont think its right. Just check what I've coded'''

def QtableUpdate(table,wstate):
    buffer = QvalueReward(wstate)
    i = 0
    j = 1
    r = 2
    while(r<len(buffer)):
        state = buffer[i]
        action = buffer[j]
        reward = buffer[r]
        if(any(state in subl for subl in table)):
            index = index_2d(table,state)
            row = index[0]
            for k in range(1,len(table[0])):
                if table[row][i] == action:
                    column = i
            state = tf.add(state,action)
        if(any(state in subl for subl in table)):
            index = index_2d(table,state)
            row1 = index[0]
        index = index_2d(table[row1],max( subl for subl in table[row1]))
        column1 = index[1]
        table[row][column]=table[row][column]+0.25*(reward+0.9*table[row1][column1]-table[row][column])
        i+=3
        j+=3
        r+=3
        
'''end of Q-LEARNING TABLE part'''


sess.close()
