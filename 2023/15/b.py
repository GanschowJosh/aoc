from collections import defaultdict
import re
with open(input(), 'r') as f:
  lines=f.readlines()

def hash(st):
  o=0
  for c in st:
    o+=ord(c)
    o*=17
    o%=256
  return o

co=list(lines[0].split(","))
codes=[]
for code in co:
  if code[-1]=='-':
    codes.append(('-',code[:-1]))
  else:
    lens,fl=re.match(r'(.+?)=(.+)', code).groups()
    codes.append(('=', lens, int(fl)))

boxes=defaultdict(list)

for code in codes:
  h=hash(code[1])
  if code[0] == '-':
    b=boxes[h]
    for bi in b:
      if bi[0]==code[1]:
        b.remove(bi)
        break
  elif code[0]=='=':
    b=boxes[h]
    for bi in b:
      if bi[0]==code[1]:
        b[b.index(bi)]=(code[1], code[2])
        break
    else:
      b.append((code[1], code[2]))

su=0
for hashval, box in boxes.items():
  for i, (lens, fl) in enumerate(box):
    su+=((1+hashval)*(i+1)*(fl))

print(su)