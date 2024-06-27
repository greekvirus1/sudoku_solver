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
