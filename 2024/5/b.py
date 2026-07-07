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

def is_correct(update):
  seen = set()
  for page in update:
    seen.add(page)
    for c in firsts[page]:
      if c in seen:
        return False
  else:
    return True

def find_viol(update):
  seen = set()
  for i, page in enumerate(update):
    seen.add(page)
    for c in firsts[page]:
      if c in seen:
        return (page, c) #violator, violation

# print(firsts)

middle_sum = 0
for update in updates:
  update = list(map(int, update.split(",")))
  if is_correct(update): continue
  else:
    while not is_correct(update):
      # print(update)
      page, bad = find_viol(update)
      update.remove(page)
      update.insert(update.index(bad), page)
    print(update)
    middle_sum += update[(len(update)//2)]

print(middle_sum)