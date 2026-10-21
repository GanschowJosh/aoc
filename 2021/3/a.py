with open(input(), 'r') as f:
  lines=f.readlines()

c=[0]*(len(lines[0])-1)
for line in lines:
  line=int(line.strip(), 2)
  for i in range(len(c)):
    if line & (1 << i):
      c[i]+=1
    else:
      c[i]-=1
    print(c)

gamma=int('0b'+''.join(map(str, (int(i > 0) for i in reversed(c)))),2)
epsilon=int('0b'+'1'*len(c),2)-gamma
print(epsilon*gamma)