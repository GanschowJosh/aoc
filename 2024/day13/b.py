import re

higher = 10000000000000

with open(input(), 'r') as f:
  text = f.read()

mraw = text.split("\n\n")
machines = []
for m in mraw:
  rows = m.split("\n")
  *button_strings, prize_string = rows
  buttons = []
  for button in button_strings:
    print(button)
    x,y = map(int, re.search(r'X\+(\d+),\s*Y\+(\d+)', button).groups())
    buttons.append((x,y))
  x,y = map(int, re.search(r'X\=(\d+),\s*Y\=(\d+)', prize_string).groups())
  machines.append((buttons, (x+higher,y+higher)))

toks = 0
for machine in machines:
  buttons, prize = machine
  tx,ty=prize
  ax,ay=buttons[0]
  bx,by=buttons[1]
  d=ax*by-ay*bx
  if d != 0:
    num_a = tx*by-ty*bx
    num_b = ax*ty-ay*tx
    if num_a%d!=0 or num_b%d!=0:
      continue
    a=num_a//d
    b=num_b//d
    if a<0 or b < 0:
      continue
    print(machine, num_a, num_b)
    toks += a*3+b

print(toks)
