with open(input(), 'r') as f:
  lines = list(map(str.strip, f.readlines()))


coords = []
for line in lines:
  coords.append(tuple(map(int, line.split(','))))

def area(a, b):
  x1, y1 = a
  x2, y2 = b
  return (abs(x2 - x1)+1) * (abs(y2 - y1)+1)

n = len(coords)
m = 0
for i in range(n):
  for j in range(i+1, n):
    m = max(m, area(coords[i], coords[j]))

print(m)