with open(input(),'r') as f:
  line=list(map(int, f.readlines()[0].split(',')))

bst=10**10
for i in range(min(line),max(line)+1):
  bst=min(bst,sum(abs(x-i) for x in line))

print(bst)