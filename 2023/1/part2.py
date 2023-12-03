f = open("input-data.txt", "r")
calibration_sum = 0
for line in f:
    numbers = []
    print(line)
    for i in range(len(line)):
        if line[i].isdigit():
           numbers.append(line[i])
        else:
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    numbers.append(str(d+1))

    calibration_sum += int(numbers[0] + numbers[-1]) 

print("calibration_sum", calibration_sum)
f.close()
