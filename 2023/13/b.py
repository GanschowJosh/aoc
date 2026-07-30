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
  currgr.append(list(line))

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

def full_test(grid, skip=None):
  for i in range(1, len(grid[0])):
    if check_vert(grid, i): 
      # print("vertical:", i)
      if (i,"v") == skip:
        continue
      return i, "v"
  for i in range(1, len(grid)):
    if check_hor(grid, i): 
      # print("horizontal:", i)
      if (i,"h") == skip:
        continue
      return i, "h"
  else:
    return None, None


def print_grid(grid):
  for row in grid:
    print("".join(row))
  
su=0
for grid in grids:
  print_grid(grid)
  original=full_test(grid)

  print("original:",original)

  found=False
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if (i,j)==(0,0): 
        pass
      if grid[i][j]=='#':
        grid[i][j]='.'
        ft,type=full_test(grid,original)
        if ft is not None:
          print(f"swapped {i} {j} to '.' now reflect {(ft,type)}")
          print_grid(grid)
          if type == "h": ft *= 100
          su+=ft
          found=True
        grid[i][j]='#'
        if found: break
      else:
        grid[i][j]='#'
        ft,type=full_test(grid,original)
        if ft is not None:
          print(f"swapped {i} {j} to '.' now reflect {(ft,type)}")
          print_grid(grid)
          if type=="h": ft *=100
          su+=ft
          found=True
        grid[i][j]='.'
        if found: break
    if found: break



print(su)