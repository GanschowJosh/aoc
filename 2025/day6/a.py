from math import prod
with open(input(), "r") as f:
  lines = f.readlines()

ops = {
  '+': sum,
  '*': prod
}

l = len(lines[0].strip().split())
s = 0
for i in range(l):
  curr = []
  for line in lines[:-1]:
    line = list(map(int, line.strip().split()))
    curr.append(line[i])
  s += ops[lines[-1].split()[i]](curr)

print(s)