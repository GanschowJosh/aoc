with open(input(), 'r') as f:
  blocks=f.read().split("\n\n")

for block in blocks:
  print(block.split("\n"))

seeds=list(map(int,blocks[0].split(": ")[1].split()))
maps=[]
for block in blocks[1:]:
  ranges=[]
  for line in block.split("\n")[1:]:
    d,s,l=map(int,line.split())
    ranges.append((s,s+l,d-s))
  ranges.sort()
  maps.append(ranges)

def apply_map(x,ranges):
  for s,e,o in ranges:
    if s<=x<e:
      return x+o
  return x

def apply_all(x,maps):
  for ranges in maps:
    x=apply_map(x,ranges)
  return x

m=10**18
for s in seeds:
  m=min(m,apply_all(s,maps))

print(m)
