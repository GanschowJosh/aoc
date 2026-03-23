f = open("input.txt", "r")
lines = f.readlines()
f.close()

left = []
right = []

for i in range(len(lines)):
    line = lines[i].strip()
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total = 0
for i, j in zip(left, right):
    total += max(i, j) - min(i, j)

print(total)