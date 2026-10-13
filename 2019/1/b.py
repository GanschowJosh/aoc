with open(input(), 'r') as f:
  lines=f.readlines()

su=0
for line in lines:
  line=int(line)
  while line > 0:
    line//=3
    line-=2
    if line <= 0: continue
    print(line)
    su+=line

print(su)
