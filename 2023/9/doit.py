YELLOW = '\033[93m'

f = open("input-data.txt", "r")

def predict(row):
    saved_rows = []
    curr_row = row
    next_row = []
    while all(v==0 for v in curr_row) == False:
        saved_rows.append(curr_row)
        for i in range(len(curr_row) - 1):
            next_row.append(curr_row[i+1]-curr_row[i])
        curr_row = next_row
        next_row = []
    saved_rows.append(curr_row) 
    for i in range(len(saved_rows)-1, -1, -1):
        saved_rows[i-1].append(saved_rows[i][-1] + saved_rows[i-1][-1])
        saved_rows[i-1].insert(0, saved_rows[i-1][0] - saved_rows[i][0])
    return [saved_rows[0][-1], saved_rows[0][0]]

 
p1 = 0 
p2 = 0
for line in f:
    row = [int(num) for num in line.split()]
    p1_val, p2_val = predict(row)
    p1 += p1_val
    p2 += p2_val
print(YELLOW+str(p1), YELLOW+str(p2))
f.close()
