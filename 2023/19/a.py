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

su = 0
for part in parts:
  curr='in'
  while curr not in ('A','R'):
    cwf = wf[curr]
    for cond in cwf:
      if cond[1] == '>':
        if part[cond[0]] > cond[2]:
          curr = cond[3]
          break
      elif cond[1] == '<':
        if part[cond[0]] < cond[2]:
          curr = cond[3]
          break
      else:
        curr = cond[3]
  if curr == 'A':
    su+=sum(part[a] for a in 'xmas')
print(su)