input = []

with open('./input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split()
        input.append(numbers)

def isSafe(l):
    increasing = 1 if int(l[1]) > int(l[0]) else -1
    for i in range(1,len(l)):
        diff = (int(l[i]) - int(l[i-1])) * increasing
        if diff >= 1 and diff <= 3:
            continue
        return False
    return True

def isSafeWithDampener(l):
    for i in range(len(l)):
        new_l = l[:i] + l[i+1:]
        if isSafe(new_l):
            return True
    return False

res = 0
res2 = 0

for line in input:
    if isSafe(line):
        res += 1
        res2 += 1
    elif isSafeWithDampener(line):
        res2 += 1

print(res)
print(res2)

