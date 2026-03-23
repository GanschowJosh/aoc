from functools import lru_cache
from copy import deepcopy

class Node:
  def __init__(self, val):
    self.val = val
    self.right_child = None
    self.left_child = None

with open(input(), 'r') as f:
  lines = list(map(str.strip, f.readlines()))
  lines = list(map(list, lines))

for i, line in enumerate(lines):
  if 'S' in line:
    start = (i, line.index('S'))

rows, cols = len(lines), len(lines[0])

cache = {}

def find_next(currNode, diagram):
  if currNode is None: return
  x,y = currNode.val
  if x>=rows or y<0 or y>=cols:
    return None
  while 0 <= x < rows and 0 <= y < cols and diagram[x][y] != '^':
    x += 1
  if x>=rows or y<0 or y>=cols:
    return None
  if (x,y) in cache:
    return cache[(x,y)]
  out = Node((x,y))
  cache[(x,y)] = out
  out.left_child = find_next(Node((x,y-1)),diagram)
  out.right_child = find_next(Node((x,y+1)),diagram)
  return out

tree = find_next(Node(start), lines)

def print_tree(root: Node):
  if not root: return
  print(root.val)
  print_tree(root.right_child)
  print_tree(root.left_child)

@lru_cache(maxsize=None)
def count(node: Node):
  if not node: return 1
  return count(node.left_child) + count(node.right_child)
# print_tree(tree)
print(count(tree))