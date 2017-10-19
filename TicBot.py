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
    i = length-1
    temp[i] = reward1
    temp[i-3] = reward2
    return temp
            
working_state = RandomState()

''' possibilities:
    s1 exists s2 exists
    s1 exists s2 doesnt
    s1 doesnt exist s2 exists
    s1 doesnt exist s2 doest exist
    how to code this out???
   bruteforce the only way???'''

def QtableUpdate(table,wstate):
    buffer = QvalueReward(wstate)
    i=0
    j=1
    k=2
    while(k<len(buffer)):
        s1=buffer[i]
        a1=buffer[j]
        r1=buffer[k]
        s2 = tf.add(s1,a1)
        if(any(s1 in subl for subl in table)):
            if(any(s2 in subl for subl in table)):
                row1 = index_2d(table,s1)[0]
                row2 = index_2d(table,s1)[0]
                col1 = getActionNumber(a1)
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*max(table[row2][1])-table[row1][col1])
            if(not(any(s2 in subl for subl in table))):
                table.append(np.zeros(17,dtype=np.int32))
                table[len(table)-1][0]=s2
                row1 = index_2d(table,s1)[0]
                row2 = index_2d(table,s1)[0]
                col1 = getActionNumber(a1)
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*max(table[row2][1])-table[row1][col1])
        if(not(any(s1 in subl for subl in table))):
            if(any(s2 in subl for subl in table)):
                table.append(np.zeros(17,dtype=np.int32))
                table[len(table)-1][0]=s1
                row1 = index_2d(table,s1)[0]
                row2 = index_2d(table,s1)[0]
                col1 = getActionNumber(a1)
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*max(table[row2][1])-table[row1][col1])      
            if(not(any(s2 in subl for subl in table))):
                table.append(np.zeros(17,dtype=np.int32))
                table[len(table)-1][0]=s2
                table.append(np.zeros(17,dtype=np.int32))
                table[len(table)-1][0]=s1
                row1 = index_2d(table,s1)[0]
                row2 = index_2d(table,s1)[0]
                col1 = getActionNumber(a1)
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*max(table[row2][1])-table[row1][col1])            
        i+=3
        j==3
        k+=3

'''end of Q-LEARNING TABLE part'''

'''just to unify all the action columns, to easily make state-action pairs'''
def getActionNumber(action):
'''dude figure this out easy only, let it return 1 for some defined action, 2 for some other action and so on...
therefore it can return number from 1 to 16'''

sess.close()
