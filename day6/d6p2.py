with open('input', 'r') as file1:
    lines = file1.read().split("\n")

def noEmpty(s):
    return s != ''

lines = list(filter(noEmpty, lines))

times = lines[0].split(":")[1].split()
time = int("".join(times))
distances = lines[1].split(":")[1].split()
distance = int("".join(distances))

start, end = 0, 0

for j in range(time):
    dis = j * (time-j)
    if dis > distance:
        start = j

for j in range (time, 0, -1):
    dis = j * (time-j)
    if dis > distance:
        end = j

print(start-end+1)
