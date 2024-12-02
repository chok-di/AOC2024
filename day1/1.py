from collections import Counter

left, right = [],[]
distance, similarity = 0, 0

with open('./input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
left.sort()
right.sort()

right_frequency = dict(Counter(right))

for i in range(len(left)):
    distance += abs(left[i] - right[i])
    similarity += left[i] * right_frequency.get(left[i],0)
    
print(distance)
print(similarity)
