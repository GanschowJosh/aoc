with open(input(),'r') as f:
  lines=f.readlines()


distance = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])

a,b=list(lines[0].strip().split(',')),list(lines[1].split(','))

curr=[0,0]
seen=set()
for ins in a:
  dir,dist=ins[0],int(ins[1:])
  if dir == 'R':
    for _ in range(dist):
      curr[0]+=1
      seen.add(tuple(curr))
  if dir == 'L':
    for _ in range(dist):
      curr[0]-=1
      seen.add(tuple(curr))
  if dir == 'U':
    for _ in range(dist):
      curr[1]+=1
      seen.add(tuple(curr))
  if dir == 'D':
    for _ in range(dist):
      curr[1]-=1
      seen.add(tuple(curr))

curr = [0,0]
best = 10**10
for ins in b:
  dir,dist=ins[0],int(ins[1:])
  if dir == 'R':
    for _ in range(dist):
      curr[0]+=1
      if tuple(curr) in seen:
        best=min(best,distance(curr,(0,0)))
  if dir == 'L':
    for _ in range(dist):
      curr[0]-=1
      if tuple(curr) in seen:
        best=min(best, distance(curr,(0,0)))
  if dir == 'U':
    for _ in range(dist):
      curr[1]+=1
      if tuple(curr) in seen:
        best=min(best,distance(curr,(0,0)))
  if dir == 'D':
    for _ in range(dist):
      curr[1]-=1
      if tuple(curr) in seen:
        best=min(best,distance(curr,(0,0)))

print(best)