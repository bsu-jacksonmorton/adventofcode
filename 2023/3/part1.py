import string
f = open("input-data.txt", "r")
matrix = []
for line in f:
    matrix.append(line)

ROWS = len(matrix)
COLS = len(matrix[0])
ans = 0
symbols = list(string.punctuation)
symbols.remove('.')
def has_adjacent_symbol(row, col):
    # check above
    if row - 1 >= 0 and matrix[row-1][col] in symbols:
        return True
    # check below
    if row + 1 < ROWS and matrix[row+1][col] in symbols:
        return True
    # check left
    if col - 1 >= 0 and matrix[row][col-1] in symbols:
        return True
    # check right
    if col + 1 < COLS and matrix[row][col+1] in symbols:
        return True
    # check diagonal top left
    if row - 1 >= 0 and col - 1 >= 0 and matrix[row-1][col-1] in symbols:
        return True
    # check diagonal top right
    if row - 1 >= 0 and col + 1 < COLS and matrix[row-1][col+1] in symbols:
        return True
    # check diagonal bottom left
    if row + 1 < ROWS and col - 1 >= 0 and matrix[row+1][col-1] in symbols:
        return True
    # check diagonal bottom right
    if row + 1 < ROWS and col + 1 < COLS and matrix[row+1][col+1] in symbols:
        return True
    return False
    
for row in range(ROWS):
    curr_num_start = None 
    is_adjacent = False
    for col in range(COLS):
        if matrix[row][col].isdigit() == False and curr_num_start != None:
            if is_adjacent:
                ans += int(matrix[row][curr_num_start:col])
                is_adjacent = False
            curr_num_start = None
        elif matrix[row][col].isdigit():
            if curr_num_start == None:
                curr_num_start = col
            is_adjacent = is_adjacent or has_adjacent_symbol(row,col) 

print(ans)
f.close()
