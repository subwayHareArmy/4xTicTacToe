import numpy as np
import time
Qtable = []
###################################################################################################################################################
def index_2d(myList, v):
    for i in range(len(myList)):
        if np.array_equal(myList[i][0],v):
            return i
def getActionNumber(action):
    row,col = action.nonzero()
    return row[0]*4 + col[0] + 1

###################################################################################################################################################
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
    state_array = np.asanyarray(state)
    x1 = np.empty((3,3), dtype = np.int32)
    for i in range(3):
        for j in range(3):      
            x1[i][j] = state_array[i][j]
    if win3(x1,1) or win3(x1,2):
        return True        
    for i in range(3):      
        for j in range(1,4):
            x1[i][j-1] = state_array[i][j]
    if win3(x1,1) or win3(x1,2):
        return True       
    for i in range(1,4):
        for j in range(1,4):
            x1[i-1][j-1] = state_array[i][j]  
    if win3(x1,1) or win3(x1,2):
         return True        
    for i in range(1,4):  
         for j in range(3):
            x1[i-1][j] = state_array[i][j]
    if win3(x1,1) or win3(x1,2):
         return True 
    if(np.count_nonzero(state_array)==16):
        return True        
    return False
###################################################################################################################################################
def RemoveAction(state):
    action = np.zeros([4,4],dtype=np.int32)
    while(1):
        i = np.random.randint(0,4)
        j = np.random.randint(0,4)
        if state[i][j]==1:
            action[i][j] = 1
            break
    return action
###################################################################################################################################################

def TermState(num):
    while(1):
        z1 = np.random.randint(3,size = (4,4), dtype=np.int32)
        if np.count_nonzero(z1)==num and np.count_nonzero(z1 == 1)==np.count_nonzero(z1 == 2)+1 and TermStateCheck(z1):
            break
    return z1


def QtableUpdate(table,tstate):
    gam = 1
    for i in range(int((np.count_nonzero(tstate)+1)/2)):
        tstatepresent = False
        action = RemoveAction(tstate)
        tstate = np.subtract(tstate,action)
        if TermStateCheck(tstate):
            break
        for checker in range(len(table)):
            if(np.array_equal(table[checker][0],tstate)):
                tstatepresent = True
        if(tstatepresent):
            row1 = index_2d(table,tstate)
            col1 = getActionNumber(action)
            if gam > table[row1][col1]:
                table[row1][col1] = gam
        else:
            table.append([])
            table[len(table)-1].append(tstate)
            for i in range(16):
                table[len(table)-1].append(0)
            row1 = index_2d(table,tstate)
            col1 = getActionNumber(action)
            table[row1][col1] = gam
        gam*=0.9

# what to do about 2 moves thing discuss with yem    
start = time.time()
for i in range(10):
    QtableUpdate(Qtable,TermState(7))
print(time.time()-start)
print(Qtable)      
########################################################################################################################################################

    
