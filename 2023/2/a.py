with open(input(), 'r') as f:
  lines=f.readlines()

maxs= {
  "red": 12,
  "green": 13,
  "blue": 14
}

s=0
for line in lines:
  line=line.strip()
  a=line.split()
  id=int(a[1][:-1])
  rounds=line.split(": ")[1].split("; ")
  #print(rounds)
  valid=True
  for round in rounds:
    pulls=round.split(", ")
    #print(pulls)
    for pull in pulls:
      amount,color=pull.split()
      amount=int(amount)
      #print(amount,color)
      if amount > maxs[color]:
        valid=False
  if valid:
    #print(id)
    s+=id

print(s)