with open(input(),'r') as f:
  lines=f.readlines()

pos,depth,aim=0,0,0

for line in lines:
  d,amt=line.split()
  amt=int(amt)
  if d == 'forward': 
    pos += amt
    depth += (aim*amt)
  elif d == 'down': aim += amt
  else: aim-=amt

print(depth*pos)