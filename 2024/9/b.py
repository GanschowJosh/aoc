with open(input(), 'r') as f:
  line = f.readline().strip()

def find_next_empty(ex, l, s):
  for i in range(l-s):
    if all(c=='.' for c in ex[i:i+s]): return i
  return None

l = len(line)
ex = []
j = 0
curr_len = 0
lens = {}
locs = {}
for i in range(l):
  curr = int(line[i])
  if i%2 == 0: 
    ex.extend([str(j)]*curr)
    lens[j]=curr
    locs[j]=curr_len
    j+=1
  else: 
    ex.extend(['.']*curr)
  curr_len+=curr

j-=1
l = len(ex)
# print(ex)
# print(lens)
# print(locs)
# print(ex.index('5'))
# print(find_next_empty(ex, l, 3))
while True:
  # print("".join(ex))
  if j == 0: break
  curr_len = lens[j]
  curr_loc = locs[j]
  i = find_next_empty(ex, l, curr_len)
  if i is None or i > curr_loc: j-=1;continue
  ex[i:i+curr_len]=ex[curr_loc:curr_loc+curr_len]
  ex[curr_loc:curr_loc+curr_len] = ['.']*curr_len
  locs[j]=i
  j-=1
  
checksum = 0
for i in range(l):
  if ex[i] == '.': continue
  checksum += (i*int(ex[i]))
print(checksum)