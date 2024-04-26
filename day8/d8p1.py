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

curr = "AAA"
i = 0
while curr != "ZZZ":
    ind = i % len(instructions)
    instruc = instructions[ind]
    if(instruc == 'L'):
        curr = myMap[curr][0]
    else:
        curr = myMap[curr][1]
    i += 1

print(i)


