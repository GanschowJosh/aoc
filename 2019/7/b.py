with open(input(), 'r') as f:
  code = list(map(int, f.readline().split(',')))

def run(code, curr, inps):
  while True:
    cc = str(code[curr]).rjust(5, '0')
    op = int(cc[-2:])

    def param(offset):
      value = code[curr + offset]
      return code[value] if cc[3 - offset] == '0' else value

    if op == 1:
      code[code[curr + 3]] = param(1) + param(2)
      curr += 4
    elif op == 2:
      code[code[curr + 3]] = param(1) * param(2)
      curr += 4
    elif op == 3:
      if not inps:
        return 'input', None, curr
      code[code[curr + 1]] = inps.popleft()
      curr += 2
    elif op == 4:
      out = param(1)
      return 'output', out, curr + 2
    elif op == 5:
      curr = param(2) if param(1) else curr + 3
    elif op == 6:
      curr = param(2) if not param(1) else curr + 3
    elif op == 7:
      code[code[curr + 3]] = int(param(1) < param(2))
      curr += 4
    elif op == 8:
      code[code[curr + 3]] = int(param(1) == param(2))
      curr += 4
    elif op == 99:
      return 'halt', None, curr


from collections import deque
from itertools import permutations

best = 0
for phases in permutations(range(5, 10)):
  states = [[code.copy(), 0] for _ in range(5)]
  inps = [deque([phases[i]]) for i in range(5)]
  inps[0].append(0)
  done = [False] * 5
  last_e_output = 0

  i = 0
  while not all(done):
    if not done[i]:
      memory, curr = states[i]
      event, out, curr = run(memory, curr, inps[i])
      states[i][1] = curr

      if event == 'output':
        inps[(i + 1) % 5].append(out)
        if i == 4:
          last_e_output = out
      elif event == 'halt':
        done[i] = True

    i = (i + 1) % 5

  best = max(best, last_e_output)

print(best)
