with open(input(), 'r') as f:
  line = f.readline()

stones = list(map(int, line.split()))

start = len(stones)
times = 25
for i in range(times):
  new = []
  for idx, stone in enumerate(stones):
    if stone == 0: new.append(1)
    elif len(str(stone))%2==0: 
      st = str(stone)
      # print(st)
      l = len(str(stone))//2
      s1 = int(st[:l])
      s2 = int(st[l:])
      new.append(s1)
      new.append(s2)
      start += 1
    else:
      new.append(stone*2024)
  stones = new[:]
  # print(stones)
print(len(stones))
print(start)