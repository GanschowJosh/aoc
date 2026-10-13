from math import prod
with open(input(),'r') as f:
  lines=f.readlines()

wf=dict()
parts=[]
inwf=True
for i,line in enumerate(lines):
  line=line.strip()
  if not line:
    inwf=False
    continue
  if inwf:
    name,rules=line[:-1].split('{')

    pr=[]
    for rule in rules.split(','):
      if ':' not in rule:
        pr.append((None,None,None,rule))
        continue

      cond,dest=rule.split(':')
      pr.append((cond[0],cond[1],int(cond[2:]),dest))
    wf[name]=pr
  else:
    part={}
    for kv in line.strip("{}").split(","):
      k,v=kv.split('=')
      part[k]=int(v)
    parts.append(part)

all_constraints=[]
from collections import deque
q=deque([('in',[])])
while q:
  curr,cons=q.popleft()
  if curr == 'A':
    all_constraints.append(cons)
    continue
  if curr == 'R': continue
  cwf=wf[curr]
  for attr, op, value, dest in cwf:
    cnx=cons[:]
    if attr is not None:
      cnx.append((attr,op,value))
    q.append((dest,cnx))

    if attr is None: break

    if op == '<':
      cons.append((attr,'>',value-1))
    else:
      cons.append((attr,'<',value+1))

mp ={
  'x':0,
  'm':1,
  'a':2,
  's':3
}
su=0
print(all_constraints)
for c in all_constraints:
  mimax=[[1,4000]]*4
  for cond in c:
    cidx=mp[cond[0]]
    if cond[1]=='>':
      mimax[cidx]=[max(mimax[cidx][0],cond[2]+1),mimax[cidx][1]]
    if cond[1]=='<':
      mimax[cidx]=[mimax[cidx][0],min(mimax[cidx][1],cond[2]-1)]
  su+=prod((b-a+1) for a,b in mimax)
  print(mimax)
print(su)