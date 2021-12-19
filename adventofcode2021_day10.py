import statistics


CLOSING_CHARACTERS = ")]}>"
OPENING_CHARACTERS = "([{<"
ERROR_POINTS = [3, 57, 1197, 25137]
COMPLETION_POINTS = [1, 2, 3, 4]

def read_lines_from_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines

def is_legal(line, i, errors, completions):
    if is_closing_character(line[i]):
        print("Not an opening character!")
        return False
    if i == len(line) - 1:
        print("End of line!")
        return False
    opening_chars = [line[i]]
    for x in range(i+1, len(line) - 1):
        char = line[x]
        if len(opening_chars) != 0:
            closing_char = find_pair(opening_chars[len(opening_chars) - 1])
        if char in OPENING_CHARACTERS:
            opening_chars.append(char)
        else:
            if char != closing_char:
                #print("Expected {} but found {} instead".format(closing_char, char))
                errors.append(char)
                return False
            else:
                #print("Chunk OK!")
                opening_chars.pop()
    if len(opening_chars) != 0:
        completion = []
        while len(opening_chars) > 0:
            char = opening_chars.pop()
            completion.append(find_pair(char))
        completions.append(completion)


    return True


def find_pair(char):
    for i in range(len(CLOSING_CHARACTERS)):
        if char == CLOSING_CHARACTERS[i]:
            return OPENING_CHARACTERS[i]
        if char == OPENING_CHARACTERS[i]:
            return CLOSING_CHARACTERS[i]


def is_closing_character(char):
    if char in CLOSING_CHARACTERS:
        return True
    return False

def is_opening_character(char):
    if char in OPENING_CHARACTERS:
        return True
    return False



lines = read_lines_from_file("adventofcode2021_day10_input.txt")
errors = []
completions = []
for line in lines:
    is_legal(line, 0, errors, completions)

sum = 0
for error in errors:
    for i in range(len(ERROR_POINTS)):
        if error == CLOSING_CHARACTERS[i]:
            sum += ERROR_POINTS[i]
print("Part one: ", sum)

sums = []
for completion in completions:
    sum = 0
    for char in completion:
        sum = sum * 5
        for i in range(len(COMPLETION_POINTS)):
            if char == CLOSING_CHARACTERS[i]:
                sum += COMPLETION_POINTS[i]
    sums.append(sum)

print("Part 2: ", statistics.median(sums))


                


