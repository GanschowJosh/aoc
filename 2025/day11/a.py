from collections import defaultdict
with open(input(), 'r') as f:
  lines = f.readlines()

graph = defaultdict(list)

for line in lines:
  a, conns = line.split(": ")
  conns = conns.split()
  graph[a].extend(conns)

def dfs(a, graph):
  if a == 'out': return 1
  return sum(dfs(b, graph) for b in graph[a])

print(dfs('you', graph))