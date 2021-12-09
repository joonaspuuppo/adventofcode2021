def read_lines_from_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines

def split_lines(lines):
    list = []
    for line in lines:
        list.append(line.split(" | ")[1])
    return list

def count_unique_digits(outputs):
    count = 0
    for line in outputs:
        for digit in line.split(" "):
            if len(digit.strip()) == 2 or len(digit.strip()) == 3 or len(digit.strip()) == 4 or len(digit.strip()) == 7:
                count = count + 1
    return count

lines = read_lines_from_file("adventofcode2021_day8_input.txt")
count = count_unique_digits(split_lines(lines))
print(count)