from math import prod
import re

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

steps = 100
rows = 103
cols = 101
midx = cols // 2
midy = rows // 2
in1 = lambda pt: pt[0]<midx and pt[1]<midy
in2 = lambda pt: pt[0]>midx and pt[1]<midy
in3 = lambda pt: pt[0]<midx and pt[1]>midy
in4 = lambda pt: pt[0]>midx and pt[1]>midy

counts = [0]*4
for robot in robots:
  n = pos(robot, steps, rows, cols)
  if in1(n):counts[0]+=1
  if in2(n):counts[1]+=1
  if in3(n):counts[2]+=1
  if in4(n):counts[3]+=1


print(prod(counts))