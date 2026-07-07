import queue
from collections import defaultdict

with open(input(), 'r') as f:
  lines = f.readlines()

plot = list(map(str.strip, lines))
# print(plot)

rows, cols = len(plot), len(plot[0])

ass = [[-1]*cols for _ in range(rows)]
neighbors = [
  [-1,0],
  [0,-1],[0,1],
  [1,0]
]

def printarr(arr):
  for row in arr:
    print("".join(map(str, row)))

def fill(x, y, counter):
  if ass[x][y] != -1: return counter
  ch = plot[x][y]
  # print(ch)
  q = queue.Queue()
  q.put((x,y))
  while q.qsize():
    # print(q.qsize())
    currx, curry = q.get()
    if plot[currx][curry] != ch or ass[currx][curry] != -1: continue
    ass[currx][curry] = counter
    # print(f"  adding {currx},{curry} as {counter}")
    # printarr(ass)
    for dx, dy in neighbors:
      nx, ny = dx+currx, dy+curry
      if 0 <= nx < rows and 0 <= ny < cols:
        q.put((nx,ny))
  return counter+1

counter = 0
for i in range(rows):
  for j in range(cols):
    counter = fill(i, j, counter)

# printarr(ass)

area = defaultdict(int)
for r in range(rows):
  for c in range(cols):
    area[ass[r][c]] += 1

def same(cid, r, c):
  return 0 <= r < rows and 0 <= c < cols and ass[r][c] == cid

sides = defaultdict(int)

for r in range(rows):
  for c in range(cols):
    cid = ass[r][c]

    #for each cell, count corners contributed to its region.
    #corner tests: (up, left, diag), (up, right, diag), (down, left, diag), (down, right, diag)

    # top-left corner
    up = same(cid, r-1, c)
    left = same(cid, r, c-1)
    diag = same(cid, r-1, c-1)
    if (not up and not left) or (up and left and not diag):
      sides[cid] += 1

    # top-right corner
    up = same(cid, r-1, c)
    right = same(cid, r, c+1)
    diag = same(cid, r-1, c+1)
    if (not up and not right) or (up and right and not diag):
      sides[cid] += 1

    # bottom-left corner
    down = same(cid, r+1, c)
    left = same(cid, r, c-1)
    diag = same(cid, r+1, c-1)
    if (not down and not left) or (down and left and not diag):
      sides[cid] += 1

    # bottom-right corner
    down = same(cid, r+1, c)
    right = same(cid, r, c+1)
    diag = same(cid, r+1, c+1)
    if (not down and not right) or (down and right and not diag):
      sides[cid] += 1

total = 0
for cid in area:
  total += area[cid] * sides[cid]

print(total)