from collections import deque
with open(input(), 'r') as f:
  lines = f.readlines()

m = [tuple(line.split()) for line in lines]
machines = []
for i,machine in enumerate(m):
  diagram, wirings, joltage = machine[0], machine[1:-1], machine[-1]
  diagram = tuple(diagram[1:-1])
  wirings = [tuple(map(int,wiring[1:-1].split(","))) for wiring in wirings]
  joltage = list(map(int, joltage[1:-1].split(",")))
  machines.append((diagram, wirings, joltage))

def bfs(start, target, wirings):
  if start == target: return 0
  q = deque([(start, 0)])
  seen = {start}

  while q:
    curr, d = q.popleft()
    for state in wirings:
      nxt = list(curr)
      for s in state:
        nxt[s] = '#' if nxt[s] == '.' else '.'
      nxt = tuple(nxt)

      if nxt == target: return d+1
      if nxt not in seen:
        seen.add(nxt)
        q.append((nxt, d+1))
  
  return None

s = 0
for d, w, j in machines:
  curr = tuple('.'*len(d))  
  s += bfs(curr, d, w)

print(s)