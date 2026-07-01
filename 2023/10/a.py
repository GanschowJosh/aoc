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
if si<0 and t_map(si,sj,si-1,sj) and sj<m-1 and t_map(si,sj,si,sj+1):
  grid[si][sj]='7'


dists = [[-1]*m for _ in range(n)]
q=deque({(si,sj,0)})

while q:
  ci,cj,cd=q.popleft()
  #print(ci,cj,cd)
  if dists[ci][cj] != -1: continue
  dists[ci][cj]=cd
  icon=grid[ci][cj]
  if icon == "|":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))
  if icon == "-":
    a,b=t_map(ci,cj,ci,cj+1),t_map(ci,cj,ci,cj-1)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))
  if icon == "L":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci,cj+1)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))
  if icon == "J":
    a,b=t_map(ci,cj,ci-1,cj),t_map(ci,cj,ci,cj-1)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))
  if icon == "7":
    a,b=t_map(ci,cj,ci,cj-1),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))
  if icon == "F":
    a,b=t_map(ci,cj,ci,cj+1),t_map(ci,cj,ci+1,cj)
    if a is None or b is None: continue
    q.append((*a, cd+1))
    q.append((*b, cd+1))


mx=0
for row in dists:
  mx=max(max(row),mx)
print(mx)