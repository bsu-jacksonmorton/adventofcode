f = open("input-data.txt", "r")
calibration_sum = 0
for line in f:
    print(line)
    start = 0
    end = len(line) - 1
    num = ""
    while start <= end:
        if line[start].isdigit():
            num += line[start]
            break
        start += 1
    while end >= start:
        if line[end].isdigit():
            num += line[end]
            break
        end -= 1
    calibration_sum += int(num)

print("calibration_sum", calibration_sum)
f.close()
