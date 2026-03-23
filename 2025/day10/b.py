from z3 import Ints, Int, Sum, Optimize, sat

with open(input(), 'r') as f:
  lines = f.readlines()

m = [tuple(line.split()) for line in lines]
machines = []
for i,machine in enumerate(m):
  diagram, wirings, joltage = machine[0], machine[1:-1], machine[-1]
  diagram = tuple(diagram[1:-1])
  wirings = [tuple(map(int,wiring[1:-1].split(","))) for wiring in wirings]
  joltage = tuple(map(int, joltage[1:-1].split(",")))
  machines.append((diagram, wirings, joltage))

# mld = max(len(machine[0]) for machine in machines)
# mlw = max(len(machine[1]) for machine in machines)
# mlj = max(len(machine[2]) for machine in machines)

# mm = max(max(machine[2]) for machine in machines)

# print(f"diagram max length = {mld}\nwiring max length = {mld}\njoltage max length = {mlj}\nmax target: {mm}")

def solve(target, wirings):
  m = len(target)
  b = len(wirings)

  opt = Optimize()

  U = sum(target)
  x = [Int(f"x{k}") for k in range(b)]
  for k in range(b):
    opt.add(x[k]>=0, x[k] <= U)

  for i in range(m):
    opt.add(Sum(x[k] for k in range(b) if i in wirings[k])==target[i])
  
  opt.minimize(Sum(x))

  if opt.check() != sat: return None

  model = opt.model()
  return sum(model.evaluate(xk).as_long() for xk in x)

s = 0
for d, w, j in machines:
  # print(curr)
  s += solve(j, w)

print(s)