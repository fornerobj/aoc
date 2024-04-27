with open("input") as f:
    lines = f.readlines()

def fun(l):
    stack = []
    while(sum(l) != 0):
        stack.append(l[0])
        nl = []
        for i in range(1, len(l)):
            nl.append(l[i]-l[i-1])
        l = nl
    ans = stack.pop()
    while(stack):
        ans = stack.pop()-ans
    return ans

res = []
for line in lines:
    nums = list(map(int, line.split()))
    res.append(fun(nums))

print(sum(res))
    
