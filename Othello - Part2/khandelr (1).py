
import sys
import gamePlay
from random import randint
from copy import deepcopy

"""
Weight assigned to each row and column for a matrix and based on this score is calculated
"""
weight=[	[500, -100, 80, 80, 80, 80, -100, 500],
			[-100, -200, -60, -60, -60, -60, -200, -100],
			[80, -60, 20, 20, 20, 20, -60, 80],
			[80, -60, 20, 0, 0, 20, -60, 80],
			[80, -60, 20, 0, 0, 20, -60, 80],
			[80, -60, 20, 20, 20, 20, -60, 80],
			[-100, -200,  -60, -60, -60, -60, -200, -100],
			[500, -100, 80, 80, 80, 80, -100, 500]	]

"""
A node is created which has a parent and a value alongwith the x and y coordinate 
"""

def makeNode(parent, value,x,y):
	return [parent, value,x,y]
"""
This method returns the possible moves for a board and color
"""

def getMoves(board, color):
	moves = []
	for i in range(8):
		for j in range(8):
			if gamePlay.valid(board, color, (i,j)):
				moves.append((i,j))

	return moves

"""
This method calculates the value for a board based on the weight and coins for that particular color
"""

def valueBoard(board):
	value = 0
	myCoins = 0
	oppCoins= 0
	#print "myColor :",myColor
	#print "opponentColor :",opponentColor
	for row in range(8):
		for column in range(8):
			if board[row][column] == myColor:
				myCoins +=1
				value = value + weight[row][column]
			elif board[row][column] == opponentColor:
				oppCoins +=1
				value = value - weight[row][column]

	#print "valueBoard :",value
	#gamePlay.printBoard(board)
	return value+myCoins*50-oppCoins*50



# def tree(depth):
# 	if depth == 3:
# 		return randint(0,10)
# 	node = [tree(), tree(), depth+1]
# 	return node
"""
This method traverses the tree for a particular node. It also does alpha beta pruning when alpha>=beta.
It sets the alpha beta value depending on the depth of the tree.
"""

def traverseTree(parnt,board,color,depth):
	#print "color",color
	global alpha
	global beta
	global localalpha
	global flag
	moves=getMoves(board,color)

	if depth==globalDepth or len(moves) == 0:
		value=valueBoard(board)
		parnt[1]=value
		return

	#print "moves",moves
	#if len(moves) == 0:
	#	return

	#iCounter=0
	for move in moves:
		#print "iCounter :",iCounter
		flag= True
		node =makeNode(parnt,None,move[0],move[1])
		#print "a"
		newBoard = deepcopy(board)
		#print "b"
		gamePlay.doMove(newBoard,color,move)
		#print "c"
		#gamePlay.printBoard(newBoard)
		#print newBoard
		oppColor=gamePlay.opponent(color)
		traverseTree(node,newBoard,oppColor,depth+1)
		#if traverseTreeReturn=="depth" or traverseTreeReturn=="pass":
			#gamePlay.printBoard(newBoard)
			#value=valueBoard(newBoard)
			#print "value",node[0][1]
		if node[0][1]==None:
			node[0][1]=node[1]
			if depth%2==0:
				localalpha=node[1]
			if depth%2==1:
				beta=node[1]
		elif node[0][1]<=node[1] and depth%2==0:
			node[0][1]=node[1]
			if localalpha!=None and localalpha<node[1]:
				localalpha=node[1]
		elif node[0][1]>=node[1] and depth%2==1:
			node[0][1]=node[1]
			if beta!=None and beta >node[1]:
					beta=node[1]

		if alpha !=None and beta !=None:
			if alpha>=beta and flag ==True:
				flag=False
				break
		if localalpha!=None and beta !=None:
			if localalpha>=beta and flag==True:
				flag=False
				break


	return
"""
change the depth based on time
"""
def changeTime(time):
  global globalDepth
  if  time<=8:
	 globalDepth=2
  elif time<=64:
	 globalDepth=3
  else:
	 globalDepth=4
  return  

"""
Evaluation function:
change the weight of the two dimensional matrix based on the board 
"""
def changeWeight(board):
	global weight
	if board[0][0]==myColor:
		weight[0][1]=200
		weight[1][0]=200
		weight[1][1]=300
	if board[0][7]==myColor:
		weight[0][6]=200
		weight[1][7]=200
		weight[1][6]=300
	if board[7][0]==myColor:
		weight[7][1]=200
		weight[6][0]=200
		weight[6][1]=300
	if board[7][7]==myColor:
		weight[7][6]=200
		weight[6][7]=200
		weight[6][6]=300
	
	if board[2][0]==myColor:
		weight[2][1]=80
	if board[3][0]==myColor:
		weight[3][1]=80
	if board[4][0]==myColor:
		weight[4][1]=80
	if board[5][0]==myColor:
		weight[5][1]=80
	
	if board[0][2]==myColor:
		weight[1][2]=80
	if board[0][3]==myColor:
		weight[1][3]=80
	if board[0][4]==myColor:
		weight[1][4]=80
	if board[0][5]==myColor:
		weight[1][5]=80
	
	if board[2][7]==myColor:
		weight[2][6]=80
	if board[3][7]==myColor:
		weight[3][6]=80
	if board[4][7]==myColor:
		weight[4][6]=80
	if board[5][7]==myColor:
		weight[5][6]=80
	
	if board[7][2]==myColor:
		weight[6][2]=80
	if board[7][3]==myColor:
		weight[6][3]=80
	if board[7][4]==myColor:
		weight[6][4]=80
	if board[7][5]==myColor:
		weight[6][5]=80
	
	return	
"""
It calculates the next best possible move depending on the algorithm. It also sets the alpha value.
"""


def nextMove(board, color, time, reversed = False):
	global myColor
	global opponentColor
	global alpha
	global beta
	global localalpha
	opponentColor=gamePlay.opponent(color)
	myColor=color
	moves=getMoves(board,color)
	#print "moves  :",moves
	if len(moves) == 0:
	   return "pass"
	childNodes=[]
  	changeTime(time)
	changeWeight(board)
	bestMove=None
	bestValue=None
	#print "moves :",len(moves)

	for move in moves:

		parnt = makeNode(None,None,move[0],move[1])
		childNodes.append(parnt)
		newBoard = deepcopy(board)
		gamePlay.doMove(newBoard,color,move)
		#gamePlay.printBoard(newBoard)
		#gamePlay.printBoard(newBoard)
		oppColor=gamePlay.opponent(color)
		traverseTree(parnt,newBoard,oppColor,1)
		#print "aaaaaaa ",aaaa
		if bestMove==None:
			bestMove=move
			bestValue=parnt[1]
		elif bestValue<parnt[1]:
			bestMove=move
			bestValue=parnt[1]
		if alpha == None:
			alpha=beta
		if alpha<beta:
			alpha=beta
		beta=None
		localalpha=None

		#print parnt[1]
	#for n in childNodes:
	#	print "final value :",n[1]

	#print "bestValue ",bestValue
	#print "bestMove ",bestMove
	#iop=raw_input()
	return bestMove

"""
The globaldepth value is defined. Also the default value for alpha and beta is provided.
"""

myColor=None
opponentColor=None
globalDepth=5
alpha=None
beta=None
localalpha=None
flag=None
#board=gamePlay.newBoard()
#print nextMove(board,"B",0)



