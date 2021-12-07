import statistics
import math

def find_optimal_position_median(positions):
   return statistics.median(positions)

def find_optimal_position_mean(positions):
   return statistics.mean(positions)
  
def get_positions_from_file(filename):
        file = open(filename, "r")
        line = file.readline()
        file.close()
        positions_as_string = line.split(",")
        positions= []
        for position in positions_as_string:
            positions.append(int(position))
        return positions    

positions = get_positions_from_file("adventofcode2021_day7_input.txt")
optimal_position = find_optimal_position_median(positions)
optimal_position_mean = find_optimal_position_mean(positions)

total_fuel = 0
for submarine_position in positions:
    fuel_cost = 0
    delta = abs(submarine_position - math.floor(optimal_position_mean))
    i = 1
    while delta > 0:
        fuel_cost = fuel_cost + i
        delta = delta - 1
        i = i + 1
    total_fuel = total_fuel + fuel_cost


print(total_fuel)