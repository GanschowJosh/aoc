with open(input(), "r") as f:
  lines = f.readlines()

area = []
visited = set()
curr = ()
for i, line in enumerate(lines):
  area.append(list(line.strip()))
  l = line.replace('.','').replace('#','').replace(chr(10), '')
  if l:
    curr = (i, line.index(l[0]))

# print(area)
# print(visited)
rows, cols = len(area), len(area[0])
curr_char = area[curr[0]][curr[1]]
while 0 <= curr[0] <= rows and 0 <= curr[1] <= cols:
  visited.add(curr)
  x, y = curr
  if curr_char == '^':
    if x == 0: print(len(visited)); exit()
    if area[x-1][y] != '#': curr = (x-1, y)
    else: curr_char = '>'
  elif curr_char == 'v':
    if x == rows-1: print(len(visited)); exit()
    if area[x+1][y] != '#': curr = (x+1, y)
    else: curr_char = '<'
  elif curr_char == '<':
    if y == 0: print(len(visited)); exit()
    if area[x][y-1] != '#': curr = (x, y-1)
    else: curr_char = '^'
  elif curr_char == '>':
    if y == cols-1: print(len(visited)); exit()
    if area[x][y+1] != "#": curr = (x, y+1)
    else: curr_char = 'v'
  
  area[curr[0]][curr[1]] = curr_char
  
  # print(visited, curr_char, x, y, curr)