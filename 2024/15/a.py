with open(input(), "r") as f:
  lines=f.readlines()



WALL="#"
BOX="O"
ROBOT="@"
EMPTY="."

ongrid=True
grid=[]
moves=""
for i,line in enumerate(lines):
  line=line.strip()
  if not line: ongrid=False;continue
  if ongrid:
    grid.append(list(line))
    if ROBOT in line:
      rx,ry=i,line.index(ROBOT)
  else:
    moves+=line

rows, cols = len(grid), len(grid[0])


def shift_right(row, start_idx):
  for i in range(cols-2, start_idx-1, -1):
    if row[i+1] in (WALL, BOX): continue
    push=True
    s=i-1
    while s > start_idx:
      if row[s] in (WALL, EMPTY): push=False
      s-=1
    if push and row[i]==BOX:
      row[i+1]=row[i]
      row[i]=EMPTY

def shift_left(row, start_idx):
  for i in range(1, start_idx):
    if row[i-1] in (WALL, BOX): continue
    push=True
    s=i+1
    while s < start_idx:
      if row[s] in (WALL, EMPTY): push=False
      s+=1
    if push and row[i]==BOX:
      row[i-1]=row[i]
      row[i]=EMPTY

def shift_down(col_num, start_idx):
  gr=grid
  for i in range(rows-2, start_idx-1, -1):
    if gr[i+1][col_num] in (WALL, BOX): continue
    push=True
    s=i-1
    while s > start_idx:
      if gr[s][col_num] in (WALL, EMPTY): push=False
      s-=1
    if push and gr[i][col_num]==BOX:
      gr[i+1][col_num]=gr[i][col_num]
      gr[i][col_num]=EMPTY

def shift_up(col_num, start_idx):
  gr=grid
  for i in range(1, start_idx):
    if gr[i-1][col_num] in (WALL, BOX): continue
    push=True
    s=i+1
    while s < start_idx:
      if gr[s][col_num] in (WALL, EMPTY): push=False
      s+=1
    if push and gr[i][col_num]==BOX:
      gr[i-1][col_num]=gr[i][col_num]
      gr[i][col_num]=EMPTY

def find_robot():
  gr=grid
  for i in range(rows):
    for j in range(cols):
      if gr[i][j] == ROBOT: return (i,j)

def print_grid():
  gr=grid
  for i in range(rows):
    for j in range(cols):
      print(gr[i][j], end="")
    print()
  print()

for command in moves:
  if command=="<":
    shift_left(grid[rx], ry)
    if grid[rx][ry-1]==EMPTY:
      grid[rx][ry-1]=ROBOT
      grid[rx][ry]=EMPTY
      rx,ry=rx,ry-1
  if command==">":
    shift_right(grid[rx],ry)
    if grid[rx][ry+1]==EMPTY:
      grid[rx][ry+1]=ROBOT
      grid[rx][ry]=EMPTY
      rx,ry=rx,ry+1
  if command=="^":
    shift_up(ry, rx)
    if grid[rx-1][ry]==EMPTY:
      grid[rx-1][ry]=ROBOT
      grid[rx][ry]=EMPTY
      rx,ry=rx-1,ry
  if command=="v":
    shift_down(ry, rx)
    if grid[rx+1][ry]==EMPTY:
      grid[rx+1][ry]=ROBOT
      grid[rx][ry]=EMPTY
      rx,ry=rx+1,ry
  print_grid()

score=0
for i in range(rows):
  for j in range(cols):
    if grid[i][j]!=BOX: continue
    score+=(100*i+j)
print(score)