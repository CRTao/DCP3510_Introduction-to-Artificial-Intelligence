
# 
turn=1;
turn_SamePlayer=0;    # 0= select piece 1= first step 2~= jump step
board=[];
blacklist=[]
whitelist=[]
cansteplist=[]
movement=[]


def initial():
	global board
	board = [
	[ 1, 0, 0, 0, 0, 0, 0, 0],
	[ 0, 1, 0, 0, 0, 0, 0, 2],
	[ 1, 0, 1, 0, 0, 0, 2, 0],
	[ 0, 1, 0, 0, 0, 2, 0, 2],
	[ 1, 0, 1, 0, 0, 0, 2, 0],
	[ 0, 1, 0, 0, 0, 2, 0, 2],
	[ 1, 0, 0, 0, 0, 0, 2, 0],
	[ 0, 0, 0, 0, 0, 0, 0, 2]
	]

def find_blacklist():
	global board,blacklist
	blacklist=[]
	for row, list in enumerate(board):
		for col, num in enumerate(list):
			if num == 1:
				blacklist.append((row,col))
	return blacklist

def find_whitelist():
	global board,whitelist
	whitelist=[]
	for row, list in enumerate(board):
		for col, num in enumerate(list):
			if num == 2:
				whitelist.append((row,col))
	return whitelist

def printboard():
	global board
	print(' ')
	print('  Col  ' + '   '.join(map(str, range(8))))
	print('  Row ' + '   ')
	for idx, row in enumerate(board):
		print('   {:1} '.format(idx), end='')
		for val in row:
			if val ==1:
				print(" ◇ ", end='')
			elif val ==2:
				print(" ◆ ", end='')
			else:
				print("  - ", end='')
		print(" ")
	print(' ')

def canmove(movement):
	global board
	list=[]
	if board[movement[0]-1][movement[1]]==0 and movement[0]-1>=0:
		list.append(movement[0]-1,movement[1])
	if board[movement[0]+1][movement[1]]==0 and movement[0]+1<8:
		list.append(movement[0]+1,movement[1])
	if board[movement[0]][movement[1]-1]==0 and movement[1]-1>=0:
		list.append(movement[0],movement[1]-1)
	if board[movement[0]][movement[1]+1]==0 and movement[1]+1<8:
		list.append(movement[0],movement[1]+1)
	return list

def canjump(movement):
	global board
	list=[]
	if board[movement[0]-2][movement[1]]==0 and movement[0]-2>=0 and board[movement[0]-1][movement[1]]!=0:
		list.append(movement[0]-2,movement[1])
	if board[movement[0]+2][movement[1]]==0 and movement[0]+2<8  and board[movement[0]+1][movement[1]]!=0:
		list.append(movement[0]+2,movement[1])
	if board[movement[0]][movement[1]-2]==0 and movement[1]-2>=0 and board[movement[0]][movement[1]-1]!=0:
		list.append(movement[0],movement[1]-2)
	if board[movement[0]][movement[1]+2]==0 and movement[1]+2<8  and board[movement[0]][movement[1]+1]!=0:
		list.append(movement[0],movement[1]+2)
	return list

def available_step(movement):
	global board, blacklist, whitelist, turn, turn_SamePlayer, cansteplist
	cansteplist=[]
	if turn==1:
		if turn_SamePlayer==0:
			cansteplist=blacklist;
		elif turn_SamePlayer==1:
			am_step = canmove(movement)
			aj_step = canjump(movement)
			cansteplist = am_step + aj_step
		else :
			cansteplist = canjump(movement)
	else:
		if turn_SamePlayer==0:
			cansteplist=whitelist;
		elif turn_SamePlayer==1:
			am_step = canmove(movement)
			aj_step = canjump(movement)
			cansteplist = am_step + aj_step
		else :
			cansteplist = canjump(movement)
	return cansteplist

if __name__ == "__main__":
	initial()
	printboard()
	print(find_blacklist())
	print(find_whitelist())
	print('')
	
	
	print("Turn "+str(turn))
	turn_SamePlayer=0
	print("Available_step"+str(available_step(None)))
	movement = input("Newmove  ")
	movement = movement.replace('(', '')
	movement = movement.replace(')', '')
	movement = movement.replace(',', '')
	print(movement)
	turn_SamePlayer=1
	print("Available_step"+str(available_step(movement)))
