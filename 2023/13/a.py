with open(input(), 'r') as f:
  lines=f.readlines()

grids=[]
currgr=[]
for line in lines:
  line=line.strip()
  if len(line) == 0:
    if currgr: grids.append(currgr)
    currgr=[]
    continue
  currgr.append(line)

if currgr:
  grids.append(currgr)

def check_vert(grid, idx):
  l=len(grid[0])
  good=True
  for i in range(1, min(idx, l-idx)+1):
    lcol=idx-i
    rcol=idx+i-1
    for j in range(len(grid)):
      if grid[j][lcol] != grid[j][rcol]: 
        good=False
        break
    if not good: break
  return good

def check_hor(grid, idx):
  l=len(grid)
  good=True
  for i in range(1, min(idx, l-idx)+1):
    trow=idx-i
    brow=idx+i-1
    for j in range(len(grid[0])):
      if grid[trow][j] != grid[brow][j]:
        good=False
        break
    if not good: break
  return good

su=0
for grid in grids:
  for row in grid:
    print(row)
  for i in range(1, len(grid[0])):
    if check_vert(grid, i): 
      print("vertical:", i)
      su+=i
  for i in range(1, len(grid)):
    if check_hor(grid, i): 
      print("horizontal:", i)
      su+=(100*i)


print(su)