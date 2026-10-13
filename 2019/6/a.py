from collections import defaultdict
with open(input(),'r') as f:
  lines=f.readlines()

graph=defaultdict(list)

for line in lines:
  a,b=line.strip().split(')')
  graph[a].append(b)

def dfs(a,carry):
  return carry+sum(dfs(b,carry+1) for b in graph[a])

print(dfs('COM',0))