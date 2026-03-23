with open(input(), "r") as f:
  lines = f.readlines()
  l = lines[0].strip()

ranges = l.split(",")
# print(ranges)
for r in range(len(ranges)):
  t = (ranges[r].split("-")[0], ranges[r].split("-")[1])
  t = (int(t[0]), int(t[1]))
  ranges[r] = t

def isvalid(num):
  num = str(num)
  l = len(num)
  # print("length", l)
  l2 = int(l / 2)
  # print("l2", l2)
  if l % 2 != 0: return True
  # print(num[:l2], num[l2:])
  if num[:l2] == num[l2:]: return False
  return True

invalid_sum = 0
for r0, r1 in ranges:
  for i in range(r0, r1+1):
    # print(f"checking {i}")
    if not isvalid(i): invalid_sum+=i;print(i)

print(invalid_sum)