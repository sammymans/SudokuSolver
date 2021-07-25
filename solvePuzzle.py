#starting position of the sudoku board
board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]   

def printBoard(board):
    #cycle through the number of rows in the grid
    for i in range(len(board)):
        #if our row is divisuble by 3, lets add some quadrant dividers
        if(i % 3 == 0 and i != 0):
            print(" - - - - - - - - - - - - -")

        #cycle through the columns
        for j in range(len(board[0])):
            #if our element in the column is divisuble by 3, lets add the qudrant divider
            if(j % 3 == 0 and j != 0):
                #use end ="" so we dont go to the nextline after using print()
                print(" | ", end ="")
            #if we run into the last element on the line, print the element and then go to the next line
            if(j == 8):
                print(board[i][j])
            #if not, just print normally with spaces in between numbers AND on the same line (end = "")
            else:
                print(str(board[i][j]) + " ", end="")

def findEmpty(board):
    #loop through the entire board
    for i in range(len(board)):
        for j in range(len(board[0])):
            #if the contents of that grid space are 0, means empty
            if(board[i][j] == 0):
                #return the position
                return i,j                  #return as 'row', 'col'

    #If no squares are equal to zero just return None
    return None

def valid(board, num, pos):
    #note: pos is a tuple, so pos[0] represents the first element -> in our case the row
    #Check if the number is valid in the ROW it is in
    for i in range(len(board[0])):
        if(board[pos[0]][i] == num and pos[1] != i):
            return False

    #Check if the number is valid in the COLUMN it is in
    for i in range(len(board)):
        if(board[i][pos[1]] == num and pos[0] != i):
            return False

    #Check if the number is valid in the 3x3 BOX it is in
    #First determine the location of the box in x,y coordinates
    boxPosX = pos[1] // 3
    boxPosY = pos[0] // 3

    #Loop through only the box we are working in
    for i in range(boxPosY * 3, boxPosY * 3 + 3):
        for j in range(boxPosX * 3, boxPosX * 3 + 3):
            if(board[i][j] == num and i != pos[0] and j != pos[1]):
                return False

    #if all the above checks fail above (row, col, box), that means our spot is valid -> return True
    return True

def solve(board):
    #base case:

    #variable find for whether or not the element in grid is empty or not
    find = findEmpty(board)
    #if it has an element (not empty), just return True -> we found the solution
    if not find:
        return True
    #else, findEmpty(board) will return the coordinates for row, col, so set those equal to two variables row,col
    else:
        row, col = find 

    #attempt to put numbers 1-9 in the solution
    for num in range(1,10):
        #if the value attempted is actually valid, replace that spot on the board with the attempted number
        if valid(board, num, (row, col)):
            #if it is valid, input that value into the board
            board[row][col] = num

            #if the board solved, we need to return True for the base case
            if(solve(board)):
                return True
            
            #if the board did not solve, reset the value back to 0 to re run the method "solve"
            board[row][col] = 0
    
    #if the board did not solve, we need to return False
    return False


solve(board)
printBoard(board)
