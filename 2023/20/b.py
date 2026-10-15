from collections import defaultdict
from math import lcm
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

for k in mod_map.keys():
  if 'rx' in mod_map[k]:
    rx_parent=k

inputs=set(mod_state[rx_parent])
hits={name: [] for name in inputs}

q=deque()
cnt=0
done=False
while True:
  q.append(('broadcaster', 'broadcaster', 0)) #to, from, sig
  cnt+=1
  while q:
    t,f,s=q.popleft()
    #print(q)
    if t == 'rx' and s == 0: print(cnt);exit()
    if t == rx_parent and s == 1 and f in inputs:
      if not hits[f] or hits[f][-1]!=cnt:
        hits[f].append(cnt)
    if t not in mod_type: continue
    type_funcs[mod_type[t]](t,f,s,q)
    if all(len(v) >= 3 for v in hits.values()):
      periods={name:times[1]-times[0] for name, times in hits.items()}

      if all(times[2]-times[1] == periods[name] for name, times in hits.items()):
        print(lcm(*periods.values()))
      done=True
      break
  if done: break
