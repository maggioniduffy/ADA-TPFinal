from random import random
import sys
import time

n = int(sys.argv[1])
 
def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[n * x + y] == -1):
        return True
    return False
 
 
def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[n * i + j], end=' ')
        print()
 
 
def solveKT(n):
    board = [-1 for i in range(n*n)]
    move_x = [2, 1, 2, 1, -1, -1, -2, -2]
    move_y = [-1, -2, 1, 2, -2, 2, 1, -1]
 
    random_x = round(random() * (n-1))
    random_y = round(random() * (n-1))
    # random_x = 0
    # random_y = 0
    print(random_x,random_y)
    board[random_x * n + random_y] = "00"
 
    pos = 1
 
    ts = time.time()
    if(not solveKTUtil(n, board, random_x, random_y, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        tf = time.time()
        tt = tf * 1000 - ts * 1000
        print("Time: ", tt)
        printSolution(n, board)
 
 
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == n**2):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            pos_aux = str(pos)
            if (pos <= 9):
              pos_aux = "0" + pos_aux
            board[n * new_x + new_y] = pos_aux
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
 
            board[n * new_x + new_y] = -1
    return False

if __name__ == "__main__":
    solveKT(n)