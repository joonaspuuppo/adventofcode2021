class SchoolOfFish:

    lanternfish_agecount = [0,0,0,0,0,0,0,0,0]

    def __init__(self, filename):
        self.create_fish_from_file(filename)
        self.day = 0
        
    def how_many_fish(self):
        sum = 0
        for age in self.lanternfish_agecount:
            sum = sum + age
        return sum
            

    def print_all_lanternfish(self):
        for lanternfish in self.lanternfish_agecount:
            print(lanternfish, end=" ")
        print()
    
    def create_fish_from_file(self, filename):
        timers = self.get_timers_from_file(filename)
        for timer in timers:
            self.lanternfish_agecount[timer] = self.lanternfish_agecount[timer] + 1

    def get_timers_from_file(self, filename):
        file = open(filename, "r")
        line = file.readline()
        file.close()
        timers_as_string = line.split(",")
        timers = []
        for timer in timers_as_string:
            timers.append(int(timer))
        return timers

    def progress_day(self):
        self.day = self.day + 1
        lanternfish = self.lanternfish_agecount
        x = lanternfish[0]
        for i in range(1, 9):
            lanternfish[i - 1] = lanternfish[i]
        lanternfish[6] = lanternfish[6] + x
        lanternfish[8] = x


school = SchoolOfFish("adventofcode2021_day6_input.txt")    

while school.day < 256:
    school.progress_day()
    #print(school.day)
print(school.how_many_fish())