board = [
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

# Check given position on the board with a number from 1-9 denoted as 'n'.
# -------->x|
#           |
#           |
#           |
#           |
#           V
#           y


def check_pos(y, x, n, board):
    # Each element in row Check
    for i in range(9):
        if board[y][i] == n:
            return False
    # Each element in column Check
    for i in range(9):
        if board[i][x] == n:
            return False
    # 3x3 Check
    y1 = (y//3)*3
    x1 = (x//3)*3
    # Row and column of 3x3 box found using integer division and checked through following loop
    for i in range(3):
        for j in range(3):
            if board[y1 + i][x1 + j] == n:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            # Printing horizontal line for separation vertically
            print('- - - - - - - - - - - ')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                # Printing vertical line for separation horizontally
                print('| ', end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(board)


def solve(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:  # Checking for empty spaces which are denoted by 0 in this case
                for n in range(1, 10):
                    # Checking each value from 1-9 to place into an empty space on the board
                    if check_pos(y, x, n, board):
                        board[y][x] = n
                        # Recursively calling the solve function again to repeat the insertion process
                        solve(board)
                        # Backtracking algorithm
                        # Backtracking if the choice is incorrect leading to a wrong solution
                        board[y][x] = 0

                return  # If all possibilities are not viable, we will return out from loop

    print("=======================")
    print("=======================")
    print_board(board)


solve(board)
