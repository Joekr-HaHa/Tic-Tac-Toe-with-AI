                                    #Tic-Tac-Toe
import sys
import random
global game_end
game_end=False
board=[" "," "," "," "," "," "," "," "," "]
def draw_board(board):
    print(""," | ",board[0]," | ",board[1]," | ",board[2]," | ","\n",\
          " -------------------","\n",\
          " | ",board[3]," | ",board[4]," | ",board[5]," | ","\n",\
          " -------------------","\n",\
          " | ",board[6]," | ",board[7]," | ",board[8]," | ")
draw_board(board)
def board_update(board):
    print(board)
def boardFull(board):
    j=0
    for i in board:
        if i==' ':
            return False
        else:
            j+=1
    if j==len(board):
        return True
def player2(board):
    letter="X"
    p2inp=int(input("Where do you want to place your 'X'?"))
    p2inp-=1
    if board[p2inp]!=" ":
        print("Space already taken")
        player2(board)
    else:
        board[p2inp]=letter
def ai(board):
    poss=[x for x, letter in enumerate(board) if letter==' ']
    move=0
    if 4 in poss:
        move=4
        return move
    for let in ['O','X']:
        for l in poss:
            cop=board[:]#copy
            cop[l]=let
            if check_win(cop,let):
                move=l
                return move
    corners=[]
    for i in poss:
        if i in[0,2,6,8]:
            corners.append(i)
    if len(corners)>0:
        move=random.choice(corners)
        return move
    
            
def check_win(board,letter):
    if board[3]==letter and board[4]==letter and board[5]==letter: 
        return True
    elif board[0]==letter and board[1]==letter and board[2]==letter:
        return True
    elif board[6]==letter and board[7]==letter and board[8]==letter:
        return True
    elif board[0]==letter and board[3]==letter and board[6]==letter:
        return True
    elif board[1]==letter and board[4]==letter and board[7]==letter:
        return True
    elif board[2]==letter and board[5]==letter and board[8]==letter:
        return True
    elif board[0]==letter and board[4]==letter and board[8]==letter:
        return True
    elif board[2]==letter and board[4]==letter and board[6]==letter:
        return True
def random_corner(board,letter):
    pos=random.choice([0,2,6,8])
    if board[pos]==" ":
        print("Placed at",pos,"corner")
        board[pos]=letter
    elif board[pos]!=" ":
        random_corner(board,letter)
def random_place(board,letter):
    pos=random.randint(0,8)
    if board[pos]==" ":
        print("Placed at",pos)
        board[pos]=letter
    elif board[pos]!=" ":
        random_place(board,letter)
game_over=False
def main():
    global game_over
    print("Tic tac toe time!")
    while not (boardFull(board)):
        if not check_win(board,"O"):
            player2(board)
            draw_board(board)
        else:
            print("O wins")
            break

        if not check_win(board,"X"):
            move=ai(board)
            print(move)
            board[move]="O"
            print("AI Turn \n")
            board_update(board)
            draw_board(board)
        else:
            print("X Wins")
            break

        if boardFull(board):
            print("Draw")
            break
main()
