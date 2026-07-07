from collections import deque

with open(input(), "r") as f:
  grid = [list(line.strip()) for line in f if line.strip()]

n, m = len(grid), len(grid[0])

for i in range(n):
  for j in range(m):
    if grid[i][j] == "S":
      si, sj = i, j
    if grid[i][j] == "E":
      ei, ej = i, j

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(si, sj):
  dist = [[-1] * m for _ in range(n)]
  q = deque([(si, sj)])
  dist[si][sj] = 0

  while q:
    i, j = q.popleft()
    for di, dj in dirs:
      ni, nj = i + di, j + dj
      if 0 <= ni < n and 0 <= nj < m:
        if dist[ni][nj] == -1 and grid[ni][nj] != "#":
          dist[ni][nj] = dist[i][j] + 1
          q.append((ni, nj))
  return dist

distS = bfs(si, sj)
distE = bfs(ei, ej)
base = distS[ei][ej]

track = []
for i in range(n):
  for j in range(m):
    if grid[i][j] != "#" and distS[i][j] != -1 and distE[i][j] != -1:
      track.append((i, j))

ans = 0
for ai, aj in track:
  for bi, bj in track:
    d = abs(ai - bi) + abs(aj - bj)
    if d == 0 or d > 20:
      continue

    cheated = distS[ai][aj] + d + distE[bi][bj]
    saved = base - cheated

    if saved >= 100:
      ans += 1

print(ans)
