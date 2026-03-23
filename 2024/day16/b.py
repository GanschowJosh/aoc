from collections import defaultdict, deque
from copy import deepcopy
import heapq

def print_matrix(matrix):
  m=max(len(str(matrix[i][j])) for i in range(len(matrix)) for j in range(len(matrix[0])))
  for row in matrix:
    for i, val in enumerate(row):
      print(str(val).ljust(m, " "), end=" \n"[i==len(row)-1])
with open(input(), 'r') as f:
  lines=f.readlines()

maze=[]
for line in lines:
  line=line.strip()
  maze.append(list(line))

n,m=len(maze),len(maze[0])

for i in range(n):
  for j in range(m):
    if maze[i][j]=='S': si,sj=i,j
    if maze[i][j]=='E': ei,ej=i,j



parents=defaultdict(list)
q=[(0,si,sj,'E')]#score,i,j,facing
heapq.heapify(q)
best=defaultdict(lambda:float('inf'))
best[(si,sj,'E')]=0
while q:
  c, ci, cj, cf = heapq.heappop(q)
  if c > best[(ci,cj,cf)]: continue
  i=ci-1
  if i >= 0 and maze[i][cj] != "#":
    mult=0 if cf=='N' else (2000 if cf=='S' else 1000)
    nxt=c+1+mult
    if best[(i,cj,'N')]>=nxt:
      if best[(i,cj,'N')]>nxt: parents[(i,cj,'N')]=[]
      best[(i,cj,'N')]=nxt
      parents[(i,cj,'N')].append((ci,cj,cf))
      heapq.heappush(q, (nxt,i,cj,'N'))
  i=ci+1
  if i < n and maze[i][cj] != '#':
    mult=0 if cf=='S' else (2000 if cf=='N' else 1000)
    nxt=c+1+mult
    if best[(i,cj,'S')]>=nxt:
      if best[(i,cj,'S')]>nxt: parents[(i,cj,'S')]=[]
      best[(i,cj,'S')]=nxt
      parents[(i,cj,'S')].append((ci,cj,cf))
      heapq.heappush(q, (nxt,i,cj,'S'))
  j=cj-1
  if j >= 0 and maze[ci][j] != '#':
    mult=0 if cf=='W' else (2000 if cf=='E' else 1000)
    nxt=c+1+mult
    if best[(ci,j,'W')]>=nxt:
      if best[(ci,j,'W')]>nxt: parents[(ci,j,'W')]=[]
      best[(ci,j,'W')]=nxt
      parents[(ci,j,'W')].append((ci,cj,cf))
      heapq.heappush(q, (nxt,ci,j,'W'))
  j=cj+1
  if j < m and maze[ci][j] != '#':
    mult=0 if cf=='E' else (2000 if cf=='W' else 1000)
    nxt=c+1+mult
    if best[(ci,j,'E')]>=nxt:
      if best[(ci,j,'E')]>nxt: parents[(ci,j,'E')]=[]
      best[(ci,j,'E')]=nxt
      parents[(ci,j,'E')].append((ci,cj,cf))
      heapq.heappush(q, (nxt,ci,j,'E'))

end_cost=min(best[(ei,ej,d)] for d in 'NSEW')
print(end_cost)
paths=deepcopy(maze)
q=deque()
seen=set()
for d in 'NSEW':
  if best[(ei,ej,d)]==end_cost:
    q.append((ei,ej,d))
    seen.add((ei,ej,d))
while q:
  ci,cj,cf=q.popleft()
  paths[ci][cj]='O'
  for pi,pj,pf in parents[(ci,cj,cf)]:
    if (pi,pj,pf) not in seen:
      seen.add((pi,pj,pf))
      q.append((pi,pj,pf))
s=sum(paths[i][j]=='O' for i in range(n) for j in range(m))
print(s)
print_matrix(paths)