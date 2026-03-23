f = open("input.txt", "r")
lines = f.readlines()
f.close()

def is_safe(levels):
    if len(levels) < 2:
        return True
    dec = levels[1] - levels[0] < 0
    prev = levels[0]
    for num in levels[1:]:
        if dec:
            if prev < num:
                return False
            diff = prev - num
            if diff < 1 or diff > 3:
                return False
        else:
            if num < prev:
                return False
            diff = num - prev
            if diff < 1 or diff > 3:
                return False
        prev = num
    return True

safe = 0
for line in lines:
    line = list(map(int, line.strip().split()))
    if is_safe(line):
        safe += 1
    else:
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            if is_safe(new_line):
                safe += 1
                break

print(safe)
