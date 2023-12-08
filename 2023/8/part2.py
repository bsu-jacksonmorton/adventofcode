import re
import math

f = open("input-data.txt", "r")
INSTRUCTION = f.readline().strip()
# eat empty line
f.readline()
NODES = dict()
DIRS = {
        "L": 0,
        "R": 1
        }
q = []
for line in f:
   line = re.sub("[(,)=]", "", line).strip().split()
   NODES[line[0]] = line[1:]
   if "A" in line[0]:
       q.append((line[0],line[0]))
ans = 0
i = 0
cycle_tracking = {}
t = 0
while q:
    if i >= len(INSTRUCTION):
        i = 0
    n = len(q)
    nodes_with_z = 0
    for _ in range(n):
        start_node, curr_node = q.pop(0)
        if "Z" in curr_node:
            cycle_tracking[start_node] = t
            nodes_with_z += 1
        '''
        If the following condition is true, then we have seen all the nodes and can determine what there cycle length is. We then need to determine what the LCM is of all the cycle lengths is so we can determine where they will converge.
        '''
        if len(cycle_tracking) == n:
            ans = math.lcm(*cycle_tracking.values())
            break
        q.append((start_node, NODES[curr_node][DIRS[INSTRUCTION[i]]]))
    if len(cycle_tracking) == n:
        break
    t += 1
    i += 1

print("Answer:", ans)
