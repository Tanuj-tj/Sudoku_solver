# unsolved Sudoku Board
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

def solve(bo):
    """
    Solve the given sudoku using recursion and backtracking
    :param bo: Board
    :return:
    """
    find = find_empty(bo)
    # Base case
    if not find:
        return True
    else:
        row,col = find

    # Looping through the values from 1 to 9
    for i in range(1,10):

        # Check if the solution is valid or not
        if valid(bo,i,(row,col)):

            # If valid add it into the board
            bo[row][col] = i

            # Recursively call solve
            if solve(bo):
                return True

            # If solve = False Backtrack and reset the last element
            bo[row][col] = 0

    return False

def valid(bo,num,pos):
    """
    Given the board check if it is valid or not .
    We will check here the row , the column and the inner square .
    :param bo: Board
    :param num: Inserted value
    :param pos: (i,j) => The Location of empty cells
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Figure out which box we are in
    """
    7 8 0  | 4 0 0  | 1 2 0
    6 0 0  | 0 7 5  | 0 0 9
    0 0 0  | 6 0 1  | 0 7 8
    - - - - - - - - - - - - - 
    0 0 7  | 0 4 0  | 2 6 0
    0 0 1  | 0 5 0  | 9 3 0
    9 0 4  | 0 6 0  | 0 0 5
    - - - - - - - - - - - - - 
    0 7 0  | 3 0 0  | 0 1 2
    1 2 0  | 0 0 7  | 4 0 0
    0 4 9  | 2 0 6  | 0 0 7
    """
    box_x = pos[1] // 3  # Eg. 0,1,2
    box_y = pos[0] // 3  # Eg. 0,1,2

    # Looping through every box
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    # If we make it through every box then we will return True
    return True

def print_board(bo):
    """
    Print the given/ sudoku board
    :param bo: Board
    """
    for i in range(len(bo)):  # Rows => 9
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):  # Columns => 9
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    Count the no of enpty cells in a given sudoku board
    :param bo: Board
    """
    for i in range(len(bo)): # Rows
        for j in range(len(bo[0])): # Columns
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("\n")
print("Solved Sudoku:")
print_board(board)

