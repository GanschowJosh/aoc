
with open(input(), "r") as f:
  lines = f.readlines()

lines = list(map(lambda x: x.strip(), (line for line in lines)))


curr = 50
out = 0
for line in lines:
  dir, num = line[0], int("".join(line[1:]))
  num %= 100
  if dir == 'L': curr -= num
  else: curr += num
  curr %= 100
  if curr == 0:
    out += 1
    print(dir, num)

print(out)