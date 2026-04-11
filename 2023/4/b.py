from collections import defaultdict
with open(input(), 'r') as f:
  lines=f.readlines()

o=0
copies=defaultdict(int)

for i,line in enumerate(lines):
  copies[i+1]+=1
  line=line.strip()
  a=line.split()
  _,nums=line.split(": ")
  w,n=nums.split(" | ")
  w=set(map(int, w.split()))
  n=set(map(int, n.split()))
  print(w,n)
  l=len(n&w)
  #print(f"card #{i+1} wins {l} adding:")
  for j in range(l):
    #print(f"  1 copy of card {i+j+2}")
    copies[i+j+2]+=copies[i+1]

print(copies)
print(sum(copies.values()))