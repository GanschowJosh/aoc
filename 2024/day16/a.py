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
  maze.append(line)

n,m=len(maze),len(maze[0])

for i in range(n):
  for j in range(m):
    if maze[i][j]=='S': si,sj=i,j
    if maze[i][j]=='E': ei,ej=i,j




q=[(0,si,sj,'E')]#score,i,j,facing
heapq.heapify(q)
best=[[float('inf')]*m for _ in range(n)]
best[si][sj]=0
while q:
  c, ci, cj, cf = heapq.heappop(q)
  i=ci-1
  if i >= 0 and maze[i][cj] != "#":
    mult=0 if cf=='N' else 1000
    nxt=c+1+mult
    if best[i][cj]>nxt:
      best[i][cj]=nxt
      heapq.heappush(q, (nxt,i,cj,'N'))
  i=ci+1
  if i < n and maze[i][cj] != '#':
    mult=0 if cf=='S' else 1000
    nxt=c+1+mult
    if best[i][cj]>nxt:
      best[i][cj]=nxt
      heapq.heappush(q, (nxt,i,cj,'S'))
  j=cj-1
  if j >= 0 and maze[ci][j] != '#':
    mult=0 if cf=='W' else 1000
    nxt=c+1+mult
    if best[ci][j]>nxt:
      best[ci][j]=nxt
      heapq.heappush(q, (nxt,ci,j,'W'))
  j=cj+1
  if j < m and maze[ci][j] != '#':
    mult=0 if cf == 'E' else 1000
    nxt=c+1+mult
    if best[ci][j]>nxt:
      best[ci][j]=nxt
      heapq.heappush(q, (nxt,ci,j,'E'))

#print_matrix(best)
print(best[ei][ej])