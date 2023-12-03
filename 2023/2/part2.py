import re
import math
# open the input data file
f = open("input-data.txt", "r")

# CONSTANTS
cubes = {
    "green": 1,
    "red": 1,
    "blue": 1
}

# PART 2
sum_of_power_sets = 0
for game in f:
    game_id = re.search("Game [0-9]*:", game)
    if game_id:
        game_id = int(game_id.group().replace("Game ", "").replace(":", ""))
    game = re.sub("Game [0-9]*: ", "", game)
    marbles = game.replace(";", ",").replace("\n", "").split(", ")
    if marbles and marbles[0] == '':
        continue
    # check to see if the marbles make sense for this game
    for marble in marbles:
        count = int(marble.split()[0])
        color = marble.split()[1]
        cubes[color] = max(cubes[color], count)
    sum_of_power_sets += math.prod(cubes.values())

    cubes["green"] = 1
    cubes["blue"] = 1
    cubes["red"] = 1
    
print("SUM OF THE POWER OF THE SETS: ", sum_of_power_sets )
f.close()
