def countNumberOfIncreases(numbers):
    count = 0
    for i in range(1, len(numbers)):
        if (numbers[i] > numbers[i-1]):
            count = count + 1
    return count

def countNumberOfSumIncreases(numbers):
    count = 0
    sums = []
    for i in range(len(numbers) - 2):
        sum = numbers[i] + numbers[i+1] + numbers[i+2]
        sums.append(sum)
    return countNumberOfIncreases(sums)

def readNumbersFromFile(filename):
    numbers = []
    file = open(filename, "r")
    for line in file:
        numbers.append(int(line))
    file.close()
    return numbers

numbers = readNumbersFromFile("adventofcode2021_day1_input.txt")
print(countNumberOfIncreases(numbers))
print(countNumberOfSumIncreases(numbers))


