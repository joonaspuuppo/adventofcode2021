class BingoNumber:

    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked


class BingoBoard:

    next_id = 0

    def __init__(self, numbers):
        self.numbers = numbers
        self.id = BingoBoard.next_id
        BingoBoard.next_id = BingoBoard.next_id + 1
    
    def print_board(self):
        for i in range(len(self.numbers[0])):
            for j in range(len(self.numbers[0])):
                print(self.numbers[i][j].number, end=" ")
            print("\n", end="")

    def sum_of_unmarked_numbers(self):
        sum = 0
        for i in range(len(self.numbers[0])):
            for j in range(len(self.numbers[0])):
                if self.numbers[i][j].marked == False:
                    sum = sum + self.numbers[i][j].number
        return sum

    def check_row(self, i):
        for number in self.numbers[i]:
            if number.is_marked() == False:
                return False
        return True

    def check_column(self, j):
        for i in range(len(self.numbers[j])):
            if self.numbers[i][j].is_marked() == False:
                return False
        return True
            
    def check_board(self):
        for i in range(len(self.numbers[0])):
            if self.check_row(i) == True or self.check_column(i) == True:
                print("Board {} wins!".format(self.id))
                return True
        print("Board {} is not a winner...".format(self.id))
        return False

    def draw_number(self, drawn_number):
        for i in range(len(self.numbers[0])):
            for j in range(len(self.numbers[0])):
                if self.numbers[i][j].number == drawn_number:
                    self.numbers[i][j].mark()
        return self.check_board()

class Bingo:

    boards = []
    numbers = []

    def __init__(self, filename):
        lines = self.read_lines_from_file(filename)
        self.add_numbers_from_line(lines[0])
        self.create_boards_from_lines(lines)

    def add_board(self, board: BingoBoard):
        self.boards.append(board)

    def print_boards(self):
        for board in self.boards:
            board.print_board()
            print()

    def print_board_by_id(self, id: int):
        for i in range(len(self.boards)):
            if self.boards[i].id == id:
                self.boards[i].print_board()
                return


    def print_numbers(self):
        for number in self.numbers:
            print(number, end=", ")

    def read_numbers_from_string(self, numbers_as_string: str):
        bingo_row = []
        numbers = numbers_as_string.split(" ")
        for number in numbers:
            number = number.strip()
            if number.isdigit():
                bingo_row.append(BingoNumber(int(number)))
        return bingo_row

    def read_lines_from_file(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines
    
    def add_numbers_from_line(self, line):
        self.numbers = line.split(",")
    
    def create_boards_from_lines(self, lines):
        for i in range(len(lines)):
            if lines[i] == "\n":
                bingo_board = []
                for j in range(1, 6):
                    bingo_board.append(self.read_numbers_from_string(lines[i+j]))
                self.add_board(BingoBoard(bingo_board))

    def play(self):
        already_won = []
        for number in self.numbers:
            number = int(number)
            print("Number {} is drawn.".format(number))
            for board in self.boards:
                if board.id not in already_won:
                    if board.draw_number(number) == True:
                        already_won.append(board.id)
                        #self.print_board_by_id(87)
                        print(board.sum_of_unmarked_numbers() * number)
                        #return
        print(already_won)
            
    

bingo = Bingo("adventofcode2021_day4_input.txt")
bingo.play()
    



