import numpy as np
import sys

# example input 0,0,0,0,0,0,0,9,0,0,9,0,7,0,0,2,1,0,0,0,4,0,9,0,0,0,0,0,1,0,0,0,8,0,0,0,7,0,0,4,2,0,0,0,5,0,0,8,0,0,0,0,7,4,8,0,1,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,9,6,1,3,0,0,0
# Entering sudoku grid
# Checks row, column and square to find same number to n
# if n founded, return False
# Else, return True

def print_grid(grid):
    template = """
+---------+---------+---------+
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
+---------+---------+---------+
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
+---------+---------+---------+
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
| {}  {}  {} | {}  {}  {} | {}  {}  {} |
+-----------------------------+
    """.format(*grid.flatten())
    print(template)

def posible(x, y ,n, grid):
    # Checking column
    for i in range(9):
        if grid[i][x] == n:
            return False
    # Checking row
    for i in range(9):
        if grid[y][i] == n:
            return False
    # Checking square
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            # Finding empty spaces in grid
            if grid[y][x] == 0:
                for n in range(1,10):
                    if posible(x, y ,n, grid):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    print("Solved grid:")
    print_grid(grid)
    sys.exit()


if __name__ == "__main__":
    sudoku = input("Enter sudoku: ")
    sudoku_list = sudoku.split(",")
    sudoku_list_int = []
    for i in sudoku_list:
        sudoku_list_int.append(int(i))
    #print_grid(sudoku_list_int)
    grid = np.array(sudoku_list_int).reshape(9,9)
    print("\nEntered grid:")
    print_grid(grid)
    solve(grid)
