with open('input', 'r') as file1:
    lines = file1.read().splitlines()

#check if character c is a symbol
def isSymbol(c):
    return not (c.isdigit() or c == ".")

#check upperleft, up, upright, left, right, lowerleft, down, lowerright and return true if any of them is a symbol
def isPart(lines, x, y, xmax, ymax):
    # Define the offsets for the neighboring cells
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Check each neighboring cell
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= xmax and 0 <= ny <= ymax and isSymbol(lines[ny][nx]):
            return True
    
    return False

#get length of the lines and the number of lines
xmax = len(lines[0])-1
ymax = len(lines)-1

total = 0
for i, line in enumerate(lines):
    curnum = ""
    check = False
    for j, c in enumerate(line):
        if c.isdigit():
            curnum += c
            if(isPart(lines, j, i, xmax, ymax)):
                check = True
        else:
            if curnum != "":
                if(check):
                    total += int(curnum)
                curnum = ""
                check = False
    #collect number at the end of the line
    if curnum != "":
        if(check):
            total += int(curnum)

print(total)