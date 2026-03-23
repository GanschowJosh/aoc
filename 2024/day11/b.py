from functools import lru_cache
with open(input(), 'r') as f:
  line = f.readline()

stones = list(map(int, line.split()))

@lru_cache(maxsize=None)
def count(val, left):
  if left == 0:
    return 1
  
  if val == 0:
    return count(1, left-1)
  
  s = str(val)
  if len(s)%2==0:
    l = len(s)//2
    s1 = int(s[:l])
    s2 = int(s[l:])
    return count(s1,left-1)+count(s2,left-1)

  return count(val*2024,left-1)

s = 0
times = 75
for v in stones:
  s+=count(v, times)
print(s)