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

dis1 = float('-inf')
dis2 = float('inf')
l, r = 0, time//2

while(dis1 < distance or dis2 >= distance):
    m = (l+r)//2
    dis1 = m * (time-m)
    dis2 = (m-1) * (time-m-1)
    if(dis1 < distance):
        l = m
        continue
    elif (dis1 >= distance and dis2 >= distance):
        r = m
        continue
    else:
        start = m
        break

dis1 = float('-inf')
dis2 = float('inf')
l, r = (time//2)+1, time
while(dis1 < distance or dis2 >= distance):
    m = (l+r)//2
    dis1 = m * (time-m)
    dis2 = (m+1) * (time-(m+1))
    if(dis1 < distance):
        r = m
        continue
    elif (dis1 >= distance and dis2 >= distance):
        l = m
        continue
    else:
        end = m
        break

print(end-start+1)
