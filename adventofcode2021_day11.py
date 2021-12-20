grid = []

def read_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    grid.append([-1]*12)
    for line in lines:
        row = [-1]
        for i in range(len(line.strip())):
            row.append(int(line[i]))
        row.append(-1)
        grid.append(row)
    grid.append([-1]*12)

def print_grid():
    for row in grid:
        for number in row:
            if number != -1:
                print(number, end="")
        print()

def step():
    #increment all by 1
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            grid[i][j] += 1
    
    #flash all over 9
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            number = grid[i][j]
            if number == 10:
                flash(i, j)
    

    #count number of flashes
    flashes = 0
    for row in grid:
        for number in row:
            if number == 0:
                flashes += 1
    
    return flashes

def flash(i, j):
    grid[i][j] = 0
    xadj = [-1, -1, -1, 0, 0, 1, 1, 1]  
    yadj = [-1, 0, 1, -1, 1, 1, 0, -1]
    for x in range(len(xadj)):
        number = grid[i + yadj[x]][j + xadj[x]]
        if number > 0:
            grid[i + yadj[x]][j + xadj[x]] += 1
            if grid[i + yadj[x]][j + xadj[x]] > 9:
                flash(i + yadj[x], j + xadj[x])
            


    

read_file("adventofcode2021_day11_input.txt")
# print_grid()
# step()
# flashes = step()
# print("Flashes: ", flashes)
# print_grid()

# step()

total_flashes = 0
allflashat = 0
for i in range(1000):
    flashes = step()
    total_flashes += flashes
    if flashes == 100:
        allflashat = i
        break

print(total_flashes)
print("All flash at: ", allflashat)

