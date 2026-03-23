with open(input(), 'r') as f:
  lines = f.readlines()

l = len(lines)
ranges = []
start = 0
for i, line in enumerate(lines):
  if line == '\n':start = i+1; break
  a, b = map(int, line.strip().split("-"))
  ranges.append((a,b))


print("done finding valid")

out = 0
for j in range(start, l):
  curr = int(lines[j].strip())
  if any(a <= curr <= b for a,b in ranges): out+=1

print(out)