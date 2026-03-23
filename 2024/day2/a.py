f = open("input.txt", "r")
lines = f.readlines()
f.close()

safe = 0
for line in lines:
    line = list(map(int, line.strip().split()))
    prev = -1
    dec = line[1] - line[0] < 0
    for num in line:
        if dec:
            if prev == -1:
                prev = num
                continue
            if prev < num:
                print(num, prev)
                break
            if prev - num < 1 or prev - num > 3:
                break
        else:
            if prev == -1:
                prev = num
                continue
            if num < prev:
                print(num, prev)
                break
            if num - prev < 1 or num - prev > 3:
                break
        prev = num
    else:
        safe += 1
print(safe)