from collections import defaultdict
from math import sqrt
from itertools import combinations

dist = lambda a,b:sqrt(pow(b[0]-a[0],2)+pow(b[1]-a[1],2))

with open(input(), 'r') as f:
  lines = f.readlines()


valid = set('abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'1234567890')

diagram = []
for line in lines:
  diagram.append(list(line.strip()))


locs = defaultdict(list)
rows, cols = len(diagram), len(diagram[0])
for i in range(rows):
  for j in range(cols):
    cell_val = diagram[i][j]
    if cell_val in valid: locs[cell_val].append((i,j))

print(locs)
found = set()
for freq, positions in locs.items():
  for (r1, c1), (r2, c2) in combinations(positions, 2):
    dr = r2-r1
    dc = c2-c1

    ar1, ac1 = r1-dr, c1-dc #beyond (r1,c1), opposite side from (r2,c2)
    ar2, ac2 = r2+dr, c2+dc #beyond (r2,c2), opposite side from (r1,c1)

    if 0 <= ar1 < rows and 0 <= ac1 < cols: found.add((ar1, ac1))
    if 0 <= ar2 < rows and 0 <= ac2 < cols: found.add((ar2, ac2))


print(found)
print(len(found))