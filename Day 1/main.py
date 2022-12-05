'''
First Attempt Very ass
array = []
with open('/Users/shankar_aa/Desktop/AoC-2022/Day 1/input.txt', 'r') as f:
    line = int(f.readline())
    print(line)
    while line != None:
        line = line.rstrip
        line = int(f.readline())
        array.append(line)

print(array)
'''
### Part 1
array = []
tempNum = 0

with open('/Users/shankar_aa/Desktop/AoC-2022/Day 1/input.txt', 'r') as f:
    for line in f:
        line.rstrip('\n') ## Remove \n at the end of the line

        if line.strip(): ## Check if the line is empty or not
            line = int(line) ## Convert line to int
            tempNum = tempNum + line ## Add the values of the elves together
        else:
            array.append(tempNum) ## Add the final value of the elf's calories together
            print(f'Appended {tempNum} ') ## Append to array
            tempNum = 0 ## Reset Tempnumber
            print(f'Reset tempNum to {tempNum}') ## debug statement

array.sort(reverse=True)
print(array)

### Part 2
output = array[0]+array[1]+array[2]
print(output)