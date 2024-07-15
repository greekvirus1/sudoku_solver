import random # type: ignore

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

def sudoku_find_square(x,y):
    '''
    Returns a list of the coordinates where the 3x3 square associated of X and Y starts
    '''
    if x < 3:
        if y < 3:
            return [0, 0]
        elif y < 6:
            return [0, 3]
        else:
            return [0, 6]
    elif x < 6:
        if y < 3:
            return [3, 0]
        elif y < 6:
            return [3, 3]
        else:
            return [3, 6]
    else:
        if y < 3:
            return [6, 0]
        elif y < 6:
            return [6, 3]
        else:
            return [6, 6]

def sudoku_solver(board):
    board_copy = board.copy()
    attempts = 1
    x = 0
    while True:
        for x in range(9):
            y = 0
            for y in range(9):
                print(x,y,attempts)
                if board_copy[x][y] == 0:
                    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    #Check row
                    for i in range(9):
                        if board_copy[i][y] != 0:
                            if board_copy[i][y] in valid_numbers:
                                valid_numbers.remove(board_copy[i][y])
                    #Check column
                    for j in range(9):
                        if board_copy[x][j] !=0:
                            if board_copy[x][j] in valid_numbers:
                                valid_numbers.remove(board_copy[x][j])
                    #Check 3x3 square
                    sqr_coordinates = sudoku_find_square(x,y)
                    i = sqr_coordinates[0]
                    for i in range(i, i+3):
                        j =sqr_coordinates[1]
                        for j in range(j, j+3):
                            if board_copy[i][j] != 0:
                                if board_copy[i][j] in valid_numbers:
                                    valid_numbers.remove(board_copy[i][j])
                    try:
                        board_copy[x][y] = random.choice(valid_numbers)
                    except:
                        board_copy[x][y] = random.randint(1,9)
        if sudoku_checker(board_copy) == True:
            print("Solution reached, number of attempts: {}".format(attempts))
            return board_copy
        else:
            x = 0
            board_copy = board.copy()
            attempts += 1

