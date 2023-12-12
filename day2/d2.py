def isValidGame(rounds, i):
    for r in rounds: 
        rolls = r.strip().split(", ")
        for roll in rolls:
            reds = 0
            greens = 0
            blues = 0
            if(reds != 0 or greens != 0 or blues != 0):
                print (rounds)
            colors = roll.split(" ")
            if(colors[1] == 'red'):
                reds += int(colors[0])
                if(reds > 12): return False
            if(colors[1] == 'green'):
                greens  += int(colors[0])
                if(greens > 13): return False
            if(colors[1] == 'blue'):
                blues += int(colors[0])
                if(blues > 14): return False
    return True

with open('input', 'r') as file1:
    lines = file1.readlines()

games = {}

sum = 0
for line in lines:
    gamenumber = line.split(":")[0].split(" ")[1]
    rounds = line.split(":")[1].strip().split("; ")
    if(isValidGame(rounds, gamenumber)):
        sum += int(gamenumber)

print(sum)

    
    