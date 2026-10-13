with open(input(), 'r') as f:
  lines=f.readlines()

su=0
for line in lines:
  line=int(line)
  c=line//3-2
  print(c)
  su+=c

print(su)
