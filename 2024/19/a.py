with open(input(), 'r') as f:
  lines=f.readlines()

patterns=lines[0].strip().split(", ")
desired=[]
for line in lines[2:]:
  desired.append(line.strip())


def ispossible(design):
  global patterns
  n=len(design)
  p=[False]*(n+1)
  p[0]=True
  for i in range(n):
    if not p[i]:continue
    for pat in patterns:
      if design.startswith(pat, i):
        p[i+len(pat)]=True
  return p[n]

c=0
for d in desired:
  if ispossible(d): c+=1
print(c)