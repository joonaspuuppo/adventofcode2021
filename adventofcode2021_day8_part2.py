class SevenSegmentDisplay:

    def __init__(self, filename, i):
        self.segments = {"top": "x",
                         "upper_left": "x",
                         "upper_right": "x",
                         "middle": "x",
                         "lower_left": "x",
                         "lower_right": "x",
                         "bottom": "x"}
        self.digits = {}
        lines = self.read_lines_from_file(filename)
        self.outputs = self.get_outputs(lines)[i].strip().split(" ")
        self.signals = self.get_signals(lines)[i].strip().split(" ")

    #correct order important!
    def deduction(self):
        self.get_easy_digits()
        self.get_three()
        self.get_top()
        self.get_upper_left()
        self.get_bottom()
        self.get_lower_left()
        self.get_nine()
        self.get_two()
        self.get_five()
        self.get_six()
        self.get_zero()


    
    def get_easy_digits(self):
        for signal in self.signals:
            if len(signal) == 2:
                self.digits[1] = signal
            elif len(signal) == 3:
                self.digits[7] = signal
            elif len(signal) == 4:
                self.digits[4] = signal
            elif len(signal) == 7:
                self.digits[8] = signal
            
    def get_three(self):
        for signal in self.signals:
            if len(signal) == 5 and len(set(signal).intersection(set(self.digits[7]))) == 3:
                self.digits[3] = signal  

    def get_top(self):
        one = set(self.digits.get(1))
        seven = set(self.digits.get(7))
        top = "".join(seven.difference(one))
        self.segments.update({"top": top})

    def get_upper_left(self):
        three_as_set = set(self.digits[3])
        four_as_set = set(self.digits[4])
        upper_left = "".join(four_as_set.difference(three_as_set))
        self.segments.update({"upper_left": upper_left})

    def get_bottom(self):
        three_as_set = set(self.digits[3])
        four_as_set = set(self.digits[4])
        top_and_bottom = three_as_set.difference(four_as_set)
        bottom = top_and_bottom.difference(set(self.segments["top"]))
        self.segments.update({"bottom": "".join(bottom)})

    def get_lower_left(self):
        three_as_set = set(self.digits[3])
        eight_as_set = set(self.digits[8])
        upper_lower_left = eight_as_set.difference(three_as_set)
        lower_left = "".join(upper_lower_left.difference(set(self.segments["upper_left"])))
        self.segments.update({"lower_left": lower_left})

    def get_nine(self):
        eight_as_set = set(self.digits[8])
        for signal in self.signals:
            if len(signal) == 6 and eight_as_set.difference(set(signal)) == set(self.segments["lower_left"]):
                self.digits[9] = signal
    
    def get_two(self):
        for signal in self.signals:
            if len(signal) == 5 and set(self.segments["lower_left"]).issubset(set(signal)):
                self.digits[2] = signal
    
    def get_five(self):
        for signal in self.signals:
            if len(signal) == 5 and set(signal) != set(self.digits[2]) and set(signal) != set(self.digits[3]):
                self.digits[5] = signal

    def get_six(self):
        for signal in self.signals:
            if len(signal) == 6 and set(signal) == set.union(set(self.digits[5]), set(self.segments["lower_left"])):
                self.digits[6] = signal

    def get_zero(self):
        nine_as_set = set(self.digits[9])
        for signal in self.signals:
            if len(signal) == 6 and set(signal).difference(nine_as_set) == set(self.segments["lower_left"]) and len(set(signal).intersection(set(self.digits[7]))) == 3:
                self.digits[0] = signal

    def read_lines_from_file(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines

    def get_outputs(self, lines):
        list = []
        for line in lines:
            list.append(line.split(" | ")[1])
        return list

    def get_signals(self, lines):
        list = []
        for line in lines:
            list.append(line.split(" | ")[0])
        return list
    
    def outputs_to_int(self):
        digits_as_string = ""
        for output in self.outputs:
            for key in self.digits:
                if set(output) == set(self.digits.get(key)):
                    digits_as_string = "".join([digits_as_string, str(key)])
        return int(digits_as_string)

sum = 0
for i in range(200):
    display = SevenSegmentDisplay("adventofcode2021_day8_input.txt", i)
    display.deduction()
    sum += display.outputs_to_int()
print(sum)

