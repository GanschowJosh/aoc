with open(input(), 'r') as f:
  lines = f.readlines()

diagram = []
for line in lines:
  diagram.append(line.strip())

starts = set()
rows, cols = len(diagram), len(diagram[0])
for i in range(rows):
  for j in range(cols):
    if diagram[i][j] == '0': starts.add((i,j))

neighbors = [
  [-1,0],
  [0,-1],[0,1],
  [1,0]
]

def bfs(diagram, x, y, visited, last):
  # print(x,y)
  if (x,y) in visited: return 0
  if x < 0 or x >= rows or y < 0 or y >= cols: return 0
  if last is not None and int(diagram[x][y])-int(diagram[last[0]][last[1]]) != 1: return 0
  # visited.add((x,y))
  if diagram[x][y] == '9': return 1
  return sum(bfs(diagram,x+dx,y+dy, visited, (x,y)) for dx, dy in neighbors)

s = 0
for x,y in starts:
  # bs = s
  s += bfs(diagram, x, y, set(), None)
  # print(s-bs)

print(s)