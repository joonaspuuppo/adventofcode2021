def read_lines_from_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines

def convert_lines_to_lists(lines):
    list_of_lists = []
    for line in lines:
        list = []
        for char in line:
            if char != "\n":
                list.append(int(char))
        list_of_lists.append(list)
    return list_of_lists

def find_low_points(list):
    low_points = []
    for i in range(len(list)):
        for j in range(len(list)):
            point = list[i][j]

            if i == 0:
                up = 11
                down = list[i+1][j]
            elif i == len(list) - 1:
                up = list[i-1][j]
                down = 11
            else:
                up = list[i-1][j]
                down = list[i+1][j]

            if j == 0:
                left = 11
                right = list[i][j+1]
            elif j == len(list) - 1:
                left = list[i][j-1]
                right = 11
            else:
                left = list[i][j-1]
                right = list[i][j+1]
            if point < up and point < down and point < left and point < right:
                low_points.append(point)
    return low_points

lines = read_lines_from_file("adventofcode2021_day9_input.txt")
list = convert_lines_to_lists(lines)
low_points = find_low_points(list)
sum = 0
for point in low_points:
    sum = sum + point + 1
print(sum)
print(low_points)

