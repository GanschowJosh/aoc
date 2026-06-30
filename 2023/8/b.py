from collections import defaultdict
import re
from math import lcm

with open(input(), 'r') as f:
  lines=f.readlines()

dirs=lines[0].strip()
dm = {
  "L": 0,
  "R": 1
}

nds=[]
for line in lines[2:]:
  m=re.match(r'(?P<node>\w+) = \((?P<left>\w+), (?P<right>\w+)\)', line.strip())
  nds.append((m["node"], m["left"], m["right"]))

graph = defaultdict(tuple)

starts=[]

for src, left, right in nds:
  assert src not in graph
  graph[src]=(left, right)
  if src[-1]=='A': starts.append(src)

reaches=[]
for st in starts:
  cnt=0
  curr=st
  while curr[-1]!='Z':
    cd=dm[dirs[cnt%len(dirs)]]
    curr=graph[curr][cd]
    cnt+=1
  reaches.append(cnt)

print(lcm(*reaches))