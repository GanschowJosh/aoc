from collections import deque
with open(input(), 'r') as f:
  lines=f.readlines()

rows,cols=len(lines), len(lines[0])-1

gr=[]
vis=[]
ot=[]
si,sj=None,None
for i,line in enumerate(lines):
  line=line.strip()
  l=bytearray(line, 'ascii')
  gr.append(l)
  vis.append([[False]*10000 for _ in range(cols)])
  ot.append(bytearray(len(line)))
  if ord('S') in l:
    si,sj=i,l.index(ord('S'))

# print(gr,si,sj)
MX=64

ot[si][sj]=1


q=deque([(si,sj,0)])#i,j,steps
while q:
  ci,cj,cd=q.popleft()
  if cd == MX:
    ot[ci][cj]=1
    gr[ci][cj]=ord('O')
    continue
  for di,dj in [(-1,0),(0,-1),(0,1),(1,0)]:
    ni,nj=di+ci,dj+cj
    if 0 > ni or ni >= rows or 0 > nj or nj >= cols:
      continue
    if gr[ni][nj]!=ord('.'): continue
    if vis[ni][nj][cd+1]: continue
    vis[ni][nj][cd+1]=True
    q.append((ni,nj,cd+1))

su=0
for row in ot:
  su+=sum(row)

print(su)
# for row in gr:
#   print(row)