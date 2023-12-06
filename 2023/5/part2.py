import re
f = open("input-data.txt", "r")
seeds = None
maps = []
curr_map = []
for line in f:
    line = line.strip("\n")
    if "map:" in line:
        maps.append(curr_map)
        curr_map = []
    elif "seeds: " in line:
        line = re.sub("seeds: ", "", line)
        seeds = line.split()
        expanded_seeds = []
        for i in range(0, 2, len(seeds) - 2):
            expanded_seeds = expanded_seeds + [*range(int(seeds[i]), int(seeds[i+1]))]
        seeds = expanded_seeds
    elif len(line):
        entry = dict()
        line = line.split()
        entry["dest"] = int(line[0])
        entry["src"] = int(line[1])
        entry["rng"] = int(line[2])
        curr_map.append(entry)

maps.append(curr_map)
maps.pop(0)
ans = None
for seed in seeds:
    seed = int(seed)
    for m in maps:
        for e in m:
            if e["src"] <= seed <= e["src"] + e["rng"]:
                seed = e["dest"] + (seed - e["src"])
                break
    if ans == None:
        ans = seed
    else:
        ans = min(ans, seed)
print(ans)
