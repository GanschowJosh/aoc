from collections import defaultdict
with open(input(),'r') as f:
  lines=f.readlines()



mod_type={}
mod_map={}
mod_state={}

def broad(to, fr, recv, q):
  for friend in mod_map[to]:
    q.append((friend, to, recv))

def flip_flop(to, fr, recv, q):
  if recv == 1: return
  mod_state[to] = int(not mod_state[to])
  for friend in mod_map[to]:
    q.append((friend, to, mod_state[to]))

def conj(to, fr, recv, q):
  mod_state[to][fr]=recv
  a=int(not all(mod_state[to].values()))
  for friend in mod_map[to]:
    q.append((friend, to, a))

type_funcs={
  'b': broad,
  '%': flip_flop,
  '&': conj
}

names=set()
for line in lines:
  line=line.strip().split(' -> ')
  name=line[0]
  friends=list(line[1].split(', '))
  ctype='b'
  if name != 'broadcaster':
    ctype=name[0]
    name=name[1:]
  names.add(name)
  mod_type[name]=ctype
  mod_map[name]=friends
  if ctype=='&':
    mod_state[name]={}
  else:
    mod_state[name]=0

for src, friends in mod_map.items():
  for dst in friends:
    if dst in mod_type and mod_type[dst]=='&':
      mod_state[dst][src]=0

print(mod_map)
print(mod_type)

from collections import deque

def refresh():
  for name in names:
    if mod_type[name] == '&':
      mod_state[name]=defaultdict(int)
    else:
      mod_state[name]=0

def check():
  good=True
  for name in names:
    if mod_type[name] == '&':
      good &= any(mod_state[name].values())
    else:
      good &= mod_state[name]
    if not good:
      return good
  return good

low, high=0,0
q=deque()
for _ in range(1000):
  q.append(('broadcaster', 'broadcaster', 0)) #to, from, sig
  while q:
    t,f,s=q.popleft()
    #print(q)
    if s: high+=1
    else: low+=1
    if t not in mod_type or (mod_type[t] == '%' and s==1): continue
    type_funcs[mod_type[t]](t,f,s,q)

print(low*high)