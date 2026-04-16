import sys
from functools import lru_cache

def parse(inp):
  with open(inp, 'r') as f:
    content = f.read()
  blocks = [b for b in content.strip().split("\n\n") if b.strip()]

  shapes = []
  regions_block = None

  for b in blocks:
    # print(b)
    if "x" in b.splitlines()[-1]:
      regions_block = b
    else:
      lines = [ln.rstrip("\n") for ln in b.splitlines() if ln.strip() and ":" not in ln]
      shapes.append(lines)


  regions = []
  for ln in regions_block.splitlines():
    ln = ln.strip()
    if not ln:
      continue
    dims, *nums = ln.split()
    dims = dims[:-1]
    w, h = map(int, dims.split("x"))
    counts = list(map(int, nums))
    regions.append((w, h, counts))

  return shapes, regions

def cells_from_3x3(grid3):
  pts = []
  for y in range(3):
    for x in range(3):
      if grid3[y][x] == '#': pts.append((x,y))
  return pts

def normalize(pts):
  minx = min(x for x, _ in pts)
  miny = min(y for _, y in pts)
  pts = sorted((x-minx, y-miny) for x, y in pts)
  return tuple(pts)

def rot90(pts):
  return [(y, -x) for x,y in pts]

def flipx(pts):
  return [(-x,y) for x,y in pts]

def all_orientations(pts):
  seen = set()
  out = []
  curr = pts[:]
  for _ in range(4):
    for f in (False, True):
      p = flipx(curr) if f else curr
      n = normalize(p)
      if n not in seen:
        seen.add(n)
        out.append(n)
    curr = rot90(curr)
  return out

def bbox(pts):
  maxx = max(x for x, y in pts)
  maxy = max(y for x, y in pts)
  return (maxx+1, maxy+1)


def placements_for_piece(orients, W, H):
  res = []
  for o in orients:
    ow, oh = bbox(o)
    for dx in range(W-ow+1):
      for dy in range(H-oh+1):
        mask = 0
        cells_idx = []
        for x,y in o:
          xx,yy = x+dx, y+dy
          idx = yy*W+xx
          cells_idx.append(idx)
          mask |= (1<<idx)
        res.append((mask, cells_idx))
  return res

def can_tile_region(W, H, shape_orients, counts):
  board_cells = W * H
  if sum(counts) == 0:
    return True

  areas = [len(shape_orients[i][0]) for i in range(len(shape_orients))]
  need = sum(areas[i] * counts[i] for i in range(len(counts)))
  if need > board_cells:
    return False

  place_masks = []
  for si in range(len(shape_orients)):
    masks = [pmask for (pmask, _) in placements_for_piece(shape_orients[si], W, H)]
    place_masks.append(masks)

  counts0 = tuple(counts)

  sys.setrecursionlimit(10**6)

  @lru_cache(maxsize=None)
  def dfs(used_mask, counts_left):
    if sum(counts_left) == 0:
      return True

    best_s = -1
    best_opts = None

    for s, c in enumerate(counts_left):
      if c == 0:
        continue
      opts = [m for m in place_masks[s] if (m & used_mask) == 0]
      if not opts:
        return False
      if best_opts is None or len(opts) < len(best_opts):
        best_opts = opts
        best_s = s
        if len(best_opts) == 1:
          break

    best_opts.sort(key=lambda m: (m & -m).bit_length())

    for pmask in best_opts:
      nxt = list(counts_left)
      nxt[best_s] -= 1
      if dfs(used_mask | pmask, tuple(nxt)):
        return True

    return False
  
  return dfs(0, counts0)

shapes, regions = parse(input())
print(shapes, regions)

shape_orients = []
for g in shapes:
  pts = cells_from_3x3(g)
  # print(pts)
  orients = all_orientations(pts)
  # print(orients)
  shape_orients.append(orients)

ok = 0
for (W,H,counts) in regions:
  if can_tile_region(W,H,shape_orients, counts): ok += 1

print(ok)

# with open(input(), 'r') as f:
#   lines = [line.rstrip() for line in f]

# # print(lines)
# areas = []
# i = 0
# while len(areas) < 6:
#   if lines[i].endswith(":"):
#     cnt = 0
#     for j in range(i+1, i+4):
#       cnt += lines[j].count("#")
#     areas.append(cnt)
#     i+=4
#   else:
#     i+=1

# ans = 0
# print(i)
# for line in lines[i:]:
#   if not line: continue
#   dims, *nums = line.replace(":","").split()
#   print(dims, nums)
#   w,h = map(int, dims.split("x"))
#   counts = list(map(int, nums))
#   print(counts, areas)

#   total = sum(areas[k]*counts[k] for k in range(6))
#   if total < w*h: ans += 1

# print(ans)