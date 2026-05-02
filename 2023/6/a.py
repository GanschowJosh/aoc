with open(input(), 'r') as f:
  lines=f.readlines()

time, distance=lines
time=time.split()
time=list(map(int, time[1:]))
distance=distance.split()
distance=list(map(int, distance[1:]))
print(time, distance)

pr=1
for i in range(len(time)):
  # i+=1
  ct,cd=time[i],distance[i]
  n=0
  for j in range(1,ct):
    if j*(ct-j) > cd:
      n+=1
  pr*=n

print(pr)