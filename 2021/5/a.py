with open(input(), 'r') as f:
  lines=f.readlines()

gr=[[0]*1000 for _ in range(1000)]

for line in lines:
  l=line.split(' -> ')
  x1,y1=map(int,l[0].split(','))
  x2,y2=map(int,l[1].split(','))
  if x1==x2:
    for i in range(min(y1,y2),max(y1,y2)+1):
      gr[x1][i]+=1
  if y1==y2:
    for i in range(min(x1,x2),max(x1,x2)+1):
      gr[i][y1]+=1

print(sum(1 for row in gr for x in row if x > 1))