with open(input(), 'r') as f:
  lines=f.readlines()

gr=[[0]*1000 for _ in range(1000)]

for line in lines:
  l=line.split(' -> ')
  x1,y1=map(int,l[0].split(','))
  x2,y2=map(int,l[1].split(','))
  dx=(x2>x1)-(x2<x1)
  dy=(y2>y1)-(y2<y1)
  st=max(abs(x2-x1),abs(y2-y1))

  for i in range(st+1):
    gr[x1+i*dx][y1+i*dy]+=1

print(sum(1 for row in gr for x in row if x > 1))