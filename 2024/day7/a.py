from itertools import combinations_with_replacement, product
with open(input(), 'r') as f:
  lines = f.readlines()

operators = ['+','*']

operations = {
  '+': lambda x,y: x+y,
  '*': lambda x,y: x*y,
}

out = 0
for line in lines:
  a, _ = line.split(": ")
  a = int(a)
  operands = list(map(int, _.split()))
  # print(a, operands)
  l = len(operands)
  l1 = l-1
  # print(temp_ops)
  seen = set()
  for comb in product(operators, repeat=l1):
    c = tuple(comb)
    if c in seen: continue
    seen.add(c)
    j = 0
    curr = operands[0]
    for i in range(1,l):
      curr = operations[c[j]](curr, operands[i])
      j+=1
    if curr == a: print(c);out+=a; break

print(out)