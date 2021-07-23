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
        #if our row is divisuble by 3, lets add the qudrant dividers
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
            

printBoard(board)

def findEmpty(board):
    #loop through the entire board
    for i in range(len(board)):
        for j in range(len(board[0])):
            #if the contents of that grid space are 0, means empty
            if(board[i][j] == 0):
                #return the position
                return i,j                  #return as 'row', 'col'

findEmpty(board)

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
    boxPosX = pos[1] // 3
    boxPosY = pos[0] // 3

    for i in range(boxPosY * 3, boxPosY * 3 + 3):
        for j in range(boxPosX * 3, boxPosX * 3 + 3):
            if(board[i][j] == num and i != pos[0] and j != pos[1]):
                return False

    #if all the above checks fail above, that means our spot is valid -> True
    return True

print(valid(board=board, num=3, pos=(0,0)))


