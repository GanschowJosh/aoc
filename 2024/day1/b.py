f = open("input.txt", "r")
lines = f.readlines()
f.close()

from collections import defaultdict

left = []
right_occurrences = defaultdict(int)

for i in range(len(lines)):
    line = lines[i].strip()
    l, r = line.split()
    left.append(int(l))
    right_occurrences[int(r)] += 1

left.sort()

score = 0
for num in left:
    score += right_occurrences[num] * num

print(score)