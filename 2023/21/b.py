from collections import deque
with open(input(), 'r') as f:
  lines=f.readlines()

rows,cols=len(lines), len(lines[0])-1

gr=[]
si,sj=None,None
for i,line in enumerate(lines):
  line=line.strip()
  l=bytearray(line, 'ascii')
  gr.append(l)
  if ord('S') in l:
    si,sj=i,l.index(ord('S'))

def count(MX):


  found = set([])

  vis=set([(si,sj,0)])

  q=deque([(si,sj,0)])#i,j,steps
  while q:
    ci,cj,cd=q.popleft()
    # print(ci,cj,cd)
    if cd == MX:
      found.add((ci,cj))
      continue
    for di,dj in [(-1,0),(0,-1),(0,1),(1,0)]:
      ni,nj=di+ci,dj+cj
      tni=ni%rows
      tnj=nj%cols
      if gr[tni][tnj] not in (ord('.'),ord('S')): continue
      if (ni,nj,cd+1) in vis: continue
      vis.add((ni,nj,cd+1))
      q.append((ni,nj,cd+1))
  return len(found)

f0=count(65)
f1=count(196)
f2=count(327)
k=202300
d1=f1-f0
d2=f2-2*f1+f0
print(f0+k*d1+k*(k-1)//2*d2)