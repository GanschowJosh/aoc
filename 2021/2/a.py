with open(input(),'r') as f:
  lines=f.readlines()

pos, depth=0,0

for line in lines:
  d,amt=line.split()
  amt=int(amt)
  if d == 'forward': pos += amt
  elif d == 'down': depth += amt
  else: depth-=amt

print(depth*pos)