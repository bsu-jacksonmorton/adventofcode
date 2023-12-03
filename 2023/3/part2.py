import string
import math
f = open("input-data.txt", "r")
matrix = []
for line in f:
    matrix.append(line)

ROWS = len(matrix)
COLS = len(matrix[0])
ans = 0
symbols = ["*"]
potential_gears = {}

def has_adjacent_symbol(row, col):
    # check above
    if row - 1 >= 0 and matrix[row-1][col] in symbols:
        return (row-1, col)
    # check below
    if row + 1 < ROWS and matrix[row+1][col] in symbols:
        return (row+1, col)
    # check left
    if col - 1 >= 0 and matrix[row][col-1] in symbols:
        return (row, col-1)
    # check right
    if col + 1 < COLS and matrix[row][col+1] in symbols:
        return (row, col+1)
    # check diagonal top left
    if row - 1 >= 0 and col - 1 >= 0 and matrix[row-1][col-1] in symbols:
        return (row-1, col-1)
    # check diagonal top right
    if row - 1 >= 0 and col + 1 < COLS and matrix[row-1][col+1] in symbols:
        return (row-1, col+1)
    # check diagonal bottom left
    if row + 1 < ROWS and col - 1 >= 0 and matrix[row+1][col-1] in symbols:
        return (row+1, col-1)
    # check diagonal bottom right
    if row + 1 < ROWS and col + 1 < COLS and matrix[row+1][col+1] in symbols:
        return (row+1, col+1)
    
for row in range(ROWS):
    curr_num_start = None 
    is_adjacent = None
    for col in range(COLS):
        if matrix[row][col].isdigit() == False and curr_num_start != None:
            if is_adjacent != None:
                if str(is_adjacent) not in potential_gears:
                    potential_gears[str(is_adjacent)] = []
                potential_gears[str(is_adjacent)].append(int(matrix[row][curr_num_start:col]))
                is_adjacent = None
            curr_num_start = None
        elif matrix[row][col].isdigit():
            if curr_num_start == None:
                curr_num_start = col
            is_adjacent = is_adjacent or has_adjacent_symbol(row,col) 
for nums in potential_gears.values():
    if len(nums) > 1:
        ans += math.prod(nums)
print(ans)
f.close()
