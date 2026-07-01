from collections import deque

with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for i,line in enumerate(lines):
  grid.append(list(line.strip()))
  if 'S' in line:
    si,sj=i,line.index('S')
n,m=len(grid),len(grid[0])

def t_map(si,sj,ii,ij):
  icon=grid[ii][ij]
  if icon=="|":
    if (ii-si==1 and ij==sj): return (ii, ij)
    if (ii-si==-1 and ij==sj): return(ii, sj)
    return None
  if icon=="-":
    if (ii==si and ij-sj==1): return (ii, ij)
    if (ii==si and ij-sj==-1): return(ii, ij)
    return None
  if icon=="L":
    if (ii-si==1 and ij==sj): return (ii,ij)
    if (ii==si and ij-sj==-1): return(ii,ij)
    return None
  if icon=="J":
    if(ii-si==1 and ij==sj): return (ii,ij)
    if(ii==si and ij-sj==1): return(ii,ij)
    return None
  if icon=="7":
    if(ii-si==-1 and ij==sj): return (ii,ij)
    if(ii==si and ij-sj==1): return (ii,ij)
    return None
  if icon=="F":
    if(ii-si==-1 and ij==sj): return (ii,ij)
    if(ii==si and ij-sj==-1): return (ii,ij)
  return None

if si>0 and t_map(si,sj,si-1,sj) and si<n-1 and t_map(si,sj,si+1,sj):
  grid[si][sj]='|'
if sj>0 and t_map(si,sj,si,sj-1) and sj<m-1 and t_map(si,sj,si,sj+1):
  grid[si][sj]='-'
if si>0 and t_map(si,sj,si-1,sj) and sj<m-1 and t_map(si,sj,si,sj+1):
  grid[si][sj]='L'
if si>0 and t_map(si,sj,si-1,sj) and sj>0 and t_map(si,sj,si,sj-1):
  grid[si][sj]='J'
if si<n-1 and t_map(si,sj,si+1,sj) and sj<m-1 and t_map(si,sj,si,sj+1):
  grid[si][sj]='F'
if si>0 and t_map(si,sj,si-1,sj) and sj<m-1 and t_map(si,sj,si,sj+1):
  grid[si][sj]='7'




route = [[0]*m for _ in range(n)]
q=deque({(si,sj)})

while q:
  ci,cj=q.popleft()
  #print(ci,cj,cd)
  if route[ci][cj]==1: continue
  route[ci][cj]=1
  icon=grid[ci][cj]
  if icon == "|":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)
  if icon == "-":
    a,b=t_map(ci,cj,ci,cj+1),t_map(ci,cj,ci,cj-1)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)
  if icon == "L":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci,cj+1)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)
  if icon == "J":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci,cj-1)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)
  if icon == "7":
    a,b=t_map(ci,cj,ci,cj-1),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)
  if icon == "F":
    a,b=t_map(ci,cj,ci,cj+1),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append(a)
    q.append(b)

#for row in route:
#  print(*row)

big = [[0]*(m*3) for _ in range(n*3)]

def mark(i,j,spots):
  bi,bj=i*3,j*3
  for di,dj in spots:
    big[bi+di][bj+dj]=1

for i in range(n):
  for j in range(m):
    if not route[i][j]:
      continue

    icon=grid[i][j]

    if icon=="|":
      mark(i,j,[(0,1),(1,1),(2,1)])
    if icon=="-":
      mark(i,j,[(1,0),(1,1),(1,2)])
    if icon=="L":
      mark(i,j,[(0,1),(1,1),(1,2)])
    if icon=="J":
      mark(i,j,[(0,1),(1,1),(1,0)])
    if icon=="7":
      mark(i,j,[(1,0),(1,1),(2,1)])
    if icon=="F":
      mark(i,j,[(1,2),(1,1),(2,1)])

bn,bm=n*3,m*3
seen=[[0]*bm for _ in range(bn)]
q=deque()

for i in range(bn):
  for j in [0,bm-1]:
    if big[i][j]==0 and not seen[i][j]:
      q.append((i,j))

for j in range(bm):
  for i in [0,bn-1]:
    if big[i][j]==0 and not seen[i][j]:
      q.append((i,j))

dirs=[(-1,0),(1,0),(0,-1),(0,1)]

while q:
  ci,cj=q.popleft()
  if seen[ci][cj]:
    continue
  seen[ci][cj]=1

  for di,dj in dirs:
    ni,nj=ci+di,cj+dj
    if ni<0 or ni>=bn or nj<0 or nj>=bm:
      continue
    if seen[ni][nj] or big[ni][nj]:
      continue
    q.append((ni,nj))

cnt=0

for i in range(n):
  for j in range(m):
    if route[i][j]:
      continue

    ci,cj=i*3+1,j*3+1

    if not seen[ci][cj]:
      cnt+=1

print(cnt)