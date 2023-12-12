file1 = open('input', 'r')
lines = file1.readlines()

sum = 0
digits = []
for line in lines:
    for c in line:
        if c.isdigit():
            digits.append(c)
    sum = sum + int(digits[0]+digits[-1])
    digits = []
print(sum)