#Sudoku is 9x9 board, containing 3x3 boards, rows and columns must have the numbers 1 to 9 with NO REPEATS
#What does a Sudoku board look like to a computer? A simple board with x,y coordinates
#How to represent this? Is there a sudokuboard-like object? A list with rows and columns would be great.

def custom_size_list(s):
    '''
    returns list filled with 0s of size 's'
    :param s: int
    '''
    the_list = [0] * s
    return the_list

def custom_array_2d(x, y):
    '''
    returns 2d array of custom size
    :param x, y: int
    '''
    arr = [[0] * x for _ in range(y)] #wtf is this? https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    return arr

example_sudoku_board_empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

example_sudoku_board_actu1 = [[3, 9, 1, 2, 8, 6, 5, 7, 4],
                              [4, 8, 7, 3, 5, 9, 1, 2, 6],
                              [6, 5, 2, 7, 1, 4, 8, 3, 9],
                              [8, 7, 5, 4, 3, 1, 6, 9, 2],
                              [2, 1, 3, 9, 6, 7, 4, 8, 5],
                              [9, 6, 4, 5, 2, 8, 7, 1, 3],
                              [1, 4, 9, 6, 7, 3, 2, 5, 8],
                              [5, 3, 8, 1, 4, 2, 9, 6, 7],
                              [7, 2, 6, 8, 9, 5, 3, 4, 1]]

example_sudoku_board_actu2 = [[9, 5, 7, 6, 1, 3, 2, 8, 4],
                              [4, 8, 3, 2, 5, 7, 1, 9, 6],
                              [6, 1, 2, 8, 4, 9, 5, 3, 7],
                              [1, 7, 8, 3, 6, 4, 9, 5, 2],
                              [5, 2, 4, 9, 7, 1, 3, 6, 8],
                              [3, 6, 9, 5, 2, 8, 7, 4, 1],
                              [8, 4, 5, 7, 9, 2, 6, 1, 3],
                              [2, 9, 1, 4, 3, 6, 8, 7, 5],
                              [7, 3, 6, 1, 8, 5, 4, 2, 9]]

#Above I played with lists and lists of lists to understand 2d arrays
#Now let's assume we have a 9x9 array that is a sudoku board
#Empty spaces are represented by 0 and some numbers are assumed to be filled in
#I will assume given board is valid sudoku board, just not finished, so no weird numbers or something.
#How do we proceed? A function that checks the board is a valid sudoku board as stated in line 1
#and another function that does something?

def sudoku_checker(board):
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #check rows
    for x in range(9):
        check_this = board[x].copy()
        check_this.sort()
        if check_this != valid_numbers:
            return False
    #check columns
    for y in range(9):
        check_this = []
        for x in range(9):
            check_this.append(board[x][y])
        check_this.sort()
        if check_this != valid_numbers:
            return False
    #Check 3x3 squares
    x = 0
    check_this = []
    while True:
        for x in range(x, x + 3):
            for y in range(0, 3):
                check_this.append(board[x][y])
        check_this.sort()
        if check_this != valid_numbers:
            return False
        check_this = []
        x -= 2
        for x in range(x, x + 3):
            for y in range(3, 6):
                check_this.append(board[x][y])
        check_this.sort()
        if check_this != valid_numbers:
            return False
        check_this = []
        x -= 2
        for x in range(x, x +  3):
            for y in range(6, 9):
                check_this.append(board[x][y])
        check_this.sort()
        if check_this != valid_numbers:
            return False
        if x and y == 8:
            return True
        else:
            x += 1
            check_this = []

print(sudoku_checker(example_sudoku_board_actu2))
