# import pygame library to have access to certain commands
import pygame
# access pygame font
pygame.font.init()
 
# Initialize a window/screen for display
screen = pygame.display.set_mode((500, 600))
# Parameters are the size of the window
 
# Set the window caption (title)
pygame.display.set_caption("Sudoku Solver - Using Backtracking Algorithm")

# Set the window icon (top left)
icon = pygame.image.load('sudokuicon.jpg')
pygame.display.set_icon(icon)

#
x = 0
y = 0
dif = 500 / 9
val = 0

# Pre-made Sudoku Board - off a random website
grid =  [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
 
# Make two pre-set fonts
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
# Parameters are name, fontSize

# Function to return the x,y "coordinates" given the position of the mouse
def get_cord(pos):
    # using the global keyword inside a function makes it a global variable
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 
# Function to highlight the cell selected (by mouse)
def draw_box():
    for i in range(2):
        # Highlight the Horizontal Sides of the box selected
        pygame.draw.line(screen, (0, 0, 128), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        # Highlight the Vertical Sides of the box selected
        pygame.draw.line(screen, (0, 0, 128), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)
        # Parameters are : surface, colour, start_pos, end_pos, width  
 
# Function to draw required lines for making Sudoku grid        
def draw():
        
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Fill purple in squares already filled with numebrs
                pygame.draw.rect(screen, (153, 0, 153), (i * dif, j * dif, dif + 1, dif + 1))
                # Parameters are surface, colour, rectangle
 
                # Fill the grid with default numbers specified
                text = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                # Parameters are the text, antialias, colour

                # Draws a surface onto another surface
                screen.blit(text, (i * dif + 15, j * dif + 15))
                # Parameters are source, destination

    # Draw lines horizontally and vertically to form the sudoku grid          
    for i in range(10):
        # box grid lines
        if i % 3 == 0 :
            thick = 7
        # any other grid line
        else:
            thick = 1
        
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
 
# Fill value entered in cell     
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
 
# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 
# Function to check if the value entered in board is valid
def valid(grid, i, j, val):
    for it in range(9):
        #Check if number is present in the row
        if grid[i][it]== val:
            return False
        #Check if number is present in the col
        if grid[it][j]== val:
            return False
    
    #Check if number is present in the 3x3 box
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if grid[i][j]== val:
                return False
    
    #If pass all the above tests, return True -> the box is valid
    return True
 
# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True

    #internally process pygame event handlers
    pygame.event.pump()   

    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            # white color background\
            #screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            # white color background\
            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
 
# Fuction to display instructions for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))
 
# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:
     
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        # Get the mouse position to insert number   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        # print(x)
        # print(y)
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()       
    draw() 
    if flag1 == 1:
        draw_box()      
    instruction()   
 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    