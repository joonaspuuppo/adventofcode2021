def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def get_template(lines):
    template = lines[0].strip()
    return template

def get_rules(lines):
    pairs = []
    pairs_with_added_letters = []
    rules = []
    for i in range(2, len(lines)):
        pair = lines[i].split(" ", 1)[0]
        pairs.append(pair)
        added = lines[i].split(" -> ")[1].strip()
        pair_with_added_letter = pair[0] + added
        pairs_with_added_letters.append(pair_with_added_letter)
    rules.append(pairs)
    rules.append(pairs_with_added_letters)
    return rules

def step(template, rules) -> str:
    line = ""
    pairs = rules[0]
    pairs_with_added_letters = rules[1]
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        for j in range(len(pairs)):
            if pair == pairs[j]:
                line += pairs_with_added_letters[j]
                break
    line += template[len(template) - 1]
    return line


lines = read_file("adventofcode2021_day14_input.txt")
template = get_template(lines)
rules = get_rules(lines)
pairs = rules[0]
pairs_with_added_letters = rules[1]
for i in range(10):
    line = step(template, rules)
    #print(line)
    template = line

chars = list(set(line))
print (chars)
counts = []
for char in chars:
    counts.append(0)

for char in line:
    for i in range(len(chars)):
        if char == chars[i]:
            counts[i] += 1
            break

print(counts)

print(max(counts) - min(counts))





        



