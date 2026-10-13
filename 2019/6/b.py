from math import ceil, log
from collections import defaultdict, deque
with open(input(),'r') as f:
  lines=f.readlines()


v=set()
graph=defaultdict(list)
parent=defaultdict(str)
mp={}
curr = 0

for line in lines:
  a,b=line.strip().split(')')
  graph[a].append(b)
  parent[b]=a
  v.add(a)
  v.add(b)
parent['COM']='COM'


root='COM'

a = {}
d=0
c='YOU'
while True:
  a[c]=d
  if c==root: break
  c=parent[c]
  d+=1

d=0
c='SAN'
while c not in a:
  c=parent[c]
  d+=1

print(a[c]+d-2)