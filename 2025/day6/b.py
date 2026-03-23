from math import prod
with open(input(), "r") as f:
  lines = f.readlines()

ops = {
  '+': sum,
  '*': prod
}

l = max(len(line) for line in lines)
n = len(lines)
print(l)
s = 0
curr = ['']*l
for i in range(l):
  if all(line[i] == ' ' for line in lines) or all(line[i] == '\n' for line in lines): 
    curr = [c for c in curr if c.strip()!='']
    operand = curr[0][-1]
    curr[0] = ''.join(curr[0][:-1])
    vals = list(map(int, map(str.strip, (c for c in curr if c != ''))))
    s += ops[operand](vals)
    # print(vals)
    curr=['']*l
    continue
  for j in range(n):
    curr[i]+=lines[j][i]
    # print(curr)
  #s += ops[lines[-1].split()[i]](curr)

print(s)