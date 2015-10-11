'''
Created on Oct 5th 2013

@author: Shreya, Mukesh
'''

import time
from pydoc import deque
from heapq import heappush, heappop
goalState = []
dictionary={}

# Uninformed Search - BFS
def uninformedSearch(queue, limit, numRuns):

    # List to keep track of visited nodes
    visited = []

    # Get first list of states in queue
    path = deque([queue])

    # cloning path
    temp_path = [queue]

    # If no more states available then return false
    if queue == []:
        print "No Solution Exists"
        return
    elif testProcedure(queue[0]):
	# Check state is goal state and print output
        outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print "Limit reached"
        return

    q = deque(queue)

    while len(q) > 0:
	# Get first element in queue
        n = q.popleft()

        temp_path = path.popleft()
        if n not in visited:
	    # add node to visited nodes
            visited.append(n)
            limit -= 1
            numRuns += 1


            if queue == []:     # check for elements in queue
	        print "No Solution Exists"
                return
            elif testProcedure(n):      # check if reached goal state
	        outputProcedure(numRuns, temp_path)
                return
            elif limit == 0:
	        print "Limit reached"
                return

            successors = expandProcedure(n)     #find successors of current state
            for succ in successors:
                new_path = temp_path + [succ]
                path.append(new_path)

            q.extend(successors)      # Add successors in queue
    print "No Solution Exists"
    return


# Informed search - A*
def informedSearch(initialState, limit, numRuns):
    # List to keep track of visited nodes
    visited = []

    # path of the tree
    temp_path = [initialState[0]]

    # If empty state, return
    if initialState == []:
        print "No Solution Exists"
        return
    elif testProcedure(initialState[0]):
        # Check state is goal state and print output
        #temp_path.append(goalState)
        generateDictionary("".join(map(str,initialState[0]))+":"+"".join(map(str,goalState)),temp_path)
        return temp_path,numRuns
        #outputProcedure(numRuns, initialState[0])
    elif limit == 0:
        # If limit reached return
        print "Limit reached"
        return

    # calculate g(n),h(n) and f(n) for the root node
    g_n = 0
    h_n = heuristicFunction(initialState[0])
    f_n = g_n + h_n

    # implement a heap
    heap = []

    # push the root, path as well as its f(n) into the heap
    heappush(heap, (f_n, [initialState[0], temp_path]))

    while len(heap) > 0:
        # Pop node with highest f(n)
        (cost_unwanted, nodeList) = heappop(heap)

        # Glean state and path to state
        n = nodeList[0]
        temp_path = nodeList[1]

        if n not in visited:
            visited.append(n)   # Append state to visited state
            limit -= 1
            numRuns += 1
            if testProcedure(n):    # Test if goal state
                generateDictionary("".join(map(str,initialState[0]))+":"+"".join(map(str,goalState)),temp_path)
                #outputProcedure(numRuns, temp_path)
                return temp_path,numRuns
            elif limit == 0:    # Test if limit reached
                print "Limit reached"
                return

            successors = expandProcedure(n) # Generate successors
            for succ in successors:
                # Calculate f_n for the successor
                g_n = len(temp_path)-1
                h_n = heuristicFunction(succ)
                f_n = g_n + h_n;

                # Push f(n), successor and path to successor to the heap
                heappush(heap, (f_n, [succ, (temp_path + [succ])]))

    print "No Solution Exists"
    return
"""
This method is used to update the dictionary
"""
def generateDictionary(key,value):
    global dictionary
    dictionary.update({key:value})

"""
This method is the heuristic function
"""
def heuristicF(state1,state2):

    posTilesGoal = dict()
    posTilesState = dict()

    for i in range(0,len(goalState)):
        posTilesGoal[state1[i]] = i;
        posTilesState[state2[i]] = i;

    manhattenDst = 0

    for i in range(1,len(goalState)):
        if ((posTilesGoal[i] == 2 and posTilesState[i] == 3) or \
            (posTilesGoal[i] == 3 and posTilesState[i] == 2) or \
            (posTilesGoal[i] == 2 and posTilesState[i] == 6) or \
            (posTilesGoal[i] == 6 and posTilesState[i] == 2) or \
            (posTilesGoal[i] == 5 and posTilesState[i] == 6) or \
            (posTilesGoal[i] == 6 and posTilesState[i] == 5)) :
            posTilesGoal[i] += 6

        diff = abs(posTilesGoal[i]-posTilesState[i])

        manhattenDst += (diff/3) + (diff%3)
    return manhattenDst


def heuristicFunction(currentState):

    posTilesGoal = dict()
    posTilesState = dict()

    for i in range(0,len(goalState)):
        posTilesGoal[goalState[i]] = i;
        posTilesState[currentState[i]] = i;

        manhattenDst = 0

    for i in range(1,len(goalState)):
        if ((posTilesGoal[i] == 2 and posTilesState[i] == 3) or \
            (posTilesGoal[i] == 3 and posTilesState[i] == 2) or \
            (posTilesGoal[i] == 2 and posTilesState[i] == 6) or \
            (posTilesGoal[i] == 6 and posTilesState[i] == 2) or \
            (posTilesGoal[i] == 5 and posTilesState[i] == 6) or \
            (posTilesGoal[i] == 6 and posTilesState[i] == 5)) :
             posTilesGoal[i] += 6

        diff = abs(posTilesGoal[i]-posTilesState[i])

        manhattenDst += (diff/3) + (diff%3)
    return manhattenDst

def testProcedure(queue):
    if (queue == goalState):
        return True
    else:
        return False

def outputProcedure(numRuns, path):
    print "Total number of runs=", numRuns
    print "Path Cost=", len(path)-1

    idx = 0
    for i in path:

        print "Game State: ", idx
        idx += 1
        print (" " if i[0] == 0 else i[0]) , " " , (" " if i[1] == 0 else i[1]) , " " , (" " if i[2] == 0 else i[2])
        print (" " if i[3] == 0 else i[3]) , " " , (" " if i[4] == 0 else i[4]) , " " , (" " if i[5] == 0 else i[5])
        print (" " if i[6] == 0 else i[6]) , " " , (" " if i[7] == 0 else i[7]) , " " , (" " if i[8] == 0 else i[8]), "\n"


# Successor function
def expandProcedure(state):
    successors = []
    blankPos = 0
    adjacent = []
    # Get position of blank tile
    for i in range(len(state)):
        if state[i] == 0:
            blankPos = i

    # Check whether left edge tiles
    if (blankPos % 3 != 2):
        nextPos = blankPos + 1
        adjacent.append(nextPos)

    # Check whether right edge tiles
    if (blankPos % 3 != 0):
        prev = blankPos - 1
        adjacent.append(prev)

    # Check up tile
    if (blankPos > 2):
        up = blankPos - 3
        adjacent.append(up)

    # Check down tile
    if (blankPos < 6):
        down = blankPos + 3
        adjacent.append(down)

    succ = state
    for pos in adjacent:
        succ = list(state)

	# Swap tiles and make new state. Add to successor
        if pos >= 0 and pos <= 8:
            temp = succ[blankPos]
            succ[blankPos] = succ[pos]
            succ[pos] = temp
            successors.append(succ)
    return successors

# Create state from initial and goal state
def makeState(nw, n, ne, w, c, e, sw, s, se):
    statelist = [nw, n, ne, w, c, e, sw, s, se]
    for i in range(len(statelist)):
	# Replace blank with 0
        if statelist[i] == "blank":
            statelist[i] = 0
    return statelist
"""
This method generates the key which is used to store the key in dictionary
"""
def generateKey(initialState,goalState):
    temp=''
    for i in initialState:
        temp=temp+str(initialState[i])
    temp=temp+':'
    for i in goalState:
        temp=temp+str(goalState[i])

    return temp
"""
This method generates the dictionary based on the state.
"""

def testCaseBasedSearch(limit):
    global goalState
    initialState=makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
    goalState=makeState(1,2,3,4,5,6,7,8,'blank')
    pathlist,numRuns=informedSearch([initialState],limit,0)
    #print "pathlist ",pathlist
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)
    goalState=makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
    goalState=makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
    goalState=makeState(1, 2, 3, 4, 5, "blank", 6, 7, 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)
    goalState=makeState(1,2,3,4,5,6,7,8,'blank')
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
    goalState=makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)
    goalState=makeState(1, 2, 3, 4, 5, "blank", 6, 7, 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(2, 8, 3, 1, "blank", 5, 4, 7, 6)
    goalState=makeState(1, 2, 3, 4, 5, "blank", 6, 7, 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    initialState=makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
    goalState=makeState(1, 2, 3, 4, 5, "blank", 6, 7, 8)
    pathlist,numRuns=informedSearch([initialState],limit,0)
    generateDictionary(generateKey(initialState,goalState),pathlist)

    #initialState=makeState(4,7,2,1,'blank',3,5,6,8)
    #goalState=makeState(1,2,3,4,5,6,7,8,'blank')
    #pathlist=testInformedSearch(initialState,goalState,limit)
    #generateDictionary(generateKey(initialState,goalState),pathlist)
"""
This is used to test if it is in the dictionary if not genrates the similar initial state and goal state.
"""
def generateTestProblems(initialState):
    global dictionary
    global goalState
    min=99999
    xi=0
    siState=""
    giState=""
    pathList=[]
    if dictionary.has_key(generateKey(initialState,goalState)):
        p=dictionary[generateKey(initialState,goalState)]
        print "pppp", p
        outputProcedure(0,p)
    else:
        for i in dictionary:
            temp=i.split(":")
            xi=i
            initState=makeState(int(temp[0][0]),int(temp[0][1]),int(temp[0][2]),int(temp[0][3]),int(temp[0][4]),int(temp[0][5]),int(temp[0][6])
                      ,int(temp[0][7]),int(temp[0][8]))
            gState=makeState(int(temp[1][0]),int(temp[1][1]),int(temp[1][2]),int(temp[1][3]),int(temp[1][4]),int(temp[1][5]),int(temp[1][6])
                      ,int(temp[1][7]),int(temp[1][8]))
            initSimi=heuristicF(initialState,initState)
            goalSimi=heuristicF(goalState,gState)
            #print initSimi
            #print goalSimi
            if min>initSimi+goalSimi:
                min=initSimi+goalSimi
                siState=initState
                giState=gState

            #print siState
            #print giState
            #print min
            #print xi
        goalState=siState
        path1,numRuns1=testInformedSearch(initialState,siState,20000)
        goalState=makeState(1,2,3,4,5,6,7,8,0)
        path2,numRuns2=testInformedSearch(giState,goalState,20000)
        path3=dictionary["".join(map(str,siState))+":"+"".join(map(str,giState))]
        path1.pop(len(path1)-1)
        path2.pop(0)
        path=[]
        if len(path1)>0:
            path.extend(path1)
        if len(path3)>0:
            path.extend(path3)
        if len(path2)>0:
            path.extend(path2)
        outputProcedure(numRuns1+numRuns2,path)

def testInformedSearch(initialState, goalState, limit):
    print "\nHueristic: No of mispalced Tiles"
    t1 = time.time()
    temp,numruns=informedSearch ([initialState], limit, 0)
    print "Time taken for Informed Search(Misplaced Tiles): ", (time.time()-t1) ," Seconds"
    #print "\nHueristic: Manhatten Distance"
    #t2 = time.time()
    #informedSearch ([initialState], limit, 0)
    #print "Time taken for Informed Search(Manhatten Distance): ", (time.time()-t2) ," Seconds"
    return temp,numruns

def testUninformedSearch(initialState, goalState, limit):
    uninformedSearch ([initialState], limit, 0)

# Main()
if __name__ == "__main__":
    initialState = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
    goalState = makeState(1,2,3,4,5,6,7,8,"blank")
    print "hi"
    #goalState=makeState(1, 2, 3, 4, 5, "blank", 6, 7, 8)
    testCaseBasedSearch(20000)
    print "dictionary",dictionary
    t1 = time.time()
    generateTestProblems(makeState(5, 1, 3, 2, "blank", 6, 4, 7, 8))
    print "Time taken for Informed Search(Manhattan): ", (time.time()-t1) ," Seconds"

    # print "Uninformed Search"
    # t1 = time.time()
    # testUninformedSearch(initialState, goalState, 200000)
    # t2 = time.time()
    # print "Time taken for Uninformed Search: ", (t2-t1), " Seconds"
    #
    # print "\n\nInformed Search"
    # testInformedSearch(initialState, goalState, 200000)

