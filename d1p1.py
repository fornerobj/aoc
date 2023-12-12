file1 = open('input', 'r')
lines = file1.readlines()

def fun(line):
    digits = []
    for i in range (len(line)):
        if(line[i].isdigit()):
            digits.append(line[i])
        for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if(line[i::].startswith(val)):
                digits.append(str(j+1))
    return digits

sum = 0
for line in lines:
    digits = fun(line)
    sum = sum + int(digits[0] + digits[-1])

print(sum)