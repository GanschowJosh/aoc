with open(input(), "r") as f:
  lines=f.readlines()
days=list(map(int, lines[0].split(",")))

def matrix_multiply(X,Y):
  if len(X[0]) != len(Y):
    return False
  return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def power_matrix(A, r):
  B = A
  n = len(A)
  S = [[int(x==y) for x in range(n)] for y in range(n)]
  while(r > 0):
    if r%2 == 1:
      S = matrix_multiply(S,B)
    B = matrix_multiply(B,B)
    r = r//2
  return S

P=[
  [0,0,0,0,0,0,1,0,1],
  [1,0,0,0,0,0,0,0,0],
  [0,1,0,0,0,0,0,0,0],
  [0,0,1,0,0,0,0,0,0],
  [0,0,0,1,0,0,0,0,0],
  [0,0,0,0,1,0,0,0,0],
  [0,0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,0]
]
n=80
start=[0 for _ in range(9)]
for d in days:
  start[d]+=1
s=[]
s.append(start)
print(sum(matrix_multiply(s,power_matrix(P,n))[0]))