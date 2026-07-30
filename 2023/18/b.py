with open(input(), 'r') as f:
  lines=f.readlines()

cx,cy=0,0
x=[]
y=[]
steps=[]
dirmap={
  "0": 'R',
  "1": 'D',
  "2": "L",
  "3": "U"
}
for line in lines:
  a,b,c=line.strip().split()
  direction=dirmap[c[-2]]
  dist=int(c[2:-2],16)
  steps.append((direction, dist))

vertices = [(0, 0)]
cx = cy = 0
boundary = 0

for direction, distance in steps:
  boundary += distance

  if direction == 'R':
    cx += distance
  elif direction == 'L':
    cx -= distance
  elif direction == 'D':
    cy += distance
  elif direction == 'U':
    cy -= distance

  vertices.append((cx, cy))

area2 = 0
for (x1, y1), (x2, y2) in zip(vertices, vertices[1:]):
  area2 += x1 * y2 - x2 * y1

ans = (abs(area2) + boundary) // 2 + 1
print(ans)