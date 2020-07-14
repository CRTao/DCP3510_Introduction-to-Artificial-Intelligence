import random
import STcpClient

'''
    輪到此程式移動棋子
    board : 棋盤狀態(list of list), board[i][j] = i row, j column 棋盤狀態(i, j 從 0 開始)
            0 = 空、1 = 黑、2 = 白
    is_black : True 表示本程式是黑子、False 表示為白子

    return step
    step : list of list, step = [(r1, c1), (r2, c2) ...]
            r1, c1 表示要移動的棋子座標 (row, column) (zero-base)
            ri, ci (i>1) 表示該棋子移動路徑
'''
def GetStep(board, is_black):
    blackpos = []
    whitepos = []
    if(is_black):
        #get black now
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    blackcheck = (i,j)
                    blackpos.append(blackcheck)
        
        # check jump
        step = blackjump(blackpos)
        if len(step) == 0:
            ismove = 0
            c = 0
            while ismove == 0:
                c += 1
                move = random.randint(0, len(blackpos)-1)  
                if blackpos[move][1]+1<=7:
                    if board[blackpos[move][0]][blackpos[move][1]+1] == 0: 
                        if blackpos[move][1]+2<=7 :
                            if board[blackpos[move][0]][blackpos[move][1]+2] != 2: 
                                if blackpos[move][0]+1<= 7 and blackpos[move][1]+1<= 7:
                                        if board[blackpos[move][0]+1][blackpos[move][1]+1] != 2 :
                                            if blackpos[move][0]+1>=0 and blackpos[move][1]-1>=0:
                                                    if board[blackpos[move][0]+1][blackpos[move][1]-1] != 2: 
                                                        step = [blackpos[move], (blackpos[move][0],blackpos[move][1]+1)] 
                                                        ismove = 1
                if c>=20:
                    if blackpos[move][1]+1<=7 and board[blackpos[move][0]][blackpos[move][1]+1] == 0:
                        step = [blackpos[move], (blackpos[move][0],blackpos[move][1]+1)]
                        ismove = 1
                    else:
                        continue
                    
    elif is_black==0:
        #get white now
        for i in range(8):
            for j in range(8):
                if board[i][j] == 2:
                    whitecheck = (i,j)
                    whitepos.append(whitecheck)
        
        # check jump
        step = whitejump(whitepos)
        if len(step) == 0:
            ismove = 0
            c = 0
            while ismove == 0:
                c += 1
                move = random.randint(0, len(whitepos)-1)  
                if whitepos[move][1]-1>=0:
                    if board[whitepos[move][0]][whitepos[move][1]-1] == 0: 
                        if whitepos[move][1]-2>=0 :
                            if board[whitepos[move][0]][whitepos[move][1]-2] != 1: 
                                if whitepos[move][0]-1>= 0 and whitepos[move][1]-1>= 0:
                                        if board[whitepos[move][0]-1][whitepos[move][1]-1] != 1 :
                                            if whitepos[move][0]-1>=0 and whitepos[move][1]+1<=7:
                                                    if board[whitepos[move][0]-1][whitepos[move][1]+1] != 1: 
                                                        step = [whitepos[move], (whitepos[move][0],whitepos[move][1]-1)] 
                                                        ismove = 1
                if c>=20:
                    if whitepos[move][1]-1>=0 and board[whitepos[move][0]][whitepos[move][1]-1] == 0:
                        step = [whitepos[move], (whitepos[move][0],whitepos[move][1]-1)]
                        ismove = 1
                    else:
                        continue        
    else:
        pass
    
    
    return step

def blackjump(mycolor):
    step = []
    for i in mycolor:
        up = (i[0]-1,i[1])
        down = (i[0]+1,i[1])
        right = (i[0],i[1]+1)
        left = (i[0],i[1]-1)
        #if white is nearby and dest is empty and in the board
        if up[0]-1 >= 0:
            if board[up[0]][up[1]] == 2 : # around is white
                    if board[up[0]-1][up[1]] == 0 : #dest is empty
                        step = [i,(i[0]-2,i[1])]
                        break
        if down[0]+1 <= 7:
            if board[down[0]][down[1]] == 2 :
                    if board[down[0]+1][down[1]] == 0 :
                        step = [i,(i[0]+2,i[1])]
                        break
        if right[1]+1 <= 7:
            if board[right[0]][right[1]] == 2 :
                    if board[right[0]][right[1]+1] == 0 :
                        step = [i, (i[0],i[1]+2)]
                        break
        if left[1]-0 >= 0:
            if board[left[0]][left[1]] == 2 :
                    if board[left[0]][left[1]-1] == 0 :
                        step = [i, (i[0],i[1]-2)]
                        break
        else : 
            step = []        
            
    return step
    
def whitejump(mycolor):
    step = []
    for i in mycolor:
        up = (i[0]-1,i[1])
        down = (i[0]+1,i[1])
        right = (i[0],i[1]+1)
        left = (i[0],i[1]-1)
        #if white is nearby and dest is empty and in the board
        if up[0]-1 >= 0:
            if board[up[0]][up[1]] == 1 : # around is black
                    if board[up[0]-1][up[1]] == 0 : #dest is empty
                        step = [i,(i[0]-2,i[1])]
                        break
        if down[0]+1 <= 7:
            if board[down[0]][down[1]] == 1 :
                    if board[down[0]+1][down[1]] == 0 :
                        step = [i,(i[0]+2,i[1])]
                        break
        if right[1]+1 <= 7:
            if board[right[0]][right[1]] == 1 :
                    if board[right[0]][right[1]+1] == 0 :
                        step = [i, (i[0],i[1]+2)]
                        break
        if left[1]-0 >= 0:
            if board[left[0]][left[1]] == 1 :
                    if board[left[0]][left[1]-1] == 0 :
                        step = [i, (i[0],i[1]-2)]
                        break
        else : 
            step = []        
            
    return step
    
while(True):
    (stop_program, id_package, board, is_black) = STcpClient.GetBoard()
    if(stop_program):
        break
    
    listStep = GetStep(board, is_black)
    STcpClient.SendStep(id_package, listStep)
