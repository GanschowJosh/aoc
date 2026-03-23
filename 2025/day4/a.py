from copy import deepcopy

with open(input(), "r") as f:
  lines = f.readlines()

diagram = []
for line in lines:
  diagram.append(list(line.strip()))
# print(diagram)

neighbors = [
  [-1,-1],[-1,0],[-1,1],
  [0,-1],[0,1],
  [1,-1],[1,0],[1,1]
]

out = 0
out_diag = deepcopy(diagram)
rows, cols = len(diagram), len(diagram[0])
for x in range(rows):
  for y in range(cols):
    if diagram[x][y] != '@':continue
    found = 0
    for dx, dy in neighbors:
      nx, ny = dx+x, dy+y
      if 0 <= nx < rows and 0 <= ny < cols:
        if diagram[nx][ny] == '@': found += 1
    if found < 4: out+=1;print(x, y);out_diag[x][y]='x'

print(out)
# for row in out_diag:
#   print("".join(row))