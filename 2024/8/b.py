from collections import defaultdict
from math import sqrt, gcd
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
    g = gcd(abs(dr), abs(dc))#smallest step
    dr //= g
    dc //= g
    r, c = r1, c1
    while 0 <= r < rows and 0 <= c < cols:
      found.add((r,c))
      r+=dr
      c+=dc
    r,c=r1-dr,c1-dc
    while 0<=r<rows and 0<=c<cols:
      found.add((r,c))
      r-=dr
      c-=dc
    
    


print(found)
print(len(found))