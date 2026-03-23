from copy import deepcopy

with open(input(), 'r') as f:
  lines = list(map(str.strip, f.readlines()))
  lines = list(map(list, lines))

for i, line in enumerate(lines):
  if 'S' in line:
    start = (i, line.index('S'))

rows, cols = len(lines), len(lines[0])
beams = set()
beams.add(start)
# out = deepcopy(lines)
splits = set()
while beams:
  temp_beams = deepcopy(beams)
  beams.clear()
  for (x,y) in temp_beams:
    # print(beams)
    if lines[x][y] == '^':
      # print(x,y)
      splits.add((x,y))
      if y > 0: beams.add((x,y-1))
      if y < cols-1: beams.add((x,y+1))
    else:
      if x+1 < rows:
      # beams[i]=(x+1,y)
        beams.add((x+1,y))
    # if out[x][y] not in ['S','^']:
    #   out[x][y] = '|'
print(len(splits))
# for (x,y) in splits:
#   out[x][y] = 'S'

# for row in out:
#   print("".join(row))