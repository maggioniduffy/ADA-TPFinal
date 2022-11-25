import time
import sys
from plot import plot_errors, plot_times

def isSafe(x, y, n, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False
 
 
def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
 
 
def solveKT(n):
    board = [[-1 for i in range(n)]for i in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    board[0][0] = "00"
 
    pos = 1
  
    ti = time.time()
    tt = 0
    ok = True
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        tf = time.time()
        tt = tf-ti
        print("Solution does not exist")
    else:
        tf = time.time()
        tt = tf-ti
        ok = False
        printSolution(n, board)

    return tt, ok
 
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == n**2):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, n, board)):
            pos_aux = str(pos)
            if (pos <= 9):
              pos_aux = "0" + pos_aux
            board[new_x][new_y] = pos_aux
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
 
            board[new_x][new_y] = -1
    return False

n = 8
if (len(sys.argv) > 1):
  n = int(sys.argv[1])

if __name__ == "__main__":
  x = []
  y = []
  for i in range(2,n):
    yaux = []
    for j in range(0,5):   
      res, ok = solveKT(i)
      yaux.append(res * 1000)
    x.append(i)
    y.append(yaux)
  plot_errors(x,y)