import numpy as np
from numpy.typing import _128Bit


def read_file(filename) -> list:
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def get_coords(lines) -> list:
    coords = []
    for line in lines:
        if line == "\n":
            break
        coord = []
        values_as_string = line.split(",")
        for value in values_as_string:
            coord.append(int(value.strip()))
        coords.append(coord)
    return coords

def get_folds(lines) -> list:
    folds = []
    for line in lines:
        if line[0] == "f":
            fold = []
            fold.append(line[11])
            fold.append(int(line.split("=")[1].strip()))
            folds.append(fold)
    return folds

def find_max_x(coords) -> int:
    max = 0
    for coord in coords:
        if coord[0] > max:
            max = coord[0]
    return max

def find_max_y(coords) -> int:
    max = 0
    for coord in coords:
        if coord[1] > max:
            max = coord[1]
    return max

def create_matrix(max_x, max_y) -> list:
    return [[0] * (max_x + 1) for i in range((max_y + 1))]

def divide_matrix(fold, matrix) -> list:
    matrices = []
    matrix1 = []
    matrix2 = []
    #fold along x-axis
    if fold[0] == "y":
        for i in range(fold[1]):
            matrix1.append(matrix[i])
        matrices.append(matrix1)
        for i in range(fold[1] + 1, len(matrix)):
            matrix2.append(matrix[i])
        matrices.append(matrix2)
    #fold along y-axis
    else:
        for row in matrix:
            newrow = []
            for i in range(fold[1]):
                newrow.append(row[i])
            matrix1.append(newrow)
        matrices.append(matrix1)
        for row in matrix:
            newrow = []
            for i in range(fold[1] + 1, len(row)):
                newrow.append(row[i])
            matrix2.append(newrow)
        matrices.append(matrix2)
    return matrices

def fold_matrix(fold, matrices) -> list:
    matrix = matrices[0]
    if fold[0] == "x":
        matrices[1] = np.flip(matrices[1], axis=1)
    else:
        matrices[1] = np.flip(matrices[1], axis=0)
    matrix1 = matrices[1]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix1[i][j] == 1:
                matrix[i][j] = 1
    return matrix

def mark_coords(matrix, coords):
    for coord in coords:
        x = coord[0]
        y = coord[1]
        matrix[y][x] = 1

def count_ones(matrix):
    count = 0
    for row in matrix:
        for cell in row:
            if cell == 1:
                count += 1
    return count

def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()



lines = read_file("adventofcode2021_day13_input.txt")
coords = get_coords(lines)
matrix = create_matrix(find_max_x(coords), find_max_y(coords))
mark_coords(matrix, coords)
for fold in get_folds(lines):
    matrix = fold_matrix(fold, divide_matrix(fold, matrix))
#print(count_ones(matrix))
print_matrix(matrix)

