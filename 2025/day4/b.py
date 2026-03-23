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

def run(diagram):
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
      if found < 4: out+=1;out_diag[x][y]='.'
  return out, out_diag

out = 0

while(1):
  n, diagram = run(diagram=diagram)
  if n == 0: break
  out += n
  # for row in diagram:
  #   print("".join(row))

print(out)
