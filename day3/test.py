line = "567...567..23"

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
    return getNumberL(line, x) + line[x] + getNumberR(line, x)

print(getNumber(line,0))