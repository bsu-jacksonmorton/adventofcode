import re
f = open("input-data.txt", "r")

INSTRUCTION = f.readline().strip()
# eat empty line
f.readline()
NODES = dict()
DIRS = {
        "L": 0,
        "R": 1
        }
for line in f:
   line = re.sub("[(,)=]", "", line).strip().split()
   NODES[line[0]] = line[1:]

ans = 0

curr_node = "AAA"
while curr_node != "ZZZ":
    for i in range(len(INSTRUCTION)):
        if curr_node == "ZZZ":
            break
        curr_node = NODES[curr_node][DIRS[INSTRUCTION[i]]]
        ans += 1
print(ans)
