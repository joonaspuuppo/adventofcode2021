def count_number_of_increases(numbers):
    count = 0
    for i in range(1, len(numbers)):
        if (numbers[i] > numbers[i-1]):
            count = count + 1
    return count

def count_number_of_sum_increases(numbers):
    count = 0
    sums = []
    for i in range(len(numbers) - 2):
        sum = numbers[i] + numbers[i+1] + numbers[i+2]
        sums.append(sum)
    return count_number_of_increases(sums)

def read_numbers_from_file(filename):
    numbers = []
    file = open(filename, "r")
    for line in file:
        numbers.append(int(line))
    file.close()
    return numbers

numbers = read_numbers_from_file("adventofcode2021_day1_input.txt")
print(count_number_of_increases(numbers))
print(count_number_of_sum_increases(numbers))


