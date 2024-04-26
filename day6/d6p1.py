import math

with open('input', 'r') as file1:
    lines = file1.read().split("\n")

def noEmpty(s):
    return s != ''

lines = list(filter(noEmpty, lines))

times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()
ans = []
for i in range(len(times)):
    ways_to_win = 0
    t = int(times[i])
    d = int(distances[i])
    for j in range(t):
        dis = j * (t-j)
        if dis > d:
            ways_to_win += 1
    ans.append(ways_to_win)
print(math.prod(ans))
