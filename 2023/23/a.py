with open(input(),'r') as f:
  lines=f.readlines()

from collections import deque
from copy import copy


gr=[]
og=[]
for line in lines:
  r=line.strip()
  gr.append(bytearray(r, 'ascii'))
  og.append(bytearray(r, 'ascii'))

n,m=len(gr),len(gr[0])

PATH=ord('.')
FOREST=ord('#')
SLOPE_UP=ord('^')
SLOPE_DOWN=ord('v')
SLOPE_LEFT=ord('<')
SLOPE_RIGHT=ord('>')
SLOPES=[SLOPE_DOWN,SLOPE_UP,SLOPE_LEFT,SLOPE_RIGHT]

si,sj=0,None
for i in range(len(gr[0])):
  if gr[0][i]==PATH: sj=i

ei,ej=len(gr)-1,None
for i in range(len(gr[0])):
  if gr[len(gr)-1][i]==PATH: ej=i

# seen=[[False]*m for _ in range(n)]
# seen[si][sj]=True

mx=0
q=deque([(si,sj,0,set())])#i,j,dist
while q:
  ci,cj,cd,seen=q.popleft()
  og[ci][cj]=ord('O')
  if ci==ei and cj==cj:
    mx=max(mx, cd)
    continue

  seen=copy(seen)

  if gr[ci][cj] == SLOPE_DOWN:
    if (ci+1,cj) in seen: continue
    seen.add((ci+1,cj))
    q.append((ci+1,cj,cd+1,seen))
  if gr[ci][cj] == SLOPE_UP:
    if (ci-1,cj) in seen: continue
    seen.add((ci-1,cj))
    q.append((ci-1,cj,cd+1,seen))
  if gr[ci][cj] == SLOPE_LEFT:
    if (ci,cj-1) in seen: continue
    seen.add((ci,cj-1))
    q.append((ci,cj-1,cd+1,seen))
  if gr[ci][cj] == SLOPE_RIGHT:
    if (ci,cj+1) in seen: continue
    seen.add((ci,cj+1))
    q.append((ci,cj+1,cd+1,seen))

  for di,dj in [(-1,0),(0,1),(1,0),(0,-1)]:
    ni,nj=di+ci,dj+cj
    if 0 > ni or ni >= n or 0 > nj or nj >= m: continue
    if gr[ni][nj]==FOREST: continue
    if (ni,nj) in seen: continue
    seen.add((ni,nj))
    q.append((ni,nj,cd+1,seen))

print(mx)
# for row in og:
#   print(row)