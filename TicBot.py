
import tensorflow as tf
import numpy as np
tf.reset_default_graph()
sess = tf.Session()
working_state = tf.Variable(tf.random_uniform([4,4],0,3,dtype=tf.int32))
Action1 = [[[1, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 1],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 1, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 1, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 1]]]
Action2 = [[[2, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 2, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 2, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 2],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [2, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 2],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [2, 0, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 2],
       [0, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [2, 0, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 2, 0, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 2, 0]],[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 2]]]  
Qtable = []
init = tf.global_variables_initializer()
sess.run(init)

def index_2d(myList, v):
    for i in range(len(myList)):
        if np.array_equal(myList[i][0],v):
            return i

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
        maxele = 0
        if(any(s1 in subl for subl in table)):
            if(any(s2 in subl for subl in table)):
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*maxele-table[row1][col1])
            if(not(any(s2 in subl for subl in table))):
                table.append([])
                table[len(table)-1].append(s2)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s1)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*maxele-table[row1][col1])
        if(not(any(s1 in subl for subl in table))):
            if(any(s2 in subl for subl in table)):
                table.append([])
                table[len(table)-1].append(s1)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s1)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*maxele-table[row1][col1])      
            if(not(any(s2 in subl for subl in table))):
                table.append([])
                table[len(table)-1].append(s1)
                for i in range(16):
                    table[len(table)-1].append(0)
                table.append([])
                table[len(table)-1].append(s2)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s1)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1] = table[row1][col1] + 0.25(r1 + 0.9*maxele-table[row1][col1])            
        i+=3
        j==3
        k+=3

def getActionNumber(action):
    actionp = action
    for i in range(len(Action1)):
        if np.array_equal(Action1[i],actionp) or np.array_equal(Action2[i],actionp):
            number = i+1
            break
    return number

QtableUpdate(Qtable,RandomState())
print(Qtable)      

sess.close()
