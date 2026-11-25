with open(input(),'r') as f:
  lines=f.readlines()

num=0
for line in lines:
  ot=line.split(' | ')[1].split()
  print(ot)
  num+=sum(1 for x in ot if len(x) in [2,4,3,7])
print(num)