with open('realinput', 'r') as file1:
    text = file1.read()

class key:
    def __init__(self, destination, source, range):
        self.source = int(source)
        self.destination = int(destination)
        self.range = int(range)

def mapFromKeys(map, input):
    for key in map:
        if input in range(key.source, key.source + key.range):
            return input + (key.destination - key.source)
    return input


def noEmpty(s):
    return s != ''

sections = list(filter(noEmpty, text.split("\n\n")))
inputSeeds = sections[0].split(" ")[1:]
maps = [[],[],[],[],[],[],[]]

for i, section in enumerate(sections[1:]):
    for line in list(filter(noEmpty, section.split("\n")[1:])):
        k = line.split(" ")
        maps[i].append(key(k[0],k[1],k[2]))

minNum = float('inf')
for x in inputSeeds:
    x = int(x)
    for m in maps:
        x = mapFromKeys(m, x)
    minNum = min(x, minNum)

print(minNum)
