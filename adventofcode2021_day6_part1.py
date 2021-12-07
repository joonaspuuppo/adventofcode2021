class SchoolOfFish:

    lanternfish_list = []

    def __init__(self, filename):
        self.create_fish_from_file(filename)
        self.day = 0
        
    def how_many_fish(self):
        return len(self.lanternfish_list)

    def print_all_lanternfish(self):
        for lanternfish in self.lanternfish_list:
            print(lanternfish.timer, end=" ")
        print()
    
    def create_fish_from_file(self, filename):
        timers = self.get_timers_from_file(filename)
        for timer in timers:
            self.lanternfish_list.append(LanternFish(timer))

    def get_timers_from_file(self, filename):
        file = open(filename, "r")
        line = file.readline()
        file.close()
        timers_as_string = line.split(",")
        timers = []
        for timer in timers_as_string:
            timers.append(int(timer))
        return timers

    def create_new_fish(self):
        self.lanternfish_list.append(LanternFish(8))

    def progress_day(self):
        self.day = self.day + 1
        new_fish_count = 0
        for lanternfish in self.lanternfish_list:
            if lanternfish.timer == 0:
                new_fish_count = new_fish_count + 1
            lanternfish.progress_timer()
        for i in range(new_fish_count):
            self.create_new_fish()

class LanternFish:

    def __init__(self, timer: int):
        self.timer = timer
    
    def progress_timer(self):
        self.timer = self.timer - 1
        if self.timer < 0:
            self.timer = 6

school = SchoolOfFish("adventofcode2021_day6_input.txt")    
# print("Fish count:", school.how_many_fish())
# print("Initial state: ", end="")
# school.print_all_lanternfish()
# school.progress_day()
# print("After day {}: ".format(school.day), end="")
# school.print_all_lanternfish()
# school.progress_day()
# print("After day {}: ".format(school.day), end="")
# school.print_all_lanternfish()
# school.progress_day()
# print("After day {}: ".format(school.day), end="")
# school.print_all_lanternfish()

while school.day < 80:
    school.progress_day()
    print(school.day)
print(school.how_many_fish())