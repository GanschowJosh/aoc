with open(input(), 'r') as f:
  lines = f.readlines()

l = len(lines)
ranges = []
start = 0
m = 0
for i, line in enumerate(lines):
  if line == '\n':start = i+1; break
  a, b = map(int, line.strip().split("-"))
  ranges.append((a,b))


print("done finding valid")

ranges.sort()
res = []
for i in range(start-1):
  a,b = ranges[i]
  if res and res[-1][1] >=b:
    continue
  for j in range(i+1, start-1):
    if ranges[j][0] <= b:
      b = max(b, ranges[j][1])
  res.append((a,b))

out = 0
for a,b in res:
  out += b-a+1
print(out)