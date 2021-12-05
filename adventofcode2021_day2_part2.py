def read_course_from_file(filename):
    course = []
    file = open(filename, "r")
    for line in file:
        course.append(line)
    file.close()
    return course

def calculate_horizontal_position(course):
    horizontal_pos = 0
    for line in course:
        if line.startswith("f"):
            increase = int(line.split(" ")[1])
            horizontal_pos = horizontal_pos + increase
    return horizontal_pos

def calculate_depth(course):
    aim = 0
    depth = 0
    for line in course:
        if line.startswith("u"):
            delta = int(line.split(" ")[1])
            aim = aim - delta
        if line.startswith("d"):
            delta = int(line.split(" ")[1])
            aim = aim + delta
        if line.startswith("f"):
            delta = int(line.split(" ")[1])
            depth = depth + delta * aim
    return depth
        
course = read_course_from_file("adventofcode2021_day2_input.txt")
horizontal_position = calculate_horizontal_position(course)
depth = calculate_depth(course)
print (horizontal_position * depth)

