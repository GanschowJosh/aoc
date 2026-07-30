with open(input(), 'r') as f:
  lines=f.readlines()

codes=list(lines[0].split(","))

def hash(st):
  o=0
  for c in st:
    o+=ord(c)
    o*=17
    o%=256
  return o

su=0
for code in codes:
  h=hash(code)
  print(f"{code} becomes {h}")
  su+=h
print(su)