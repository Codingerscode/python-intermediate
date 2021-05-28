import pygame,sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_COLOR=(23,145,135)
LINE_WIDHT = 15
player = 1

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((28,170,156))


def draw_lines():
    #horizontal
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDHT)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDHT)

    #vertical
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDHT)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDHT)

draw_lines()
board = np.zeros((3,3))

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen,(239,231,200),(int(col * 200 + 100 ),int(row * 200 + 100)),60,20)
            elif board[row][col] == 2:
                pygame.draw.line(screen,(66,66,66),(col * 200 + 55,row * 200 + 200 - 55),(col *200 + 200 -55 ,row * 200 + 55),25)
                pygame.draw.line(screen,(66,66,66),(col * 200 + 55,row * 200  +  55),(col *200 + 200 -55 ,row * 200 +200 - 55),25)
#board
def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    return board[row][col] == 0

def board_full():
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
            return False
    return True


#checking the win function
def check_win(player):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning(col,player)
            return True

    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning(col,player)
            return True

    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning(col,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_winning(player)
        return True       

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_winning(player)
        return True
    
    return False


def draw_vertical_winning(col,player):
    posX = col * 200 + 200
    if player ==1:
        color = (239,231,200)
    elif player == 2:
        color = (66,66,66)
    
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)


def draw_horizontal_winning(row,player):
    posY = row * 200 + 200
    if player ==1:
        color = (239,231,200)
    elif player == 2:
        color = (66,66,66)
    
    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)


def draw_asc_winning(player):
    if player ==1:
        color = (239,231,200)
    elif player == 2:
        color = (66,66,66)
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_winning(player):
    if player ==1:
        color = (239,231,200)
    elif player == 2:
        color = (66,66,66)
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart():
    screen.fill((28,170,156))
    draw_lines()
    player = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

game_over = False
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player ==2 :
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
