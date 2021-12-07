class PipeNetwork:

    def __init__(self, rows, cols):
        self.network = [[0 for i in range(cols)] for j in range(rows)]
        self.overlaps = 0

    def add_pipe_at_coordinate(self, x, y):
        self.network[y][x] = self.network[y][x] + 1
        #print("Pipe added at: {}, {}".format(x, y) )

    def find_overlaps(self):
        for i in range(len(self.network[0])):
            for j in range(len(self.network[0])):
                if self.network[i][j] > 1:
                    self.overlaps = self.overlaps + 1

    def draw_pipe(self, x1, y1, x2, y2):
        if x1 == x2:
            #vertical pipe
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    self.add_pipe_at_coordinate(x1, i)
            else:
                for i in range(y1, y2 - 1, -1):
                    self.add_pipe_at_coordinate(x1, i)
        elif y1 == y2:
            #horizontal pipe
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    self.add_pipe_at_coordinate(i, y1)
            else:
                for i in range(x1, x2 - 1, -1):
                    self.add_pipe_at_coordinate(i, y1)
        else:
            delta = abs(x1 - x2) #same as abs(y1 - y2)
            x_is_increasing = x1 < x2
            y_is_increasing = y1 < y2
            for i in range(delta + 1):
                if x_is_increasing and y_is_increasing:
                    self.add_pipe_at_coordinate(x1 + i, y1 + i)
                elif x_is_increasing and not y_is_increasing:
                    self.add_pipe_at_coordinate(x1 + i, y1 - i)
                elif not x_is_increasing and y_is_increasing:
                    self.add_pipe_at_coordinate(x1 - i, y1 + i)
                elif not x_is_increasing and not y_is_increasing:
                    self.add_pipe_at_coordinate(x1 - i, y1 - i)
    
    def read_lines_from_file(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines

    def construct_network(self, lines):
        for line in lines:
            coords = line.strip().split(" -> ")
            coord1 = coords[0].split(",")
            coord2 = coords[1].split(",")
            self.draw_pipe(int(coord1[0]), int(coord1[1]), int(coord2[0]), int(coord2[1]))
        self.find_overlaps()

network = PipeNetwork(1000, 1000)
network.construct_network(network.read_lines_from_file("adventofcode2021_day5_input.txt"))
print(network.overlaps)