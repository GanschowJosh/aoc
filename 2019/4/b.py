with open(input(),'r') as f:
  lines=f.readlines()

a,b=map(int, lines[0].split('-'))

ct=0
for i in range(a,b+1):
  i=str(i)
  same=False
  dec=True
  last=i[0]
  for j,chr in enumerate(i[1:],start=1):
    if chr==last:
      if j-2 >= 0 and i[j-2]==chr: continue
      if j+1 < len(i) and i[j+1]==chr: continue
      same=True
    if int(chr) < int(last): dec=False
    if not dec: break
    last=chr
  if same and dec:
    ct+=1

print(ct)