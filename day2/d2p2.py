def findmaxofcolor(game, color):
    mincolor = 0
    rounds = game.split("; ")
    for r in rounds:
        rolls = r.split(", ")
        for r in rolls:
            colnumpair = r.split(" ")
            if(colnumpair[1] == color):
                mincolor = max(int(colnumpair[0]), mincolor)
    return mincolor

with open('input', 'r') as file1:
    lines = file1.readlines()

sum = 0
for line in lines:
    gamenumber = line.split(":")[0].split(" ")[1]
    game = line.split(":")[1].strip()
    sum += (findmaxofcolor(game, "red") * findmaxofcolor(game, "green") * findmaxofcolor(game, "blue"))

print(sum)