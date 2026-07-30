from collections import deque
with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(line.strip()))


rows=len(grid)
cols=len(grid[0])



def sim(sr,sc,sd):
  energized=[bytearray(cols) for _ in range(rows)]
  st=(sr,sc,sd)
  q=deque({st})
  seen=set()
  while q:
    cr,cc,cd=q.popleft()
    energized[cr][cc]=1
    if (cr,cc,cd) in seen: continue
    seen.add((cr,cc,cd))

    curr_cell=grid[cr][cc]
    if curr_cell == '.':
      if cd=='r' and cc+1 < cols: q.append((cr,cc+1,cd))
      if cd=='l' and cc-1 >= 0: q.append((cr,cc-1,cd))
      if cd=='d' and cr+1 < rows: q.append((cr+1,cc,cd))
      if cd=='u' and cr-1 >= 0: q.append((cr-1,cc,cd))
    if curr_cell == '/':
      if cd=='r' and cr-1 >= 0: q.append((cr-1,cc,'u'))
      if cd=='l' and cr+1 < rows: q.append((cr+1,cc,'d'))
      if cd=='d' and cc-1 >= 0: q.append((cr,cc-1,'l'))
      if cd=='u' and cc+1 < cols: q.append((cr,cc+1,'r'))
    if curr_cell == '\\':
      if cd=='r' and cr+1 < rows: q.append((cr+1,cc,'d'))
      if cd=='l' and cr-1 >= 0: q.append((cr-1,cc,'u'))
      if cd=='d' and cc+1 < cols: q.append((cr,cc+1,'r'))
      if cd=='u' and cc-1 >= 0: q.append((cr,cc-1,'l'))
    if curr_cell == '|':
      if cd in ('r', 'l'):
        if cr+1 < rows: q.append((cr+1,cc,'d'))
        if cr-1 >= 0: q.append((cr-1,cc,'u'))
      if cd=='d' and cr+1 < rows: q.append((cr+1,cc,cd))
      if cd=='u' and cr-1 >= 0: q.append((cr-1,cc,cd))
    if curr_cell == '-':
      if cd=='r' and cc+1 < cols: q.append((cr,cc+1,cd))
      if cd=='l' and cc-1 >= 0: q.append((cr,cc-1,cd))
      if cd in ('u', 'd'):
        if cc+1 < cols: q.append((cr,cc+1,'r'))
        if cc-1 >= 0: q.append((cr,cc-1,'l'))
  return sum(sum(j for j in i) for i in energized)


best=0
for i in (0,rows-1):
  for j in range(cols):
    c=sim(i,j,('d' if i==0 else 'u'))
    best=max(c,best)

for j in (0, cols-1):
  for i in range(rows):
    c=sim(i,j,('r' if j==0 else 'l'))
    best=max(c,best)

print(best)