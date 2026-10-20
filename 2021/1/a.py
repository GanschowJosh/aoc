with open(input(),'r') as f:
  lines=f.readlines()

inc=0
last=int(lines[0].strip())
for line in lines[1:]:
  line=int(line.strip())
  if line > last:
    print(line, last)
  inc+=int(line>last)
  last=line

print(inc)
