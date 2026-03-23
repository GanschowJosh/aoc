from copy import deepcopy
with open(input(), "r") as f:
  lines = f.readlines()

area = []
visited = set()
curr = ()
for i, line in enumerate(lines):
  area.append(list(line.strip()))
  l = line.replace('.','').replace('#','').replace(chr(10), '')
  if l:
    curr = (i, line.index(l[0]), l[0])

rows, cols = len(area), len(area[0])

def simulate(area, curr):
  rows, cols = len(area), len(area[0])
  curr_char = area[curr[0]][curr[1]]
  visited = set()
  while 0 <= curr[0] < rows and 0 <= curr[1] < cols and len(visited) < 4*rows*cols:
    if curr in visited: return True
    visited.add(curr)
    x, y, curr_char = curr
    if curr_char == '^':
      if x == 0: return False
      if area[x-1][y] != '#': curr = (x-1, y, curr_char)
      else: curr_char = '>'; curr = (x, y, curr_char)
    elif curr_char == 'v':
      if x == rows-1: return False
      if area[x+1][y] != '#': curr = (x+1, y, curr_char)
      else: curr_char = '<'; curr = (x, y, curr_char)
    elif curr_char == '<':
      if y == 0: return False
      if area[x][y-1] != '#': curr = (x, y-1, curr_char)
      else: curr_char = '^'; curr = (x, y, curr_char)
    elif curr_char == '>':
      if y == cols-1: return False
      if area[x][y+1] != "#": curr = (x, y+1, curr_char)
      else: curr_char = 'v'; curr = (x, y, curr_char)
    
    area[curr[0]][curr[1]] = curr_char


pos = set()
for i in range(rows):
  for j in range(cols):
    new_area = deepcopy(area)
    if new_area[i][j] not in ['^','v','<','>','#']: new_area[i][j] = '#'
    if simulate(new_area, curr): pos.add((i, j))

print(pos, len(pos))