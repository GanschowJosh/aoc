with open(input(), 'r') as f:
  lines=f.readlines()

time, distance=lines
time=time.split()
time=time[1:]
time=int("".join(time))
distance=distance.split()
distance=distance[1:]
distance=int("".join(distance))
print(time, distance)


n=0
for j in range(1,time):
  if j*(time-j) > distance:
    n+=1

print(n)