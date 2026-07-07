

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

n=2000
su=0
for num in nums:
  su+=rep(num, n)

print(su)