from functools import cache

with open(input(), 'r') as f:
  lines=f.readlines()

rows=[]
arrs=[]
for line in lines:
  row,arr=line.strip().split()
  rows.append("?".join([row]*5))
  arrs.append(tuple(map(int, arr.split(",")))*5)


def handle_line(row, arr):
  @cache
  def count(i, group, run):
    if i == len(row):
      if run:
        return int(group == len(arr)-1 and run == arr[group])
      return int(group == len(arr))

    found=0
    options=".#" if row[i]=='?' else row[i]
    for c in options:
      if c=='#':
        if group < len(arr) and run < arr[group]:
          found += count(i+1, group, run+1)
      elif run:
        if group < len(arr) and run == arr[group]:
          found += count(i+1, group+1, 0)
      else:
        found += count(i+1, group, 0)
    return found

  return count(0, 0, 0)
  
results=[]
for row, arr in zip(rows, arrs):
  results.append(handle_line(row, arr))
print(sum(results))
