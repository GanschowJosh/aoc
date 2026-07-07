from collections import deque

with open(input(), 'r') as f:
  lines=f.readlines()

nums = list(map(int, (line.strip() for line in lines)))

def mix(n, v):
  return n^v

def prune(n):
  return n%16777216

def next_num(n):
  b64=n*64
  n=mix(n, b64)
  n=prune(n)

  b32=n//32
  n=mix(n,b32)
  n=prune(n)

  b2048=n*2048
  n=mix(n,b2048)
  n=prune(n)

  return n

def rep(i, times):
  for _ in range(times):
    i=next_num(i)
  return i

#calculate sequences for each monkey

n=len(nums)
seqs=[dict() for _ in range(n)]
seen=set()
for i, num in enumerate(nums):
  q=deque(maxlen=4)
  last=num%10
  for _ in range(2000):
    num=next_num(num)
    curr=num%10
    q.append(curr-last)
    if len(q) == 4:
      t=tuple(q)
      if t not in seqs[i]:
        seqs[i][t]=curr
        seen.add(t)
    last=curr

best=0
best_seq=None
for t in seen:
  curr=0
  for seq in seqs:
    if t in seq:
      curr+=seq[t]
  if curr > best:
    best=curr
    best_seq=t

print(best_seq)
print(best)
#print(seqs)