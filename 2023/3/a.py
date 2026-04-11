with open(input(),'r')as f:
  lines=f.readlines()

DOT=ord('.')
NUMS=[ord(str(i)) for i in range(10)]
schematic=[]
for line in lines:
  schematic.append(bytearray(line.strip(), 'ascii'))

n,m=len(schematic),len(schematic[0])

neighbors=[
  [-1,-1],[-1,0],[-1,1],
  [0,-1],[0,1],
  [1,-1],[1,0],[1,1]
]
def sum_around(i,j):
  out=0
  done=set()
  for di,dj in neighbors:
    ni,nj=di+i,dj+j
    if (ni,nj) in done:
      continue
    if 0>ni or n<=ni or 0>nj or m<=nj: continue
    curr=schematic[ni][nj]
    if curr not in NUMS: continue
    c=[]
    it=nj
    while it<n:
      #print(f"going right from ({ni},{nj}) testing ({ni},{it}), val={schematic[ni][it]}={chr(schematic[ni][it])}")
      if (ni,it) in done or schematic[ni][it] not in NUMS:
        break
      done.add((ni,it))
      c.append(chr(schematic[ni][it]))
      it+=1
    it=nj-1
    while it>=0:
      #print(f"going left from ({ni},{nj}) testing ({ni},{it}), val={schematic[ni][it]}={chr(schematic[ni][it])}")
      print(it)
      if (ni,it) in done or schematic[ni][it] not in NUMS:
        break
      done.add((ni,it))
      #print("inserting", chr(schematic[ni][it]))
      c.insert(0,chr(schematic[ni][it]))
      it-=1
    #print(i,j,"".join(c))
    out+=int("".join(c))
  return out

out=0
for i in range(n):
  for j in range(m):
    curr=schematic[i][j]
    if curr in NUMS or curr==DOT:
      continue
    out+=sum_around(i,j)

print(out)