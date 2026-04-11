from math import prod
with open(input(), 'r') as f:
  lines=f.readlines()


s=0
for line in lines:
  maxs={
    "red": 0,
    "green": 0,
    "blue": 0
  }
  line=line.strip()
  a=line.split()
  id=int(a[1][:-1])
  rounds=line.split(": ")[1].split("; ")
  #print(rounds)
  for round in rounds:
    pulls=round.split(", ")
    #print(pulls)
    for pull in pulls:
      amount,color=pull.split()
      amount=int(amount)
      #print(amount,color)
      if amount > maxs[color]:
        maxs[color]=amount
  s+=prod(maxs.values())

print(s)