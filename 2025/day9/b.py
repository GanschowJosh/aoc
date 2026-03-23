from collections import deque

with open(input(), 'r') as f:
  lines = list(map(str.strip, f.readlines()))

coords = []
for line in lines:
  coords.append(tuple(map(int, line.split(','))))

def area(a, b):
  x1, y1 = a
  x2, y2 = b
  return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

# build edges from red loop
edges = []
for i in range(len(coords)):
  x1, y1 = coords[i]
  x2, y2 = coords[(i + 1) % len(coords)]
  if x1 == x2:
    if y1 > y2:
      y1, y2 = y2, y1
    edges.append(('v', x1, y1, y2))
  else:
    if x1 > x2:
      x1, x2 = x2, x1
    # y1 == y2 by problem statement
    edges.append(('h', y1, x1, x2))

# coordinate compression
xs = set()
ys = set()
for x, y in coords:
  xs.add(x)
  ys.add(y)

minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)

xs.update([minx - 1, maxx + 1])
ys.update([miny - 1, maxy + 1])

xs = sorted(xs)
ys = sorted(ys)
x_idx = {x: i for i, x in enumerate(xs)}
y_idx = {y: i for i, y in enumerate(ys)}

w = len(xs) - 1
h = len(ys) - 1

v_wall = [[False] * h for _ in range(w + 1)]  # between columns i-1 and i
h_wall = [[False] * (h + 1) for _ in range(w)]  # between rows j-1 and j

for kind, a, b1, b2 in edges:
  if kind == 'v':
    x = a
    i = x_idx[x]
    for j in range(h):
      if ys[j + 1] <= b1 or ys[j] >= b2:
        continue
      v_wall[i][j] = True
  else:
    y = a
    j = y_idx[y]
    for i in range(w):
      if xs[i + 1] <= b1 or xs[i] >= b2:
        continue
      h_wall[i][j] = True

start_i = x_idx[minx - 1]
start_j = y_idx[miny - 1]

outside = [[False] * h for _ in range(w)]
q = deque()
q.append((start_i, start_j))
outside[start_i][start_j] = True

while q:
  i, j = q.popleft()
  # left
  if i > 0 and not outside[i - 1][j] and not v_wall[i][j]:
    outside[i - 1][j] = True
    q.append((i - 1, j))
  # right
  if i + 1 < w and not outside[i + 1][j] and not v_wall[i + 1][j]:
    outside[i + 1][j] = True
    q.append((i + 1, j))
  # down
  if j > 0 and not outside[i][j - 1] and not h_wall[i][j]:
    outside[i][j - 1] = True
    q.append((i, j - 1))
  # up
  if j + 1 < h and not outside[i][j + 1] and not h_wall[i][j + 1]:
    outside[i][j + 1] = True
    q.append((i, j + 1))

inside = [[not outside[i][j] for j in range(h)] for i in range(w)]

psum = [[0] * (h + 1) for _ in range(w + 1)]
for i in range(w):
  row_sum = 0
  for j in range(h):
    if inside[i][j]:
      row_sum += 1
    psum[i + 1][j + 1] = psum[i][j + 1] + row_sum

def sum_inside(x1, y1, x2, y2):
  return (
    psum[x2][y2]
    - psum[x1][y2]
    - psum[x2][y1]
    + psum[x1][y1]
  )

n = len(coords)
best = 0
for i in range(n):
  x1, y1 = coords[i]
  for j in range(i + 1, n):
    x2, y2 = coords[j]
    lx, rx = sorted((x1, x2))
    ly, ry = sorted((y1, y2))

    ci1 = x_idx[lx]
    ci2 = x_idx[rx]
    cj1 = y_idx[ly]
    cj2 = y_idx[ry]

    tot_cells = (ci2 - ci1) * (cj2 - cj1)
    if tot_cells == 0:
      continue

    s = sum_inside(ci1, cj1, ci2, cj2)
    if s != tot_cells:
      continue

    best = max(best, area((x1, y1), (x2, y2)))

print(best)
