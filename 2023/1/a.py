with open(input(), 'r') as f:
  lines=f.readlines()

def find_first(s):
  for i in s:
    try:
      i=int(i)
      return i
    except:
      continue

def find_last(s):
  for i in range(len(s)-1,-1,-1):
    try:
      i=int(s[i])
      return i 
    except:
      continue
s=0
for line in lines:
  s+=(find_first(line)*10)
  s+=find_last(line)

print(s)