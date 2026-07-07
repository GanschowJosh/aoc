from collections import defaultdict
with open(input(), 'r') as f:
  lines=f.readlines()

graph=defaultdict(set)
for line in lines:
  a,b=line.strip().split("-")
  graph[a].add(b)
  graph[b].add(a)

best=[]

def search(cl,can):
  global best

  if len(cl)+len(can)<=len(best):
    return

  if not can:
    if len(cl)>len(best):
      best=cl[:]
    return

  for v in list(can):
    search(cl+[v], can&graph[v])
    can.remove(v)

search([],set(graph.keys()))
print(",".join(sorted(best)))