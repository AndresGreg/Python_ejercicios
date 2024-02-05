import pygame
from pygame.locals import *
import time
import copy
import numpy as np
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1050))
clock = pygame.time.Clock()
running = True
color_sand = (133, 5, 48)
color_gray = (82, 79, 71)
color_black = (36, 34, 28)
color_water = (11, 57, 77)
color_rock = (163, 130, 11)
color_gas = (189, 106, 6)

cell_size = 10
grid_size = 1
colxrow = 100
pause = True
paint = 1
pygame.display.set_caption("Celullar automata: elements")

matrix = np.zeros((colxrow, colxrow))
new_matrix = np.zeros((colxrow, colxrow))

#Genera los muros
row_index = 0    
for row in matrix:
    column_index = 0
    for column in row:
        if row_index == 0 or row_index == 99 or column_index == 0 or column_index == 99:
            matrix[row_index, column_index] = 1
                     
        column_index +=1
    row_index +=1





def print_screen(matrix):
    
    row_index = 0    
    for row in matrix:
        column_index = 0
        for column in row:
            
            if matrix[row_index, column_index] == 0: #Pinta blank(black)
                
                rectangulo = pygame.Rect(row_index*cell_size+grid_size,column_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                pygame.draw.rect(screen, color_black, rectangulo)
            
            if matrix[row_index, column_index] == 1: #pinta rocks
                
                rectangulo = pygame.Rect(row_index*cell_size+grid_size,column_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                pygame.draw.rect(screen, color_rock, rectangulo)   
                

            if matrix[row_index, column_index] == 2: #paint sand

                rectangulo = pygame.Rect(row_index*cell_size+grid_size,column_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                pygame.draw.rect(screen, color_sand, rectangulo) 

            if matrix[row_index, column_index] == 3: #paint water

                rectangulo = pygame.Rect(row_index*cell_size+grid_size,column_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                pygame.draw.rect(screen, color_water, rectangulo)

            if matrix[row_index, column_index] == 4: #paint gas

                rectangulo = pygame.Rect(row_index*cell_size+grid_size,column_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                pygame.draw.rect(screen, color_gas, rectangulo)

            
            column_index +=1
        row_index +=1
    
    #leyend
    font = pygame.font.SysFont(None, 30)
    text_blank = font.render('0: BLANK', True, color_black, color_gray)
    textRect_blank = text_blank.get_rect()
    textRect_blank.topleft = (60, 1020)
    screen.blit(text_blank, textRect_blank)

    font = pygame.font.SysFont(None, 30)
    text_rocks = font.render('1: ROCKS', True, color_rock, color_gray)
    textRect_rocks = text_rocks.get_rect()
    textRect_rocks.topleft = (260, 1020)
    screen.blit(text_rocks, textRect_rocks)

    font = pygame.font.SysFont(None, 30)
    text_sand = font.render('2: SAND', True, color_sand, color_gray)
    textRect_sand = text_sand.get_rect()
    textRect_sand.topleft = (460, 1020)
    screen.blit(text_sand, textRect_sand)

    font = pygame.font.SysFont(None, 30)
    text_water = font.render('3: WATER', True, color_water, color_gray)
    textRect_water = text_water.get_rect()
    textRect_water.topleft = (660, 1020)
    screen.blit(text_water, textRect_water)

    font = pygame.font.SysFont(None, 30)
    text_gas = font.render('4: GAS', True, color_gas, color_gray)
    textRect_gas = text_gas.get_rect()
    textRect_gas.topleft = (860, 1020)
    screen.blit(text_gas, textRect_gas)

    
    return matrix

def calc_step(matrix):
    new_matrix = copy.deepcopy(matrix)
    row_index = 0    
    for row in matrix:
        column_index = 0
        for column in row:
            
            if matrix[row_index, column_index] == 0: ######################Pinta blank(black)
                
                None
            
            if matrix[row_index, column_index] == 1: #######################pinta rocks

                None

            if matrix[row_index, column_index] == 2: #####################paint sand

                if matrix[row_index, column_index+1] == 0:  #sand goes down
                    new_matrix[row_index, column_index+1] = 2
                    new_matrix[row_index, column_index] = 0

                if matrix[row_index, column_index+1] == 3: # sand density
                    new_matrix[row_index, column_index+1] = 2
                    new_matrix[row_index, column_index] = 3
                
                if matrix[row_index, column_index+1] == 4: # sand density
                    new_matrix[row_index, column_index+1] = 2
                    new_matrix[row_index, column_index] = 4
                    

                if matrix[row_index, column_index+1] != 0: #sand goes sideways
                    

                    if matrix[row_index+1, column_index+1] == 0 and matrix[row_index+1, column_index] == 0 and matrix[row_index-1, column_index+1] == 0 and matrix[row_index-1, column_index] == 0:# CAN GO BOTH SIDE WAYS? RANDOM CHOICE
                        random_side = random.randint(0, 2)
                        if random_side == 0:
                            new_matrix[row_index+1, column_index] = 2
                            new_matrix[row_index, column_index] = 0
                        else:
                            new_matrix[row_index-1, column_index] = 2
                            new_matrix[row_index, column_index] = 0

                    else:
                        if matrix[row_index+1, column_index+1] == 0 and matrix[row_index+1, column_index] == 0: #sand only can go right
                            new_matrix[row_index+1, column_index] = 2
                            new_matrix[row_index, column_index] = 0
                        elif matrix[row_index-1, column_index+1] == 0 and matrix[row_index-1, column_index] == 0: #sand only can go left       
                            new_matrix[row_index-1, column_index] = 2
                            new_matrix[row_index, column_index] = 0

            if matrix[row_index, column_index] == 3: ###############################paint water
                
                    if matrix[row_index, column_index+1] == 0:  #water goes down
                        new_matrix[row_index, column_index+1] = 3 
                        new_matrix[row_index, column_index] = 0
                    elif matrix[row_index, column_index+1] == 4: # sand density
                        new_matrix[row_index, column_index+1] = 3
                        new_matrix[row_index, column_index] = 4
                        

                    else: 
                        

                        if 0 in matrix[:, column_index+1]:# if there are space in the next row...
                            qty_right = False
                            qty_left = False
                            for i in range(1,colxrow):
                                if row_index+i < colxrow:
                                    if matrix[row_index+i, column_index+1] == 0:
                                        qty_right = True
                                        break
                                if row_index-i > 0:
                                    if matrix[row_index-i, column_index+1] == 0:
                                        qty_left = True
                                        break
                                
                            
                            if qty_right:
                                if matrix[row_index+1, column_index] == 0: #water go right
                                    new_matrix[row_index+1, column_index] = 3
                                    new_matrix[row_index, column_index] = 0
                                    
                            elif qty_left:
                                if matrix[row_index-1, column_index] == 0: #water go left
                                    new_matrix[row_index-1, column_index] = 3
                                    new_matrix[row_index, column_index] = 0
                                

                        

                            
                        




         
                


            if matrix[row_index, column_index] == 4: ###########################paint gas

                    if matrix[row_index, column_index-1] == 0:  #water goes down
                        new_matrix[row_index, column_index-1] = 4 
                        new_matrix[row_index, column_index] = 0

                    else: 
                        

                        if 0 in matrix[:, column_index-1]:# if there are space in the next row...
                            qty_right = False
                            qty_left = False
                            for i in range(1,colxrow):
                                if row_index+i < colxrow:
                                    if matrix[row_index+i, column_index-1] == 0:
                                        qty_right = True
                                        break
                                if row_index-i > 0:
                                    if matrix[row_index-i, column_index-1] == 0:
                                        qty_left = True
                                        break
                                
                            
                            if qty_right:
                                if matrix[row_index+1, column_index] == 0: #water go right
                                    new_matrix[row_index+1, column_index] = 4
                                    new_matrix[row_index, column_index] = 0
                                    
                            elif qty_left:
                                if matrix[row_index-1, column_index] == 0: #water go left
                                    new_matrix[row_index-1, column_index] = 4
                                    new_matrix[row_index, column_index] = 0

            
            column_index +=1
        row_index +=1

          
    return new_matrix

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
              

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("pause")
            
                pause = not pause
        if pygame.mouse.get_pressed()[0]:
            x, y= mouse_position
            column_click = int(y/cell_size)
            row_click = int(x/cell_size)

            
            if column_click != 1 and column_click != colxrow-2 and row_click != 1 and row_click != colxrow-2:
                try:
                    matrix[row_click][column_click] = paint
                    matrix[row_click+1][column_click] = paint
                    matrix[row_click-1][column_click] = paint
                    matrix[row_click][column_click+1] = paint     
                    matrix[row_click][column_click-1] = paint
                except:
                   pass
             
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
               paint = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
               paint = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
               paint = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
               paint = 3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
               paint = 4

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_gray)

    # RENDER YOUR GAME HERE

    
                    
    print_screen(matrix)
    matrix = calc_step(matrix)
    

    time.sleep(0.0001)
    mouse_position = pygame.mouse.get_pos()
            
    pygame.display.flip()
    
    clock.tick(600)  # limits FPS to 60

pygame.quit()