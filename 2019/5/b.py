with open(input(),'r') as f:
  lines=f.readlines()

code=list(map(int, lines[0].split(',')))

curr = 0
while code[curr] != 99:
  #print(code,curr)
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
    a=code[curr+1]
    #print(cc,a,cc[2]=='0',code[a])
    if cc[2] == '0':
      a=code[a]
    print(a)
    curr+=2
  if op == '5':
    a,b=code[curr+1:curr+3]
    if cc[2] == '0':
      a=code[a]
    if cc[1] == '0':
      b=code[b]
    if int(a):
      curr=b
    else:
      curr+=3
  if op == '6':
    a,b=code[curr+1:curr+3]
    if cc[2] == '0':
      a=code[a]
    if cc[1] == '0':
      b=code[b]
    if not int(a):
      curr=b
    else:
      curr+=3
  if op == '7':
    a,b,c=code[curr+1:curr+4]
    if cc[2]=='0':
      a=code[a]
    if cc[1] == '0':
      b=code[b]
    if int(a) < int(b):
      code[c]=1
    else:
      code[c]=0
    curr+=4
  if op == '8':
    a,b,c=code[curr+1:curr+4]
    if cc[2]=='0':
      a=code[a]
    if cc[1]=='0':
      b=code[b]
    if int(a) == int(b):
      code[c]=1
    else:
      code[c]=0
    curr+=4
  