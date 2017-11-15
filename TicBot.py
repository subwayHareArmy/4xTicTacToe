import time
import numpy as np
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
Qtable = np.load('Qtable.npy')
Qtable = Qtable.tolist()

def index_2d(myList, v):
    for i in range(len(myList)):
        if np.array_equal(myList[i][0],v):
            return i
      
def RandomState():
    while(1):
        z1 = np.random.randint(3,size = (4,4), dtype=np.int32)
        if np.count_nonzero(z1)%2==0:
            if np.count_nonzero(z1 == 1)==np.count_nonzero(z1 == 2):
                if not(TermStateCheck(z1)):
                    break
    return z1
    
def TakeAction(state,playernum):
    action = np.zeros([4,4],dtype=np.int32)
    while(1):
        i = np.random.randint(0,3)
        j = np.random.randint(0,3)
        if state[i][j]==0:
            action[i][j] = playernum
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
    state_array = np.asanyarray(state)
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
    whoWonFlag = 2
    temp = []
    while not(TermStateCheck(state)):
        temp.append(state)
        action = TakeAction(state,1)
        temp.append(action)
        temp.append(0)
        state = np.add(state,action)
        if TermStateCheck(state):
              whoWonFlag = 1
              break
        temp.append(state)
        action = TakeAction(state,2)
        temp.append(action)
        temp.append(0)
        state = np.add(state,action)
    length = len(temp)
    reward1 = 1
    reward2 = -1
    i = length-1
    temp[i] = reward1
    if whoWonFlag == 2:
       temp[i-3] = reward2   
    return temp
            

def QtableUpdate(table,wstate):
    buffer = QvalueReward(wstate)
    l=0
    m=1
    n=2
    while(n<len(buffer)):
        s1=buffer[l]
        a1=buffer[m]
        r1=buffer[n]
        s2 = np.add(s1,a1)
        maxele = 0
        s1present = False
        s2present = False
        for checker in range(len(table)):
            if(np.array_equal(table[checker][0],s1)):
                s1present = True
            if(np.array_equal(table[checker][0],s2)):
                s2present = True
        if(s1present):
            if(s2present):
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ]+= r1 + 0.9*maxele-table[row1][col1]
            if(not(s2present)):
                table.append([])
                table[len(table)-1].append(s2)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ]+= r1 + 0.9*maxele-table[row1][col1]
        if(not(s1present)):
            if(s2present):
                table.append([])
                table[len(table)-1].append(s1)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ]+= r1 + 0.9*maxele-table[row1][col1]      
            if(not(s2present)):
                table.append([])
                table[len(table)-1].append(s1)
                for i in range(16):
                    table[len(table)-1].append(0)
                table.append([])
                table[len(table)-1].append(s2)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(a1)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ]+= r1 + 0.9*maxele-table[row1][col1]           
        l+=3
        m==3
        n+=3


def getActionNumber(action):
    actionp = action
    for i in range(len(Action1)):
        if np.array_equal(Action1[i],actionp) or np.array_equal(Action2[i],actionp):
            number = i+1
            break
    return number
start = time.time()
for i in range(0):
    working_state = RandomState()
    QtableUpdate(Qtable,working_state)
print(len(Qtable))
print(time.time()-start)
np.save('Qtable.npy',Qtable)