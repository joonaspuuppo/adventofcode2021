def read_data_from_file(filename):
    data = []
    file = open(filename, "r")
    for line in file:
        data.append(line)
    file.close()
    return data

def find_most_common_bit_from_data(data, i):
    count0 = 0
    count1 = 0
    for line in data:
        if line[i] == "0":
            count0 = count0 + 1
        else:
            count1 = count1 + 1
    if count0 > count1:
        return "0"
    return "1"

def calculate_gamma(data):
    binary_as_string = ""
    for i in range(len(data[0]) - 1):
        binary_as_string = binary_as_string + find_most_common_bit_from_data(data, i)
    return binary_as_string

def invert_binary_as_string(binary_as_string):
    inverted_string = ""
    for ch in binary_as_string:
        if ch == "0":
            inverted_string = inverted_string + "1"
        else:
            inverted_string = inverted_string + "0"
    return inverted_string

def calculate_power_consumption(binary1, binary2):
    return int(binary1, 2) * int(binary2, 2)

data = read_data_from_file("adventofcode2021_day3_input.txt")
gamma = calculate_gamma(data)
epsilon = invert_binary_as_string(gamma)
print(calculate_power_consumption(gamma, epsilon))




