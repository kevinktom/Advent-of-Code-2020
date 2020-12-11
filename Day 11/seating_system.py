"""
Part One:
Given a matrix representing seats on a ferry, the following rules are applied with each wave of people:
-If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
-If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
-Otherwise, the seat's state does not change.

Part Two:
-From a seat, a person will only be able to see the direct seats in all directions
-Rules won't apply to adjacent seats anymore, but rather the first seat the person sees in all 8 directions
-Now it takes 5 or more visible occupied seats for an occupied seat to become empty

Ex. The empty seat below would see no occupied seats:
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Approach:
Part One
-Create function to check adjacent occupied neighboring seats
-Create an apply rule function that will change the status of the seat to a temporary variable
-After looping through the whole matrix and applying temporary variables indicating if seats will be occupied or open in the next wave,
    loop through the matrix again to apply the state. This is needed as we want to change the state of all seats at once without them being affected by neighboring seats being changed
-Compare the old state and new state by using deepcopy to know when the While True loop can be stopped

Part Two
-Same functions as part one except the function to check adjacent seats will be changed.
-In this case, for each direction continuously check in that direction (while loop)
-Also change 4 to 5
"""

def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        for line in lines:
            item = line.strip()
            input_numbers.append(list(item))
    return input_numbers

input_numbers = create_input_array()

# Test input
# input_numbers = [
#                 ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
#                 ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
#                 ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
#                 ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#'],
#                 ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
#                 ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
#                 ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
#                 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
#                 ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
#                 ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#']
#                 ]

adjacents = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
width = len(input_numbers[0])
height = len(input_numbers)

# Function to find adjacent occupied seats for PART ONE

# def adjacent_occupied_seats(y, x, matrix):
#     occupied_count = 0
#     for adj in adjacents:
#         new_y, new_x = y+adj[0], x+adj[1]
#         if 0 <= new_y < height and 0 <= new_x < width:
#             neighbor = matrix[new_y][new_x]
#             if neighbor == '#' or neighbor == 'E':
#                 occupied_count += 1
#     return occupied_count

# Function to find adjacent occupied seats for PART TWO
def adjacent_occupied_seats(y, x, matrix):
    occupied_count = 0
    for adj in adjacents:
        new_y, new_x = y+adj[0], x+adj[1]
        while 0 <= new_y < height and 0 <= new_x < width:
            neighbor = matrix[new_y][new_x]
            if neighbor == '#' or neighbor == 'E':
                occupied_count += 1
                break
            elif neighbor == 'L' or neighbor == 'O':
                break
            new_y += (adj[0])
            new_x += (adj[1])
    return occupied_count

def all_rules(y, x, matrix):
    current = matrix[y][x]
    adjacent_seat_count = adjacent_occupied_seats(y, x, matrix)
    if current == 'L' and adjacent_seat_count == 0:
        matrix[y][x] = 'O'
    elif current == '#' and adjacent_seat_count >= 5:
        
        matrix[y][x] = 'E'

def apply_state(y,x, matrix):
    if matrix[y][x] == 'O':
        matrix[y][x] = '#'
    elif matrix[y][x] == 'E':
        matrix[y][x] = 'L'


def one_arrival(matrix):
    width = len(matrix[0])
    height = len(matrix)
    for y in range(height):
        for x in range(width):
            all_rules(y, x, matrix)
    for y in range(height):
        for x in range(width):
            apply_state(y, x, matrix)
    return matrix

def count_all_occupied(matrix):
    count = 0
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == '#':
                count += 1
    return count

import copy

def all_arrivals(matrix):
    old_state = matrix
    while True:
        old_state2 = copy.deepcopy(old_state)
        current_state = one_arrival(matrix)
        if current_state == old_state2:
            return count_all_occupied(current_state)
        old_state = current_state


# Answer for both parts. Comment in the correct 'adjacent_occupied_seats' to get the corresponding answer
print(all_arrivals(input_numbers))


