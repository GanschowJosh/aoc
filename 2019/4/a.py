with open(input(),'r') as f:
  lines=f.readlines()

a,b=map(int, lines[0].split('-'))

ct=0
for i in range(a,b+1):
  i=str(i)
  same=False
  dec=True
  last=i[0]
  for chr in i[1:]:
    if chr==last: same=True
    if int(chr) < int(last): dec=False
    if not dec: break
    last=chr
  if same and dec:
    ct+=1

print(ct)