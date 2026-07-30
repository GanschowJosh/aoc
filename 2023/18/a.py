with open(input(), 'r') as f:
  lines=f.readlines()

cx,cy=0,0
x=[]
y=[]
steps=[]
for line in lines:
  a,b,c=line.strip().split()
  steps.append((a,int(b),c[1:-1]))

vertices = [(0, 0)]
cx = cy = 0
boundary = 0

for direction, distance, _ in steps:
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