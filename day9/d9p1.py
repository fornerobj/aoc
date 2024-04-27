with open("input") as f:
    lines = f.readlines()

def fun(l):
    ans = 0
    while(sum(l) != 0):
        ans += l[-1]
        nl = []
        for i in range(1, len(l)):
            nl.append(l[i]-l[i-1])
        l = nl
    return ans

res = []
for line in lines:
    nums = list(map(int, line.split()))
    res.append(fun(nums))

print(sum(res))
    
