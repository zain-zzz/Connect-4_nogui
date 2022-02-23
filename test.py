import numpy as np
from random import randint
#Board
board = np.zeros((6,7))
#Functions
def check(col,player):
    x = 0
    while x != -8:
        x -= 1
        if board[x][col] == 0:
            if player == 1:
                board[x][col] = "1"
                x = -8
            if player == 2:
                board[x][col] = "2"
                x = -8
def checkW(player):
    #horizontal
    score = 0
    for y in range (0, 6):
        for x in range (0, 7):
            if board[y][x] == player:
                score += 1
                if score == 4:
                    print("Player ", player , "wins!")
                    global game_over
                    game_over = True
            else:
                score = 0
        score = 0
    #vertical
    score = 0
    for x in range(0, 7):
        for y in range(1, 7):
            if board[-y][x] == player:
                score += 1
                if score == 4:
                    print("Player ", player, "wins!")
                    game_over = True
            else:
                score = 0
        score = 0
    #diagonal
    score = 0
    for x in range(0, 4):
        if board[2+x][0+x] == player:
            score += 1
            if score == 4:
                print("Player ", player, "wins!")
                game_over = True
        else:
            score = 0
    for x in range(0, 5):
        if board[1+x][0+x] == player:
            score += 1
            if score == 4:
                print("Player ", player, "wins!")
                game_over = True
        else:
            score = 0
    for x in range(0, 6):
        if board[0+x][0+x] == player:
            score += 1
            if score == 4:
                print("Player ", player, "wins!")
                game_over = True
        else:
            score = 0
#Variables
singleplayer = False
game_over = False
player = 1
#Game
print("Its just connect 4 nothing special")
question = input("Do you want to face an AI (Y/N)")
if question == 'yes' or question == 'Yes' or question == 'y' or question == 'Y':
    singleplayer = True
if singleplayer == True:
    while not game_over:
        turn = 0
        #Player 1 turn
        if player == 1:
            col = int(input("Player 1 choose your row (1-7)"))
            col -= 1
        #'AI' turn
        if player == 2:
            if turn == 0:
                col = randint(0,6)
            else:
                move = randint(0,1)
                if move == 0 and col != 0:
                    col -=1
                elif move == 0 and col !=6:
                    col +=1
                else:
                    col -=1
        check(col,player)
        if player == 2:
            print(board)
        checkW(player)
        player = player % 2
        player += 1
        turn = 1

else:
    while not game_over:
        #Player 1 turn
        if player == 1:
            col = int(input("Player 1 choose your row (1-7)"))
            col -= 1
        #Player 2 turn
        if player == 2:
            col = int(input("Player 2 choose your row (1-7)"))
            col -= 1
        check(col,player)
        print(board)
        checkW(player)
        player = player % 2
        player += 1
