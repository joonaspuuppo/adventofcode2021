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

def find_least_common_bit_from_data(data, i):
    count0 = 0
    count1 = 0
    for line in data:
        if line[i] == "0":
            count0 = count0 + 1
        else:
            count1 = count1 + 1
    if count0 <= count1:
        return "0"
    return "1"

def find_oxygen_generator_rating(data):
    starts_with_string = ""
    for i in range(len(data[0]) - 1):
        starts_with_string = starts_with_string + find_most_common_bit_from_data(data, i)
        data = filter_data(data, starts_with_string)
        if len(data) == 1:
            return data[0]

def find_co2_scrubber_rating(data):
    starts_with_string = ""
    for i in range(len(data[0]) - 1):
        starts_with_string = starts_with_string + find_least_common_bit_from_data(data, i)
        data = filter_data(data, starts_with_string)
        if len(data) == 1:
            return data[0]

def filter_data(data, starts_with_string):
    filtered = []
    if starts_with_string == "":
        return data
    for line in data:
        if line.startswith(starts_with_string):
            filtered.append(line)
    return filtered

def calculate_life_support_rating(binary1, binary2):
    return int(binary1, 2) * int(binary2, 2)
    
data = read_data_from_file("adventofcode2021_day3_input.txt")
oxygen_generator_rating = find_oxygen_generator_rating(data)
data = read_data_from_file("adventofcode2021_day3_input.txt")
co2_scrubber_rating = find_co2_scrubber_rating(data)
print(calculate_life_support_rating(oxygen_generator_rating, co2_scrubber_rating))

