with open(input(), 'r') as f:
  lines=f.readlines()

patterns=lines[0].strip().split(", ")
desired=[]
for line in lines[2:]:
  desired.append(line.strip())


def ispossible(design):
  global patterns
  n=len(design)
  p=[0]*(n+1)
  p[0]=1
  for i in range(n):
    if not p[i]:continue
    for pat in patterns:
      if design.startswith(pat, i):
        p[i+len(pat)]+=p[i]
  return p[n]

c=0
for d in desired:
  c+=ispossible(d)
print(c)