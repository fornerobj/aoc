from math import lcm

with open('input') as f:
    sections = f.read().strip().split("\n\n")

instructions = sections[0]
lines = sections[1].splitlines()

myMap = dict()

for line in lines:
    key, value = line.split(" = ")
    (v1, v2) = value.split(", ")
    v1 = v1[1:]
    v2 = v2[:-1]
    myMap[key] = (v1, v2) 

def numSteps(c):
    i = 0
    while(c[2] != 'Z'):
        ind = i % len(instructions)
        instruc = instructions[ind]
        if(instruc == 'L'):
            c = myMap[c][0]
        else:
            c = myMap[c][1]
        i += 1
    return i

cur = [n for n in myMap if n[2] == "A"]
steps = [numSteps(n) for n in cur]

print(lcm(*steps))

