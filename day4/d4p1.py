with open('input', 'r') as file1:
    lines = file1.read().splitlines()

def noEmpty(s):
    return s != ''

total = 0
for i, line in enumerate(lines):
    points = 0
    line = line.split(':')[1].strip()
    winners = list(filter(noEmpty, line.split('|')[0].strip().split(' ')))
    scratches = list(filter(noEmpty, line.split('|')[1].strip().split(' ')))
    for s in scratches: 
        if s in winners:
            if points == 0:
                points += 1
            else:
                points *= 2
    total += points
print(total)