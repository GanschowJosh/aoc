with open(input(), 'r') as f:
  lines=f.readlines()


N=len(lines[0])-1
def findc(iter, l):
  c=[0]*l
  for line in iter:
    for i in range(len(c)):
      if line & (1 << i):
        c[i]+=1
      else:
        c[i]-=1
      # print(c)

  return list(reversed(c))

c=findc(list(map(lambda x: int(x.strip(),2), lines)), N)

#find ox
lefto=set(map(lambda x: int(x,2), lines))
leftc=set(map(lambda x: int(x,2), lines))
curr = 0
while len(lefto) > 1 or len(leftc) > 1  and curr < N:
  co=findc(lefto,N)
  c2=findc(leftc,N)
  coc=co[curr]
  c2c=c2[curr]
  trgo=int(coc >= 0)
  trgc=int(c2c < 0)
  tormvo=set()
  tormvc=set()
  # print(23 & 1<<(N-curr-1), trg, cco)
  if len(lefto) > 1:
    for lft in lefto:
      if bool(lft & (1 << (N-curr-1))) != bool(trgo):
        tormvo.add(lft)
    lefto.difference_update(tormvo)
  if len(leftc) > 1:
    for lft in leftc:
      if bool(lft & (1 << (N-curr-1))) != bool(trgc):
        tormvc.add(lft)
    leftc.difference_update(tormvc)
  # print(lefto)
  curr+=1

ox=lefto.pop()
co=leftc.pop()

print(ox*co)