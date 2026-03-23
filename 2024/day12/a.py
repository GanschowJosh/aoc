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
for x in range(rows):
  for y in range(cols):
    area[ass[x][y]]+=1

perim = defaultdict(int)

for x in range(rows):
  for y in range(cols):
    cid = ass[x][y]
    for dx, dy in neighbors:
      nx, ny = x+dx, y+dy
      if not(0<=nx < rows and 0 <= ny < cols):
        perim[cid] += 1
      elif ass[nx][ny] != cid: perim[cid] += 1

score = {cid: area[cid]*perim[cid] for cid in area}

print(sum(score.values()))