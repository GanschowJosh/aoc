from itertools import combinations
with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(line.strip()))

newgr=[]
for row in grid:
  newgr.append(row)
  if all(r=='.' for r in row):
    newgr.append(row)


tr=0
for i in range(len(grid[0])):
  if all(grid[x][i]=='.'for x in range(len(grid))):
    for j,row in enumerate(newgr):
      newgr[j]=row[:i+tr]+['.']+row[i+tr:]
    tr+=1

og_grid=grid
grid=newgr

gals=[]
n,m=len(grid),len(grid[0])
for i in range(n):
  for j in range(m):
    if grid[i][j]=='#': gals.append((i,j))

su=0
for (x1,y1),(x2,y2) in combinations(gals,2):
  # print(x1,y1,x2,y2,abs(x2-x1)+abs(y2-y1))
  su+=(abs(x2-x1)+abs(y2-y1))

print(su)