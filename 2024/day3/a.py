f = open("input.txt", "r")
lines = f.readlines()
f.close()

def mul(x,y):
    return x*y

string = ''.join(line.strip() for line in lines)
import re
re_string = r'mul\(-?\d+,-?\d+\)'
matches = re.findall(re_string, string)
print(matches)

total = 0
for match in matches:
    total += eval(match)
print(total)