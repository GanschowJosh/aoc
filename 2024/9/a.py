with open(input(), 'r') as f:
  line = f.readline().strip()

def find_next_empty(ex, l):
  for i in range(l):
    if ex[i] == '.': return i
  return None

l = len(line)
ex = []
j = 0
empties = 0
for i in range(l):
  curr = int(line[i])
  if i%2 == 0: ex.extend([str(j)]*curr);j+=1
  else: ex.extend(['.']*curr); empties+=curr

end = len(ex)
print(empties)
while empties:
  n = find_next_empty(ex, end)
  ex[n],ex[end-1] = ex[end-1],ex[n]
  end-=1
  empties-=1
  # print("".join(ex[:end]))

checksum = 0
for i in range(end):
  checksum += (i*int(ex[i]))
print(checksum)