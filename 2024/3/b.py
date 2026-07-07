import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

input_memory = ''.join(line.strip() for line in lines)

mul_regex = r'mul\((\d+),(\d+)\)'
do_regex = r'do\(\)'
dont_regex = r"don't\(\)"

mul_matches = [(m.group(), m.start(), m.end(), int(m.group(1)), int(m.group(2))) for m in re.finditer(mul_regex, input_memory)]
do_matches = [m.start() for m in re.finditer(do_regex, input_memory)]
dont_matches = [m.start() for m in re.finditer(dont_regex, input_memory)]

control_events = sorted([(pos, 'do') for pos in do_matches] + [(pos, 'dont') for pos in dont_matches])

enabled = True 
event_index = 0
result_sum = 0

for mul in mul_matches:
    mul_start = mul[1]
    while event_index < len(control_events) and control_events[event_index][0] < mul_start:
        enabled = (control_events[event_index][1] == 'do')
        event_index += 1
    if enabled:
        result_sum += mul[3] * mul[4]

print(result_sum)
