with open(input(), 'r') as f:
  lines=f.readlines()

hist=[]
for line in lines:
  hist.append(list(map(int, line.strip().split())))

def next_seq(seq):
  if len(seq) == 1: return [0]
  out=[]
  for i, s in enumerate(seq):
    if i == 0: continue
    out.append(s-seq[i-1])
  return out

su=0
for h in hist:
  curr = h
  done=[]
  while not all(c==0 for c in curr):
    done.append(curr)
    curr=next_seq(curr)
  carry=0
  for d in reversed(done):
    carry+=d[-1]
  su+=carry

print(su)