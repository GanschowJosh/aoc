from collections import defaultdict
with open(input(), 'r') as f:
  lines=f.readlines()

graph=defaultdict(list)
for line in lines:
  a,b=line.strip().split("-")
  graph[a].append(b)
  graph[b].append(a)

seen=set()
for k in graph.keys():
  if k[0]!='t': continue
  for n in graph[k]:
    for nn in graph[n]:
      for nnn in graph[nn]:
        if nnn==k:
          o=tuple(sorted([k,n,nn]))
          #print(o)
          seen.add(o)
print(len(seen))