with open('input', 'r') as file1:
    lines = file1.read().splitlines()

def noEmpty(s):
    return s != ''

#keep dictionary of cards and how many copies + original there are
games = {}
numGames = len(lines)
for i in range(numGames):
    games[i] = 1

for i, line in enumerate(lines):
    numMatching = 0
    line = line.split(':')[1].strip()
    winners = list(filter(noEmpty, line.split('|')[0].strip().split(' ')))
    scratches = list(filter(noEmpty, line.split('|')[1].strip().split(' ')))
    nums = []

    for s in scratches: 
        if s in winners:
            numMatching += 1
    
    for j in range(numMatching):
        games[i+j+1] += games[i]
        
total = 0
for game in games:
    total += games[game]
print(total)

