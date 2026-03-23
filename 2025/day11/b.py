from collections import defaultdict
from copy import deepcopy
from functools import cache
with open(input(), 'r') as f:
  lines = f.readlines()

graph = defaultdict(list)

for line in lines:
  a, conns = line.split(": ")
  conns = conns.split()
  graph[a].extend(conns)

print("graph made")

@cache
def dfs(a, fft, dac):
  fft = fft or (a=='fft')
  dac = dac or (a=='dac')
  if a == 'out':
    return 1 if (fft and dac) else 0
  return sum(dfs(b, fft, dac) for b in graph[a])

out = dfs('svr', False, False)

print(out)