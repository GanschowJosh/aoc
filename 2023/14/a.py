with open(input(), 'r') as f:
  lines=f.readlines()

grid=[]
for line in lines:
  grid.append(list(line.strip()))


l=len(grid)
c=len(grid[0])
for _ in range(l):
  for i in range(1, l):
    for j in range(c):
      if grid[i][j]!='O': continue
      if grid[i-1][j]!='.': continue
      grid[i-1][j]='O'
      grid[i][j]='.'

for row in grid:
  print("".join(row))


tot=0
for i in range(l):
  for j in range(c):
    if grid[i][j]=='O': tot+=(l-i)

print(tot)