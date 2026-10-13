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
  if a not in mp:
    mp[a]=curr
    curr+=1
  if b not in mp:
    mp[b]=curr
    curr+=1
  v.add(a)
  v.add(b)
parent['COM']='COM'

def find_ht(i):
  return 1+max([find_ht(j) for j in graph[i]]+[0])
ht=find_ht('COM')


root='COM'

LOG=ceil(log(ht,2))

up=[[root]*LOG for _ in range(len(v))]
depth=defaultdict(int)

stack=[(root,root)]
while stack:
  v,p=stack.pop()
  up[mp[v]][0] = p
  for k in range(1,LOG):
    up[mp[v]][k]=up[mp[up[mp[v]][k-1]]][k-1]

  for child in graph[v]:
    if child==p: continue
    depth[child]=depth[v]+1
    stack.append((child,v))

def lca(u,v):
  if depth[u]<depth[v]:
    u,v=v,u

  diff=depth[u]-depth[v]
  for k in range(LOG):
    if diff & (1<<k):
      u=up[mp[u]][k]
  if u == v:
    return u

  for k in range(LOG-1,-1,-1):
    if up[mp[u]][k]!=up[mp[v]][k]:
      u=up[mp[u]][k]
      v=up[mp[v]][k]
  return up[mp[u]][0]

def dist(u,v):
  return depth[u]+depth[v]-2*depth[lca(u,v)]

print(dist('YOU','SAN')-2)