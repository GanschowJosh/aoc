with open(input(),'r') as f:
  line=f.readlines()[0]

code=list(map(int, line.split(",")))

code[1]=12
code[2]=2

curr = 0
while code[curr] != 99:
  op=code[curr]
  if op not in (1,2): print('what'); exit()
  a,b,c=code[curr+1:curr+4]
  if op == 1:
    code[c]=code[a]+code[b]
  if op == 2:
    code[c]=code[a]*code[b]
  curr += 4

print(code[0])