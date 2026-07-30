import heapq
from itertools import count

with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(map(int, line.strip())))

rows,cols=len(grid),len(grid[0])

dirs=[('r', 0, 1), ('l', 0, -1), ('d', 1,0),('u',-1,0)]
opposite={
  'r':'l',
  'l':'r',
  'd':'u',
  'u':'d'
}

best={}

q=[]
start=(0,0,(0,None))
best[start]=0
heapq.heappush(q,(0,0,0,(0,None)))

while q:
  chl,cr,cc,(runlen,rundir)=heapq.heappop(q)
  state=(cr,cc,(runlen,rundir))

  if chl != best[state]: continue

  if (cr,cc)==(rows-1,cols-1):
    endstate=state
    break

  for d,dr,dc in dirs:
    if rundir != None and d == opposite[rundir]: continue
    if rundir == d:
      newlen=runlen+1
      if newlen>3: continue
    else:
      newlen=1

    nr=dr+cr
    nc=dc+cc
    if 0 > nr or nr >= rows or 0 > nc or nc >= cols: continue

    newhl=chl+grid[nr][nc]
    newstate=(nr,nc,(newlen,d))

    if newhl >= best.get(newstate,10**10): continue

    best[newstate]=newhl
    heapq.heappush(q,(newhl,nr,nc,(newlen,d)))

print(chl)