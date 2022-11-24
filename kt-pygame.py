from re import S
import time
import pygame
pygame.init()

n = 4
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 60)
class BoardSquare:
    def __init__(self, x_start, y_start, width_height, is_white):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.is_white = is_white

def calculate_coordinates(x_array, y_array, is_white):
    if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT:
        width_height = SCREEN_WIDTH / n
    else:
        width_height = SCREEN_HEIGHT / n
 
    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height
 
    return BoardSquare(x_coordinate, y_coordinate, width_height, is_white)


chess_board = []
is_white = False
for y in range(n):
    chess_row = []
    is_white = not is_white
    for x in range(n):
        chess_row.append(calculate_coordinates(x, y, is_white))
        is_white = not is_white
    chess_board.append(chess_row)

for row in chess_board:
    for square in row:
        surf = pygame.Surface((square.width_height, square.width_height))
 
        if square.is_white:
            surf.fill((255, 255, 255))
        else:
            surf.fill((0, 0, 0))
        text = font.render("-1", True, green, blue)
        textRect = text.get_rect()
        textRect.center = [square.x_start,square.y_start]
        screen.blit(surf, (square.x_start, square.y_start))
        rect = surf.get_rect()
        screen.blit(surf, (square.x_start, square.y_start))
        pygame.display.flip()
            
def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[n * x + y] == -1):
        return True
    return False
 
def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i*n + j], end=' ')
        print()
 
def solveKT(n):
    board = [-1 for i in range(n*n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    board[0] = "00"
    update_chessboard(0,0,"00")
    pos = 1

    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
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
            clean_cell(curr_x,curr_y,str(pos-1))
            board[n * new_x + new_y] = pos_aux
            update_chessboard(new_x,new_y,pos_aux)
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
 
            board[n * new_x + new_y] = -1
            clean_cell(new_x,new_y,"-1")
    return False

def update_chessboard(pos_x,pos_y,p):
  square = chess_board[pos_x][pos_y]
  surf = pygame.Surface((square.width_height, square.width_height))
  surf.fill((255, 0, 0))
  text = font.render(p, True, green)
  textRect = surf.get_rect()
  textRect.center = (textRect.centerx, textRect.center[1])
  surf.blit(text,textRect)
  rect = surf.get_rect()
  screen.blit(surf, (square.x_start, square.y_start))
  pygame.display.flip()
  pygame.time.wait(1000)

def clean_cell(pos_x,pos_y,p):
  square = chess_board[pos_x][pos_y]
  surf = pygame.Surface((square.width_height, square.width_height))
  if (square.is_white):
    surf.fill((255, 255, 255))
  else:
    surf.fill((0,0,0))
  
  text = font.render(p, True, green)
  textRect = surf.get_rect()
  textRect.center = (textRect.centerx, textRect.center[1])
  surf.blit(text,textRect)
  rect = surf.get_rect()
  screen.blit(surf, (square.x_start, square.y_start))
  pygame.display.flip()
  pygame.time.wait(500)
  
if __name__ == "__main__":
    solveKT(n)