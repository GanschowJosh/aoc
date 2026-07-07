from collections import deque, defaultdict
CORRUPTED=ord('#')
UNCORRUPTED=ord('.')
PATH=ord('O')

def print_matrix(matrix):
  m=max(len(chr(matrix[i][j])) for i in range(len(matrix)) for j in range(len(matrix[0])))
  for row in matrix:
    for i, val in enumerate(row):
      print(str(chr(val)).ljust(m, " "), end=" \n"[i==len(row)-1])

with open(input(), 'r') as f:
  lines=f.readlines()

n,m=int(input("n: "))+1,int(input("m: "))+1
gr=[bytearray(n) for _ in range(m)]
for i in range(n):
  for j in range(m):
    gr[i][j]=UNCORRUPTED

coords=[]
for line in lines:
  line=line.strip()
  X,Y=map(int, line.split(","))
  coords.append((Y,X))

steps=int(input("steps: "))
for i in range(steps):
  cn,cm=coords[i]
  gr[cn][cm]=CORRUPTED

#print_matrix(gr)

q=deque({(0,0,0)})
v=[bytearray(n) for _ in range(m)]
v[0][0]=1
neighbors=[
  [-1,0],
  [0,-1],[0,1],
  [1,0]
]
while q:
  ci,cj,cd=q.popleft()
  #print(ci,cj,cd)
  #print(q)
  if ci==n-1 and cj==m-1:
    print(cd)
    exit()
  for di,dj in neighbors:
    ni,nj=di+ci,dj+cj
    if 0 <= ni < n and 0 <= nj < m and gr[ni][nj]!=CORRUPTED and v[ni][nj]==0:
      q.append((ni,nj,cd+1))
      v[ni][nj]=1
