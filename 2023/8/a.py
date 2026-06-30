from collections import defaultdict
import re

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

for src, left, right in nds:
  assert src not in graph
  graph[src]=(left, right)

curr="AAA"
cnt=0
while curr != "ZZZ":
  cd=dirs[cnt%len(dirs)]
  cnode=graph[curr]
  curr=cnode[dm[cd]]
  cnt+=1
print(cnt)