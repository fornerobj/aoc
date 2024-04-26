with open('realinput', 'r') as file1:
    text = file1.read()

class key:
    def __init__(self, destination, source, range):
        self.range = (int(source), int(source)+int(range)-1)
        self.diff  = int(destination) - int(source)

# map = array of keys ^, input = array of ranges
def mapFromKeys(map, input):
    arr = []
    while(input):
        r = input.pop()
        overlaps = False
        #print("Range is", r)
        for key in map:
            k = key.range
            #print("Key range is", k)
            d = key.diff
            if r[1] >= k[0] and r[0] <= k[1]:
                overlaps = True
                if (r[0] >= k[0] and r[1] <= k[1]):
                    #print("A")
                    arr.append((r[0]+d, r[1]+d))
                elif (r[0] >= k[0] and r[1] > k[1]):
                    #print("B")
                    arr.append((r[0]+d, k[1]+d))
                    input.append((k[1]+1, r[1]))
                elif (r[0] < k[0] and r[1] <= k[1]):
                    #print("C")
                    input.append((r[0], k[0]-1))
                    arr.append((k[0]+d, r[1]+d))
                else:
                    #print("D")
                    input.append((r[0], k[0]-1))
                    arr.append((k[0]+d, k[1]+d))
                    input.append((k[0]+1, r[1]))
        if (not overlaps):
            arr.append((r[0], r[1]))
    return arr


def noEmpty(s):
    return s != ''

sections = list(filter(noEmpty, text.split("\n\n")))
inputSeeds = sections[0].split(" ")[1:]
ranges = [(int(inputSeeds[0]), int(inputSeeds[0])+int(inputSeeds[1])-1), (int(inputSeeds[2]), int(inputSeeds[2])+int(inputSeeds[3])-1)]
      
maps = [[],[],[],[],[],[],[]]

for i, section in enumerate(sections[1:]):
    for line in list(filter(noEmpty, section.split("\n")[1:])):
        k = line.split(" ")
        maps[i].append(key(k[0],k[1],k[2]))

for m in maps:
    ranges = mapFromKeys(m, ranges)

ans = sorted(ranges)[0][0] 
print(ans)

