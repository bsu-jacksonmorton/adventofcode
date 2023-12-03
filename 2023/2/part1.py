import re
# open the input data file
f = open("input-data.txt", "r")

# CONSTANTS
cubes = {
    "green": 13,
    "red": 12,
    "blue": 14
}

# PART 1
sum_of_ids = 0
for game in f:
    game_valid = True
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
        if cubes[color] < count:
            game_valid = False
            break
    if game_valid:
        sum_of_ids += game_id
print("TOTAL VALID GAME SUM: ", sum_of_ids)
f.close()
