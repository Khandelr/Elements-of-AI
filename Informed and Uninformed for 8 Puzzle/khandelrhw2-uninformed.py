
import sys
import time
#-------------Make Node---------------------------------------  
"""This method accepts state, parent , depth and pathcost as parameters
   It creates a node and returns it. 
"""

def makeNode(state, parent, depth, pathCost):
    return [state, parent, depth, pathCost]
#-------------End of Make Node--------------------------------

#-------------Test Procedure----------------------------------
"""This method accepts a state and checks whether the state is the goal state.
   If it is the goal state returns true oe else return false.
"""

def testProcedure(currentList):
    if currentList[0]==goalState:
        return True;
    return False;
#-------------End of Test Procedure---------------------------

#-------------Make State--------------------------------------
"""This method accepts nw,n,ne,w,c,e,sw,s,se and returns the state.
"""

def makeState(nw,n,ne,w,c,e,sw,s,se):
    return [nw,n,ne,w,c,e,sw,s,se];
#-------------End of Make State-------------------------------

#-------------Exapand Procedure-------------------------------
"""This method accepts the first node and the remaining nodes as an list.
   There is a variable tracklist which keeps  a track of the visited state. This ensures we dont visit the same state twice.
   For a given state, maximum a blank can be moved in four directions to generate four different states.
   The four states are checked to see if they are present in the trackList.
   If not then the respective states are appended to the list for BFS and inserted at the start for DFS.
   This list is then returned. 
"""

def expandProcedure(firstElementQueue, otherQueue):
    index = firstElementQueue[0].index("blank")
    varCount=0
    listOne=list(firstElementQueue[0])
    
    if firstElementQueue[0] in trackList:
        return otherQueue        

    trackList.append(firstElementQueue[0])
    

    if index -1>=0 and ((abs((index%3)-((index-1)%3))==1)):
        listOne[index],listOne[index-1]=listOne[index-1],listOne[index]
        depth=firstElementQueue[2]
        if listOne not in trackList:
            if varSearch==1:    
                otherQueue.append(makeNode(listOne,firstElementQueue,depth+1,firstElementQueue[3]))
            else :
                otherQueue.insert(varCount,makeNode(listOne,firstElementQueue,depth+1,firstElementQueue[3]))
                varCount=varCount+1
    
    listFour=list(firstElementQueue[0])
    if index +3<9:
        listFour[index],listFour[index+3]=listFour[index+3],listFour[index]
        depth=firstElementQueue[2]
        if listFour not in trackList:
            if varSearch==1:   
                otherQueue.append(makeNode(listFour,firstElementQueue,depth+1,firstElementQueue[3]))
            else :
                otherQueue.insert(varCount,makeNode(listFour,firstElementQueue,depth+1,firstElementQueue[3]))
                varCount=varCount+1
    
    listTwo=list(firstElementQueue[0])
    if index +1<9 and ((abs((index%3)-((index+1)%3))==1)):
        listTwo[index],listTwo[index+1]=listTwo[index+1],listTwo[index]
        depth=firstElementQueue[2]
        if listTwo not in trackList:
            if varSearch==1:
                otherQueue.append(makeNode(listTwo,firstElementQueue,depth+1,firstElementQueue[3]))
            else :
                otherQueue.insert(varCount,makeNode(listTwo,firstElementQueue,depth+1,firstElementQueue[3]))
                varCount=varCount+1            

    listThree=list(firstElementQueue[0])
    if index -3>=0:
        listThree[index],listThree[index-3]=listThree[index-3],listThree[index]
        depth=firstElementQueue[2]
        if listThree not in trackList:
            if varSearch==1:
                otherQueue.append(makeNode(listThree,firstElementQueue,depth+1,firstElementQueue[3]))
            else:
                otherQueue.insert(varCount,makeNode(listThree,firstElementQueue,depth+1,firstElementQueue[3]))
                varCount=varCount+1
        
    

    
    return otherQueue
#-------------End of Expand Procedure-------------------------


#-------------Output Procedure--------------------------------
"""This method accepts num runs and the node as a parameter.
   This node has a state which equals the goal state.
   This is then traversed to generate a list to reach the parent state from the goal state.
   This is then taversed in reverse order and the state is printed in the matrix form. 

"""

def outputProcedure(numRuns, firstElementQueue):
    path=[firstElementQueue[0]]
    parent=firstElementQueue[1]

    while parent !=None:
        path.append(parent[0])
        parent =parent[1]

    path.reverse()
    for i in range(len(path)):
        print path[i]
        for j in range(len(path[i])):
            if path[i][j]!="blank":
                print path[i][j] ,
            else :
                print "B",
            if (j%3)<2:
                 print "|" ,
            if (j%3)==2:
                 print 
    
    print "Goal or Final state reached in steps: ", numRuns
    print "Depth :", firstElementQueue[2]
    print "Total Time : ",round(time.time()-timestarted,3)

#-------------End Output Procedure----------------------------


#---------General Search--------------------------------------
"""This method accepts queue, limit and numruns as parameters.
   The limit is the recursion limit.
   The queue contains the nodes.
   This method is called recursively to check if the goal state is reached or if the queue is empty
   or if the recursion limit is reached.
"""

def generalSearch(queue, limit, numRuns):
    if queue == []:
        return False
    elif testProcedure(queue[0]):
        outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print "Limit reached"
    else:
        limit -= 1
        numRuns += 1
        #print len(trackList)
        generalSearch(expandProcedure(queue[0], queue[1:len(queue)]), limit, numRuns)
		
#---------End General Search---------------------------------


#---------Test BFS-------------------------------------------
"""This method accepts initial state, goal state and limit as arguments.
   This method is for BFS. 
"""
def testBFS(init,goal, limit):
    queue=[makeNode(init,None,0,0)]
    queue1=[]
    global trackList
    queue1=expandProcedure(queue[0],queue1)
    generalSearch(queue1,limit,0)
    
#---------End Test BFS---------------------------------------------------

#---------Test DFS-------------------------------------------------------
"""This method accepts initial state, goal state and limit as arguments.
   This method is for DFS. 
"""

def testDFS(init,goal, limit):
    queue=[makeNode(init,None,0,0)]
    queue1=[]
    global trackList
    queue1=expandProcedure(queue[0],queue1)
    generalSearch(queue1,limit,0)
#---------End Test DFS---------------------------------------------------

goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, "blank")
sys.setrecursionlimit(10000)

trackList=[]
# First group of test cases - should have solutions with depth <= 5
initialState1 = makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
initialState2 = makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)
initialState3 = makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
initialState4 = makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
initialState5 = makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)


# Second group of test cases - should have solutions with depth <= 10
initialState6 = makeState(2, 8, 3, 1, "blank", 5, 4, 7, 6)
initialState7 = makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
initialState8 = makeState("blank", 2, 3, 1, 5, 6, 4, 7, 8)
initialState9 = makeState(1, 3, "blank", 4, 2, 6, 7, 5, 8)
initialState10 = makeState(1, 3, "blank", 4, 2, 5, 7, 8, 6)


# Third group of test cases - should have solutions with depth <= 20
initialState11 = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
initialState12 = makeState(5, 1, 3, 2, "blank", 6, 4, 7, 8)
initialState13 = makeState(2, 3, 8, 1, 6, 5, 4, 7, "blank")
initialState14 = makeState(1, 2, 3, 5, "blank", 6, 4, 7, 8)
initialState15 = makeState("blank", 3, 6, 2, 1, 5, 4, 7, 8)


# Fourth group of test cases - should have solutions with depth <= 50
initialState16 = makeState(2, 6, 5, 4, "blank", 3, 7, 1, 8)
initialState17 = makeState(3, 6, "blank", 5, 7, 8, 2, 1, 4)
initialState18 = makeState(1, 5, "blank", 2, 3, 8, 4, 6, 7)
initialState19 = makeState(2, 5, 3, 4, "blank", 8, 6, 1, 7)
initialState20 = makeState(3, 8, 5, 1, 6, 7, 4, 2, "blank")



print "Enter"
print "1: BFS"
print "2: DFS"
varSearch=input()
timestarted=time.time()
if varSearch==1:
    testBFS(initialState6,goalState,100000)
else:
    testDFS(initialState5,goalState,100000)
