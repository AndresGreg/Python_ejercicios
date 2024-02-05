import pygame
import time
import copy
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
color_white = (200, 200, 200)
color_gray = (100, 100, 100)
color_black = (0, 0, 0)
cell_size = 10
grid_size = 1
colxrow = 100
pause = True
cell_vecinas = 0
pygame.display.set_caption("Game of life")


matrix = [[column for column in range(colxrow)] for row in range(colxrow)]
for column in range(colxrow):
    for row in range(colxrow):
        matrix[column][row] = False


def print_pantalla(matrix):
    colum_index = 0
    
    for fila in matrix:
            
            row_index = 0
            for ind_fila in fila:
                if matrix[colum_index][row_index] == True:
                    
                    rectangulo = pygame.Rect(row_index*cell_size+grid_size,colum_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                    pygame.draw.rect(screen, color_white, rectangulo)
               
                if matrix[colum_index][row_index] == False:

                    rectangulo = pygame.Rect(row_index*cell_size+grid_size,colum_index*cell_size+grid_size, cell_size-grid_size, cell_size-grid_size)
                    pygame.draw.rect(screen, color_black, rectangulo)   

                row_index +=1
            
            colum_index +=1
    return matrix

def juega_pantalla(matrix):
    row_index = 0
    colum_index = 0
    new_matrix = copy.deepcopy(matrix)
    
    for colum in matrix:
            
            row_index = 0

            for row in colum:
                cell_vecinas = 0
                
                if 99 > colum_index > 0 and 99 > row_index > 0:  
                    cell_vecinas = 0
                #try:
                    if matrix[colum_index-1][row_index-1]== True:
                        cell_vecinas +=1
                    if matrix[colum_index-1][row_index]== True:
                        cell_vecinas +=1
                    if matrix[colum_index-1][row_index+1]== True:
                        cell_vecinas +=1
                    if matrix[colum_index][row_index-1]== True:
                        cell_vecinas +=1
                    #if matrix[colum_index][row_index]:
                        #cell_vecinas +=1
                    if matrix[colum_index][row_index+1]== True:
                        cell_vecinas +=1
                    if matrix[colum_index+1][row_index-1]== True:
                        cell_vecinas +=1
                    if matrix[colum_index+1][row_index]== True:
                        cell_vecinas +=1
                    if matrix[colum_index+1][row_index+1]== True:
                        cell_vecinas +=1
                    
                #except:
                    
                   # None
                    #print("mal")
                    if matrix[colum_index][row_index] == True:
                        if cell_vecinas == 2:
                            new_matrix[colum_index][row_index] = True 
                        elif cell_vecinas == 3:
                            new_matrix[colum_index][row_index] = True 
                        elif cell_vecinas < 2 or cell_vecinas > 3:
                            new_matrix[colum_index][row_index] = False
                    
                    elif matrix[colum_index][row_index] == False:
                       
                        if cell_vecinas == 3:
                            new_matrix[colum_index][row_index] = True 
                        elif cell_vecinas < 3 or cell_vecinas > 3:
                            new_matrix[colum_index][row_index] = False
                
                    

                    """     if matrix[colum_index][row_index] == True and cell_vecinas == 3:  #VIVE
                        new_matrix[colum_index][row_index] = True 
                    elif matrix[colum_index][row_index] == True and cell_vecinas == 2: #VIVE
                        new_matrix[colum_index][row_index] = True 
                    elif matrix[colum_index][row_index] == True and cell_vecinas< 2: #muere
                        new_matrix[colum_index][row_index] = False

                    elif matrix[colum_index][row_index] == True and cell_vecinas> 3: #muere overpopulation
                        new_matrix[colum_index][row_index] = False

                    elif matrix[colum_index][row_index] == False and cell_vecinas == 3: # REVIVE
                        new_matrix[colum_index][row_index] = True

                    else:
                        
                    new_matrix[colum_index][row_index] = False"""
                    """
                        if matrix[colum_index][row_index] == True:
                     if cell_vecinas == 2 or cell_vecinas == 3:

                        new_matrix[colum_index][row_index] = True
                        

                    
                        else: 
                        
                        new_matrix[colum_index][row_index] = False
                        
                    if matrix[colum_index][row_index] == False:
                    if cell_vecinas == 3:
                        
                        
                        new_matrix[colum_index][row_index] = True
                    """
                
                
                
                row_index +=1
            
            colum_index +=1
          
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
            column_click = int(y/10)
            row_click = int(x/10)
            matrix[column_click][row_click] = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_gray)

    # RENDER YOUR GAME HERE

   

    
    
    if not pause:
       
       matrix = juega_pantalla(matrix)
       
       matrix = print_pantalla(matrix)
    else:
       
       matrix = print_pantalla(matrix)

    time.sleep(0.01)

    mouse_position = pygame.mouse.get_pos()
    

    
                
            
    pygame.display.flip()
    



    clock.tick(60)  # limits FPS to 60

pygame.quit()