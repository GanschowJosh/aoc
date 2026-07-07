from collections import defaultdict
from pathlib import Path

base_dir = Path(__file__).resolve().parent

with open(base_dir / input().strip(), "r") as f:
  lines = f.readlines()


conds, updates = list(), list()
for line in lines:
  if line == '\n': continue
  line = line.strip()
  if "|" in line: conds.append(line); conds[-1] = (int(conds[-1].split("|")[0]), int(conds[-1].split("|")[1]))
  else: updates.append(line)

# print(conds, updates)

firsts = defaultdict(list)
for a, b in conds:
  firsts[a].append(b)

print(firsts)
middle_sum = 0
for update in updates:
  update = list(map(int, update.split(",")))
  seen = set()
  bad = False
  for page in update:
    seen.add(page)
    for c in firsts[page]:
      if c in seen:
        bad=True;break
    if bad: break
  else: 
    # print(update[(len(update)//2) + 1])
    print(update)
    middle_sum += update[(len(update)//2)]

print(middle_sum)