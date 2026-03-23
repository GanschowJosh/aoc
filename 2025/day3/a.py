with open(input(), "r") as f:
  lines = f.readlines()

s = 0
for line in lines:
  line = list(map(int, line.strip()))
  m = 0
  max_seen = -1
  for bat in line:
    curr = int("".join([str(max_seen), str(bat)]))
    if curr > m: m = curr
    max_seen = max(max_seen, bat)
  s += m
  # print(max_seen, m)
print(s)