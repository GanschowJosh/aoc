with open(input(), "r") as f:
    lines = f.readlines()

ongrid = True
grid = []
moves = ""
for line in lines:
  line = line.strip()
  if not line: ongrid = False; continue
  if ongrid:
    new_row = []
    for ch in line:
      if ch == '#':   new_row += ['#','#']
      elif ch == 'O': new_row += ['[',']']
      elif ch == '.': new_row += ['.','.']
      elif ch == '@': new_row += ['@','.']
    grid.append(new_row)
  else:
    moves += line

rows, cols = len(grid), len(grid[0])

for i in range(rows):
  for j in range(cols):
    if grid[i][j] == '@':
      rx, ry = i, j

BOX_CHARS = {'[', ']'}

def try_move_horizontal(dc):
  global rx, ry
  nc = ry + dc
  ec = nc
  while grid[rx][ec] in BOX_CHARS:
    ec += dc
  if grid[rx][ec] == '#':
    return
  while ec != ry:
    grid[rx][ec] = grid[rx][ec - dc]
    ec -= dc
  grid[rx][ry] = '.'
  ry += dc

def try_move_vertical(dr):
  global rx,ry
  frontier = {(rx, ry)}
  all_cells = set()
  while frontier:
    next_frontier = set()
    for (r, c) in frontier:
      nr = r + dr
      cell = grid[nr][c]
      if cell == '#':
        return
      all_cells.add((r, c))
      if cell == '[':
        next_frontier.add((nr, c))
        next_frontier.add((nr, c + 1))
      elif cell == ']':
        next_frontier.add((nr, c))
        next_frontier.add((nr, c - 1))
    frontier = next_frontier - all_cells

  for (r, c) in sorted(all_cells, key=lambda x: x[0], reverse=(dr == 1)):
    grid[r + dr][c] = grid[r][c]
    grid[r][c] = '.'
  rx += dr

for command in moves:
  if command == '<':
    try_move_horizontal(-1)
  elif command == '>':
    try_move_horizontal(1)
  elif command == '^':
    try_move_vertical(-1)
  elif command == 'v':
    try_move_vertical(1)

score = 0
for i in range(rows):
  for j in range(cols):
    if grid[i][j] == '[':
      score += 100 * i + j
print(score)