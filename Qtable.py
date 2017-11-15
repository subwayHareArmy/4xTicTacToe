import numpy as np
import time
Qtable = []

def index_2d(myList, v):
    for i in range(len(myList)):
        if np.array_equal(myList[i][0],v):
            return i
      
def RandomState():
    while(1):
        z1 = np.random.randint(3,size = (4,4), dtype=np.int32)
        if np.count_nonzero(z1)%2==0 and np.count_nonzero(z1 == 1)==np.count_nonzero(z1 == 2) and not(TermStateCheck(z1)):
            break
    return z1
    
def TakeAction(state,playernum):
    action = np.zeros([4,4],dtype=np.int32)
    while(1):
        i = np.random.randint(0,4)
        j = np.random.randint(0,4)
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

def QtableUpdate(table,wstate):   
    s1 = np.asanyarray(wstate)
    playernum = 1
    action = TakeAction(wstate,playernum)
    s2 = np.add(wstate,action)  
    s1present = False
    s2present = False
    maxele = 0
    for checker in range(len(table)):
        if(np.array_equal(table[checker][0],s1)):
            s1present = True
        if(np.array_equal(table[checker][0],s2)):
            s2present = True
    if(s1present):
            if(s2present):
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(action)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ] = 0.9*maxele

            if(not(s2present) and not(TermStateCheck(s2))):
                table.append([])
                table[len(table)-1].append(s2)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(action,playernum)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ] =  0.9*maxele

            if(not(s2present) and TermStateCheck(s2)):
                row1 = index_2d(table,s1)
                col1 = getActionNumber(action,playernum)
                table[row1][col1 ] = 1
    
    if(not(s1present) and not(TermStateCheck(s1))):
        if(s2present):
                table.append([])
                table[len(table)-1].append(s1)
                for i in range(16):
                    table[len(table)-1].append(0)
                row1 = index_2d(table,s1)
                row2 = index_2d(table,s2)
                col1 = getActionNumber(action,playernum)
                for i in range (1,16):
                    if table[row2][i] > maxele:
                        maxele = table[row2][i]
                table[row1][col1 ]+= 0.9*maxele-table[row1][col1]
        if(not(s2present) and not(TermStateCheck(s2))):
            
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
            col1 = getActionNumber(action,playernum)
            for i in range (1,16):
                if table[row2][i] > maxele:
                    maxele = table[row2][i]
            table[row1][col1 ] = 0.9*maxele 


        if(not(s2present) and TermStateCheck(s2)):
             table.append([])
             table[len(table)-1].append(s1)
             for i in range(16):
                 table[len(table)-1].append(0)
             row1 = index_2d(table,s1)
             col1 = getActionNumber(action,playernum)
             table[row1][col1 ] = 1 


def getActionNumber(action,num):
    row,col = action.nonzero()
    return row[0]*4 + col[0] + 1


start = time.time()
for i in range(1000):
    QtableUpdate(Qtable,RandomState())
print(time.time()-start)