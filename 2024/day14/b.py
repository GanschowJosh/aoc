from math import prod
import re
import time

with open(input(), 'r') as f:
  lines = f.readlines()

robots = []
for line in lines:
  praw, vraw = line.split()
  px, py = map(int, re.search(r'p\=(\d+),(\d+)', praw).groups())
  vx, vy = map(int, re.search(r'v\=(-?\d+),(-?\d+)', vraw).groups())
  robots.append(((px,py),(vx,vy)))

def pos(robot, steps, rows, cols):
  start, velo = robot
  nx=start[0]+steps*velo[0]
  nx%=cols
  ny=start[1]+steps*velo[1]
  ny%=rows
  return (nx, ny)

m = 10000
rows = 103
cols = 101

def printarr(arr):
  for row in arr:
    print("".join(map(str, row)))

def count(thing, arr):
  c = 0
  for t in arr:
    if t == thing: c += 1
  return c

for i in range(m):
  curr = [[0]*cols for _ in range(rows)]
  for robot in robots:
    nx,ny = pos(robot, i, rows, cols)
    curr[ny][nx]=1
  # printarr(curr)
  yes = False
  for row in curr:
    if "1"*10 in "".join(map(str, row)): yes = True
  if yes: printarr(curr); print(i)
