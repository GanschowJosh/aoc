with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(line.strip()))


def rot_n(grid):
  l=len(grid)
  c=len(grid[0])
  for i in range(1, l):
    for j in range(c):
      if grid[i][j]!='O': continue
      ii=i
      while ii>0 and grid[ii-1][j] =='.':
        ii-=1
      if ii==i: continue
      grid[ii][j]='O'
      grid[i][j]='.'
      

def rot_e(grid):
  l=len(grid)
  c=len(grid[0])
  for j in range(c-2,-1,-1):
    for i in range(l):
      if grid[i][j]!='O': continue
      jj=j
      while jj<c-1 and grid[i][jj+1]=='.':
        jj+=1
      if jj==j: continue
      grid[i][jj]='O'
      grid[i][j]='.'
      

def rot_s(grid):
  l=len(grid)
  c=len(grid[0])
  for i in range(l-2,-1,-1):
    for j in range(c):
      if grid[i][j]!='O': continue
      ii=i
      while ii < l-1 and grid[ii+1][j]=='.':
        ii+=1
      if ii==i: continue
      grid[ii][j]='O'
      grid[i][j]='.'


def rot_w(grid):
  l=len(grid)
  c=len(grid[0])
  for j in range(1,c):
    for i in range(l):
      if grid[i][j]!='O': continue
      jj=j
      while jj>0 and grid[i][jj-1]=='.':
        jj-=1
      if jj==j: continue
      grid[i][jj]='O'
      grid[i][j]='.'


cycles=1_000_000_000

def encode(grid):
  return tuple(map(tuple, grid))

seen={encode(grid): 0}

curr_c = 0

while curr_c < cycles:
  curr_c+=1
  rot_n(grid)
  rot_w(grid)
  rot_s(grid)
  rot_e(grid)
  e=encode(grid)
  if e in seen:
    remaining=cycles-curr_c
    diff=curr_c-seen[e]
    curr_c+=(remaining//diff)*diff
  else:
    seen[e]=curr_c


tot=0
l=len(grid)
c=len(grid[0])
for i in range(l):
  for j in range(c):
    if grid[i][j]=='O': tot+=(l-i)

print(tot)