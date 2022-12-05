with open('/Users/shankar_aa/Desktop/AoC-2022/Day 1/input.txt', 'r') as fh:
    for line in fh:
        line = line.rstrip("\n")
        print(line)
        if line.strip():
            print('The line is NOT empty ->', line)
        else:
            print('The line is empty')