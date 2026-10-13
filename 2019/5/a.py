with open(input(),'r') as f:
  lines=f.readlines()

code=list(map(int, lines[0].split(',')))

curr = 0
while code[curr] != 99:
  cc=str(code[curr])
  op=cc[-1]
  cc=cc.rjust(5,'0')
  if op == '1':
    a,b,c=code[curr+1:curr+4]
    if cc[2] == '0':
      a=code[a]
    if cc[1] == '0':
      b=code[b]
    code[c]=a+b
    curr+=4
  if op == '2':
    a,b,c=code[curr+1:curr+4]
    if cc[2] == '0':
      a=code[a]
    if cc[1] == '0':
      b=code[b]
    code[c]=a*b
    curr+=4
  if op == '3':
    a=code[curr+1]
    i=int(input())
    code[a]=i
    curr+=2
  if op == '4':
    print(code[code[curr+1]])
    curr+=2
  
print(code)