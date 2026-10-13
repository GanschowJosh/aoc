with open(input(),'r') as f:
  lines=f.readlines()


distance = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])

a,b=list(lines[0].strip().split(',')),list(lines[1].split(','))

curr=[0,0]
seen=set()
c_step=0
steps=dict()
for ins in a:
  dir,dist=ins[0],int(ins[1:])
  if dir == 'R':
    for _ in range(dist):
      curr[0]+=1
      seen.add(tuple(curr))
      c_step+=1
      steps[tuple(curr)]=c_step
  if dir == 'L':
    for _ in range(dist):
      curr[0]-=1
      seen.add(tuple(curr))
      c_step+=1
      steps[tuple(curr)]=c_step
  if dir == 'U':
    for _ in range(dist):
      curr[1]+=1
      seen.add(tuple(curr))
      c_step+=1
      steps[tuple(curr)]=c_step
  if dir == 'D':
    for _ in range(dist):
      curr[1]-=1
      seen.add(tuple(curr))
      c_step+=1
      steps[tuple(curr)]=c_step

curr = [0,0]
best = 10**10
c_step=0
for ins in b:
  dir,dist=ins[0],int(ins[1:])
  if dir == 'R':
    for _ in range(dist):
      curr[0]+=1
      c_step+=1
      if tuple(curr) in seen:
        best=min(best,c_step+steps[tuple(curr)])
  if dir == 'L':
    for _ in range(dist):
      curr[0]-=1
      c_step+=1
      if tuple(curr) in seen:
        best=min(best,c_step+steps[tuple(curr)])
  if dir == 'U':
    for _ in range(dist):
      curr[1]+=1
      c_step+=1
      if tuple(curr) in seen:
        best=min(best,c_step+steps[tuple(curr)])
  if dir == 'D':
    for _ in range(dist):
      curr[1]-=1
      c_step+=1
      if tuple(curr) in seen:
        best=min(best,c_step+steps[tuple(curr)])

print(best)