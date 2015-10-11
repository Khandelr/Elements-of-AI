import random
def print_board():
	for i in range(0,3):
		for j in range(0,3):
			print map[2-i][j],
			if j != 2:
				print "|",
		print ""


def check_done(turn):
	for i in range(0,3):
		if map[i][0] == map[i][1] == map[i][2] != " " \
		or map[0][i] == map[1][i] == map[2][i] != " ":
			if turn==user_turn:		
				print turn, "human won!!!"
			elif turn==computer_turn:
				print turn, "computer won!!!"
			return True
		
	if map[0][0] == map[1][1] == map[2][2] != " " \
	or map[0][2] == map[1][1] == map[2][0] != " ":
		if turn==user_turn:		
				print turn, "human won!!!"
		elif turn==computer_turn:
			print turn, "computer won!!!"
		return True

	if " " not in map[0] and " " not in map[1] and " " not in map[2]:
		print "Draw"
		return True
		

	return False


def next_attack_move():
	if (map[1][1]==computer_turn and map[2][2]==user_turn and map[0][0]==" "):
		map[0][0]=computer_turn
		return True
	if (map[1][1]==computer_turn and map[0][0]==user_turn and map[2][2]==" "):
		map[2][2]=computer_turn
		return True
	if map[1][1]==computer_turn and map[0][2]==user_turn and map[2][0]==" ":
		map[2][0]=computer_turn
		return True
	if map[1][1]==computer_turn and map[2][0]==user_turn and map[0][2]==" ":
		map[0][2]=computer_turn
		return True

	if map[0][0]==user_turn and map[2][2]==user_turn and map[1][1]==computer_turn:
		if map[1][2]==" ":
			map[1][2]=computer_turn
			return True
		elif map[1][0]==" ":
			map[1][0]=computer_turn
			return True
	if map[0][2]==user_turn and map[2][0]==user_turn and map[1][1]==computer_turn:
		if map[1][2]==" ":
			map[1][2]=computer_turn
			return True
		elif map[1][0]==" ":
			map[1][0]=computer_turn
			return True

	if ((map[0][0]==computer_turn and map[1][1]==" " and map[2][2]==" ") or (map[0][0]==" " and map[1][1]==computer_turn and map[2][2]==" ") or
			(map[0][0]==" " and map[1][1]==" " and map[2][2]==computer_turn)):
				if map[0][0]==" ":
					map[0][0]=computer_turn
					return True
				elif map[2][2]==" ":
					map[2][2]=computer_turn
					return True
				elif map[1][1]== " ":
					map[1][1]=computer_turn
					return True
	if ((map[0][2]==computer_turn and map[1][1]==" " and map[2][0]==" ") or (map[0][2]==" " and map[1][1]==computer_turn and map[2][0]==" ") or
			(map[0][2]==" " and map[1][1]==" " and map[2][0]==computer_turn)):
				if map[0][2]==" ":
					map[0][2]=computer_turn
					return True
				elif map[2][0]==" ":
					map[2][0]=computer_turn
					return True
				elif map[1][1]== " ":
					map[1][1]=computer_turn
					return True

	for i in range(0,3):
		if ((map[i][0]==computer_turn and map[i][1]==" " and map[i][2]==" ") or (map[i][0]==" " and map[i][1]==computer_turn and map[i][2]==" ") or
			(map[i][0]==" " and map[i][1]==" " and map[i][2]==computer_turn)):
				if map[i][0]==" ":
					map[i][0]=computer_turn
					return True
				elif map[i][2]==" ":
					map[i][2]=computer_turn
					return True
				elif map[i][1]== " ":
					map[i][1]=computer_turn
					return True

		elif ((map[0][i]==computer_turn and map[1][i]==" " and map[2][i]==" ") or (map[0][i]==" " and map[1][i]==computer_turn and map[2][i]==" ") or
			(map[0][i]==" " and map[1][i]==" " and map[2][i]==computer_turn)):
				if map[0][i]==" ":
					map[0][i]=computer_turn
					return True
				elif map[2][i]==" ":
					map[2][i]=computer_turn
					return True
				elif map[1][i]== " ":
					map[1][i]=computer_turn
					return True                          
	



def second_move():
	center_corner_flag=random.randrange(1,3)
	if map[1][1]==user_turn or (center_corner_flag==1 and count==0):
		random_number=random.randrange(1,5)
		if random_number==1:
			map[0][0]=computer_turn
		elif random_number==2:
			map[0][2]=computer_turn
		elif random_number==3:
			map[2][0]=computer_turn 
		else:
			map[2][2]=computer_turn
	else:
		map[1][1]=computer_turn    

def check_if_win():
				
	for i in range(0,3):
									
		if ((map[i][0]==computer_turn and map[i][1]==computer_turn) or (map[i][0]==computer_turn and map[i][2]==computer_turn) or
			(map[i][1]==computer_turn and map[i][2]==computer_turn)):
			if map[i][0]==" ":
				map[i][0]=computer_turn
				return 
			elif map[i][1]==" ":
				map[i][1]=computer_turn
				return
			elif map[i][2]==" ":
				map[i][2]=computer_turn
				return
		if ((map[0][i]==computer_turn and map[1][i]==computer_turn) or (map[0][i]==computer_turn and map[2][i]==computer_turn) or 
			(map[1][i]==computer_turn and map[2][i]==computer_turn)):
				if map[0][i]==" ":
					map[0][i]=computer_turn
					return
				elif map[1][i]==" " :
					map[1][i]=computer_turn
					return
				elif map[2][i]==" ":
					map[2][i]=computer_turn
					return

	if ((map[0][0]== computer_turn and map[1][1]==computer_turn) or (map[0][0]== computer_turn and map[2][2]==computer_turn) or 
			(map[1][1]== computer_turn and map[2][2]==computer_turn) ):
			if map[0][0]==" ":
				map[0][0]=computer_turn
				return
			elif map[1][1]==" ":
				map[1][1]=computer_turn
				return
			elif map[2][2]==" ":
				map[2][2]=computer_turn
				return
				
	if((map[0][2]== computer_turn and map[1][1]==computer_turn)or (map[0][2]== computer_turn and map[2][0]==computer_turn) or
		(map[1][1]== computer_turn and map[2][0]==computer_turn)):
			if map[0][2]==" ":
				map[0][2]=computer_turn
				return
			elif map[1][1]==" ":
				map[1][1]=computer_turn
				return
			elif map[2][0]==" ":
				map[2][0]=computer_turn
				return
						



def next_defense_move(turn1,turn2):
	if (count==1 and user_turn=="X") or count==0:
		second_move()
		return True
	else:
		for i in range(0,3):
			for j in range(0,3):
				if map[i][j]==turn1:
					#print "inside i j",i,j
					if ((i+1<3 and map[i+1][j]==turn1)or (i+2<3 and map[i+2][j]==turn1)):
						if map[i+1][j]==" ":
							map[i+1][j]=turn2
							return True
						elif i+2<3 and map[i+2][j]==" ":
							map[i+2][j]=turn2
							return True
						elif i>0 and map[i-1][j]==" ":
							map[i-1][j]=turn2
							return True
								
					if ((j+1<3 and map[i][j+1]==turn1)or (j+2<3 and map[i][j+2]==turn1)):
						if map[i][j+1]==" ":
							map[i][j+1]=turn2
							return True
						elif j+2 <3 and map[i][j+2]==" ":
							map[i][j+2]=turn2 
							return True
						elif j>0 and map[i][j-1]==" ":
							map[i][j-1]=turn2
							return True

		if ((map[0][0]== turn1 and map[1][1]==turn1) or (map[0][0]== turn1 and map[2][2]==turn1) or 
			(map[1][1]== turn1 and map[2][2]==turn1) ):
			if map[0][0]==" ":
				map[0][0]=turn2
				return True
			elif map[1][1]==" ":
				map[1][1]=turn2
				return True
			elif map[2][2]==" ":
				map[2][2]=turn2
				return True
				
		if((map[0][2]== turn1 and map[1][1]==turn1)or (map[0][2]== turn1 and map[2][0]==turn1) or
			(map[1][1]== turn1 and map[2][0]==turn1)):
			if map[0][2]==" ":
				map[0][2]=turn2
				return True
			elif map[1][1]==" ":
				map[1][1]=turn2
				return True
			elif map[2][0]==" ":
				map[2][0]=turn2
				return True

		if map[1][0]==turn1 and map[0][1]==turn1 and map[0][0]==" ":
			map[0][0]=turn2
			return True
		if map[0][1]==turn1 and map[1][2]==turn1 and map[0][2]==" ":
			map[0][2]=turn2
			return True
		if map[1][2]==turn1 and map[2][1]==turn1 and map[2][2]==" ":
			map[2][2]=turn2
			return True
		if map[1][0]==turn1 and map[2][1]==turn1 and map[2][0]==" ":
			map[2][0]=turn2
			return True


def next_draw_move():
	for i in range(0,3):
		for j in range(0,3):
			if map[i][j]==" ":
				map[i][j]=computer_turn
				return



def print_statement():
	print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
	print "7|8|9"
	print "4|5|6"
	print "1|2|3"
	print

def get_XY():
	global X
	global Y
	if pos<=9 and pos >=1:
		Y=pos/3
		X=pos%3
		if X!=0:
			X-=1
		else:
			X=2
			Y-=1


def computer_turn_init():
	global user_turn
	global computer_turn
	if user_turn == "X":
		computer_turn="O"
	else:
		computer_turn= "X"

		

turn = "X"
map = [[" "," "," "],
	   [" "," "," "],
	   [" "," "," "]]
done = False
count=0 
X=-1
Y=-1
user_turn=raw_input("User Select either X or O : ").upper()
while user_turn!="X" and user_turn!="O":
	print "Invalid Input"
	user_turn=raw_input("User Select either X or O : ").upper()


computer_turn=""
computer_turn_init()
print "computer_turn :", computer_turn
while done != True:
	print_board()
	
	print turn, "'s turn"
	print

	moved = False
	while moved != True:
		print_statement()
		try:
			if user_turn=="X":
				pos = input("Select: ")
				get_XY()        
				if map[Y][X] == " ":
					map[Y][X] = user_turn
					count+=1
					moved = True
					done = check_done(user_turn)

					if done == False:
						check_if_win()	
						done = check_done(computer_turn)
						print "done ",done
						if done == False:                    
						
							def_flag=next_defense_move(user_turn,computer_turn)
							print "def_flag 1 ",def_flag
							if def_flag!=True:
								def_flag=False	
							done = check_done(computer_turn)
							if done == False and def_flag==False:
								def_attack_flag=next_attack_move()
								print "def_attack_flag ",def_attack_flag
								if def_attack_flag!=True:
									def_attack_flag=False
								if def_attack_flag!=True:
									next_draw_move()
			else:
				check_if_win()
				done=check_done(computer_turn)
				if done==False:
					def_flag=next_defense_move(user_turn,computer_turn)
					print "def_flag ",def_flag
					if def_flag!=True:
						def_flag=False	
					if def_flag==False:
						def_attack_flag=next_attack_move()
						print "def_attack_flag ",def_attack_flag
						if def_attack_flag!=True:
							def_attack_flag=False
						if def_attack_flag!=True:
							next_draw_move()
				
					done = check_done(computer_turn)
					print_board()
				
					if done == False:
						pos = input("Select: ")
						get_XY()        
						if map[Y][X] == " ":
							map[Y][X] = user_turn
							count+=1
							moved = True
							done = check_done(user_turn)
	
				else:
					moved=True
			
			
		except:
			print "You need to add a numeric value"