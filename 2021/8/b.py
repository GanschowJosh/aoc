with open(input(),'r') as f:
  lines=f.readlines()

tot = 0
for line in lines:
  print(lines)
  mp={}
  rmp={}
  nums=line.split(' | ')[0].split()
  ot=line.split(' | ')[1].split()
  done=set()
  for num in nums: # get the easy ones
    if len(num) == 2:
      mp[1]=frozenset(num)
      rmp[frozenset(num)]=1
      done.add(frozenset(num))
    if len(num) == 3:
      mp[7]=frozenset(num)
      rmp[frozenset(num)]=7
      done.add(frozenset(num))
    if len(num) == 4:
      mp[4]=frozenset(num)
      rmp[frozenset(num)]=4
      done.add(frozenset(num))
    if len(num) == 7:
      mp[8]=frozenset(num)
      rmp[frozenset(num)]=8
      done.add(frozenset(num))
  for num in nums:
    fz=frozenset(num)
    if len(fz)!=6: continue
    if mp[4] <= fz: digit=9
    elif mp[1]<=fz: digit=0
    else:           digit=6
    mp[digit]=fz
    rmp[fz]=digit
    done.add(fz)
  for num in nums:
    fz=frozenset(num)
    if len(fz)!=5: continue
    if mp[1] <= fz: digit=3
    elif fz<=mp[9]: digit=5
    else:           digit=2
    mp[digit]=fz
    rmp[fz]=digit
    done.add(fz)
  print(mp)
  if len(done) != 10:
    print(f"missing some: {mp}")
  for i in range(4):
    fz=frozenset(ot[i])
    print(rmp[fz],end='')
    tot+=(rmp[fz]*10**(3-i))
  print()
print(tot)