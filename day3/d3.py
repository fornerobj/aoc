def getNumberL(line, x):
    num = ''
    x -= 1  # Start from the position left to x
    while x >= 0 and line[x].isdigit():
        num = line[x] + num
        x -= 1
    return num

def getNumberR(line, x):
    num = ''
    x += 1  # Start from the position right to x
    while x < len(line) and line[x].isdigit():
        num = num + line[x]
        x += 1
    return num

def getNumber(line, x):
    return int(getNumberL(line, x) + line[x] + getNumberR(line, x))

#check if character c is a symbol
def isStar(c):
    return c == "*"

#check upperleft, up, upright, left, right, lowerleft, down, lowerright and return true if any of them is a symbol
def hasTwoAdjacentNumbers(lines, x, y, xmax, ymax):
    nums = []
    # Define the offsets for the neighboring cells
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Check each neighboring cell
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= xmax and 0 <= ny <= ymax and (lines[ny][nx]).isdigit():
            if(getNumber(lines[ny], nx)) not in nums:
                nums.append(getNumber(lines[ny], nx))
    
    if(len(nums) >= 2):
        return nums[0] * nums[1]
    else:
        return 0

with open('input', 'r') as file1:
    lines = file1.read().splitlines()

#get length of the lines and the number of lines
xmax = len(lines[0])-1
ymax = len(lines)-1

total = 0
for i, line in enumerate(lines):
    curnum = ""
    check = 0
    gearRatio = 1
    for j, c in enumerate(line):
        if isStar(c):
            total += hasTwoAdjacentNumbers(lines, j, i, xmax, ymax)

print(total)