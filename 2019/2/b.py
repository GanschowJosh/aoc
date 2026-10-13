with open(input(),'r') as f:
  line=f.readlines()[0]

og_code=list(map(int, line.split(",")))

target=19690720

for noun in range(100):
  for verb in range(100):
    code=og_code[:]
    code[1]=noun
    code[2]=verb



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
    if code[0]==target:
      print(100*noun+verb)
      exit()