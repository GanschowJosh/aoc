from itertools import combinations

with open(input(), "r") as f:
  lines = f.readlines()

s = 0
for line in lines:
  line = line.strip()
  d = list(map(int, line))
  n = len(d)
  k = 12
  result = []
  start = 0
  while k > 0:
    end = n-k
    max_d = -1
    max_idx = -1
    for i in range(start, end+1):
      if d[i] > max_d:
        max_d = d[i]
        max_idx = i
    result.append(max_d)
    start = max_idx+1
    k -= 1
  val = int("".join(map(str, result)))
  s+=val

print(s)
