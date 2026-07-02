from itertools import combinations
import heapq
extend=1_000_000
with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(line.strip()))

n,m=len(grid),len(grid[0])

newgr=[]
for row in grid:
  if all(r=='.' for r in row):
    newgr.append([extend for _ in range(m)])
  else:
    newgr.append([1 for _ in range(m)])



tr=0
for i in range(len(grid[0])):
  if all(grid[x][i]=='.'for x in range(len(grid))):
    for j,row in enumerate(newgr):
      newgr[j][i]*=extend
    tr+=1

og_grid=grid

gals=[]
n,m=len(grid),len(grid[0])
for i in range(n):
  for j in range(m):
    if grid[i][j]=='#': gals.append((i,j))

neighbors=[
  [-1,0],
  [0,-1],[0,1],
  [1,0]
]
su=0
INF=10**20
for (x1,y1),(x2,y2) in combinations(gals,2):
  pq=[(0,(x1,y1))]
  v=[[INF]*m for _ in range(n)]
  v[x1][x2]=0
  while pq:
    cc,(ci,cj)=heapq.heappop(pq)
    if (ci, cj) == (x2,y2):
      su+=cc
      break
    for di,dj in neighbors:
      ni,nj=di+ci,dj+cj
      if ni<0 or ni>=n or nj<0 or nj>=m: continue
      tc=cc+newgr[ni][nj]
      if not v[ni][nj] or tc<v[ni][nj]:
        v[ni][nj]=tc
        heapq.heappush(pq,(tc,(ni,nj)))
    

print(su)