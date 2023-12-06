import math
f = open("input-data.txt", "r")

# parse data
times = [int(time) for time in f.readline().split()[1::]]
distances = [int(distance) for distance in f.readline().split()[1::]]
races = list(zip(times, distances)) 
ans = []

for race in races:
    time, dist = race
    curr_race_ans = 0
    for i in range(time):
        speed = i+1
        if (speed * (time - (i + 1))) > dist:
            curr_race_ans += 1
    ans.append(curr_race_ans)

print(math.prod(ans))
f.close()
