with open(input(),'r') as f:
  lines=list(map(lambda x: x.strip(), f.readlines()))

inc=0
last=sum(map(int, lines[:3]))
print(lines[:3])
for i in range(1, len(lines)-2):
  print(lines[i:i+3])
  su=sum(map(int, lines[i:i+3]))
  # if su > last:
    # print(su, last)
  inc+=int(su>last)
  last=su

print(inc)
