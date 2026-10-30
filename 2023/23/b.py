with open(input(),'r') as f:
  lines=f.readlines()


gr=[]
og=[]
for line in lines:
  r=line.strip()
  gr.append(bytearray(r, 'ascii'))
  og.append(bytearray(r, 'ascii'))

n,m=len(gr),len(gr[0])

from collections import defaultdict

PATH=ord('.')
FOREST=ord('#')
SLOPE_UP=ord('^')
SLOPE_DOWN=ord('v')
SLOPE_LEFT=ord('<')
SLOPE_RIGHT=ord('>')
SLOPES=[SLOPE_DOWN,SLOPE_UP,SLOPE_LEFT,SLOPE_RIGHT]

for i in range(n):
  for j in range(m):
    if gr[i][j] in SLOPES: gr[i][j]=PATH

si,sj=0,None
for i in range(len(gr[0])):
  if gr[0][i]==PATH: sj=i

ei,ej=len(gr)-1,None
for i in range(len(gr[0])):
  if gr[len(gr)-1][i]==PATH: ej=i

def neighbors(pos):
  i, j = pos
  for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    ni, nj = i + di, j + dj
    if 0 <= ni < n and 0 <= nj < m and gr[ni][nj] == PATH:
      yield ni, nj

start = (si, sj)
end = (ei, ej)

adj = {(i,j): list(neighbors((i, j))) for i in range(n) for j in range(m) if gr[i][j] == PATH}

junctions = {pos for pos, edges in adj.items() if len(edges) != 2} | {start, end}

j_graph = defaultdict(list)

for source in junctions:
  for first in adj[source]:
    prev, curr = source, first
    distance = 1
    while curr not in junctions:
      a, b = adj[curr]
      if a == prev: nxt=b
      else: nxt=a
      prev, curr = curr, nxt
      distance += 1
    j_graph[source].append((curr, distance))

mx = 0
stack = [(start, 0, {start})]

while stack:
  curr, distance, seen = stack.pop()
  if curr == end:
    mx = max(mx, distance)
    continue
  for nxt, weight in j_graph[curr]:
    if nxt not in seen:
      stack.append((nxt, distance + weight, seen | {nxt}))

print(mx)