from collections import defaultdict
from itertools import combinations
from math import sqrt, prod
with open(input(), 'r') as f:
  lines = f.readlines()

def dist(a, b):
  x1,y1,z1 = a
  x2,y2,z2 = b
  x=(x2-x1)**2
  y=(y2-y1)**2
  z=(z2-z1)**2
  return sqrt(x+y+z)

coords = list(map(str.strip, lines))
for i, coord in enumerate(coords):
  coords[i] = tuple(map(int, coord.split(",")))
# print(coords)

dists = {}

for a, b in combinations(coords, 2):
  dists[tuple(sorted((tuple(a),tuple(b))))] = dist(a,b)
srt = sorted(dists.items(),key=lambda x: x[1])
# print(srt)


circuits = {}
for i, c in enumerate(coords):
  circuits[tuple(c)] = i
while not len(set(circuits.values())) == 1:
  curr = srt.pop(0)
  a,b,d = curr[0][0],curr[0][1],curr[1]
  if circuits[a] == circuits[b]: continue
  else: 
    old = circuits[b]
    new = circuits[a]
    for k,v in circuits.items():
      if v == old: circuits[k] = new
    circuits[b] = circuits[a]
    last = (a,b)

print(last)
print(last[0][0]*last[1][0])

# print(circuits)
# s = defaultdict(int)
# for k, v in circuits.items():
#   s[v] += 1
# # print(s)
# top = sorted(s.values(), reverse=True)[:3]
# print(prod(top))