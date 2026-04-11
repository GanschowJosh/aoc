with open(input(), 'r') as f:
  lines=f.readlines()

o=0

for i,line in enumerate(lines):
  line=line.strip()
  a=line.split()
  _,nums=line.split(": ")
  w,n=nums.split(" | ")
  w=set(map(int, w.split()))
  n=set(map(int, n.split()))
  print(w,n)
  l=len(n&w)
  print(f"for game #{i+1}: {int(2**(l-1))}")
  o+=int(2**(l-1))
print(o)