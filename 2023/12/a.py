from itertools import combinations

with open(input(), 'r') as f:
  lines=f.readlines()

rows=[]
arrs=[]
for line in lines:
  row,arr=line.strip().split()
  rows.append(list(row))
  arrs.append(tuple(map(int, arr.split(","))))


def find_config(row):
  o=[]
  curr=0
  for c in row:
    if c=='#': curr+=1
    else:
      if curr == 0: continue
      o.append(curr)
      curr=0
  if curr!=0:
    o.append(curr)
  return tuple(o)
  
found = 0
l = len(rows)
for i in range(l):
  crow=rows[i]
  car=arrs[i]

  qs=[]
  num_h=0
  for i,p in enumerate(crow):
    if p=='?': qs.append(i)
    if p=='#': num_h+=1
  
  needed=sum(car)
  if needed<num_h: continue
  diff=needed-num_h

  
  for comb in combinations(qs, diff):
    tmp=crow[:]
    for c in comb:
      tmp[c]='#'
    # print(*tmp)
    # print(find_config(tmp))
    if find_config(tmp)==car: found+=1
  
  # print(found)

print(found)
