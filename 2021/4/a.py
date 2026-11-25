with open(input(), 'r') as f:
  lines=f.readlines()

call=list(map(int, lines[0].split(',')))
boards=[]

curr=[]
for line in lines[2:]:
  if not line.strip():
    boards.append(curr)
    curr=[]
    continue
  curr.append(list(map(int, line.split())))

boards.append(curr)

def score(brd, a):
  seen=set(call[:a])
  return sum(x for row in brd for x in row if x not in seen)

def feas(a):
  seen=set(call[:a])
  for board in boards:
    if any(all(x in seen for x in row) for row in board) or any(all(x in seen for x in col) for col in zip(*board)):
      return score(board, a)
  return None

l,r=0,len(call)
while l < r:
  mid=(l+r)//2
  if feas(mid) is not None:
    r=mid
  else:
    l=mid+1
print(feas(l)*call[l-1])