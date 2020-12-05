"""
Part One:
Given an input with the first 7 characters as either F or B and the last 3 characters as L or R, return the highest seat id
To get the seat id you must first determine the row and column of the seat
There are 128 rows and 8 columns
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
-F means to take the lower half, keeping rows 0 through 63.
-B means to take the upper half, keeping rows 32 through 63.
-F means to take the lower half, keeping rows 32 through 47.
-B means to take the upper half, keeping rows 40 through 47.
-B keeps rows 44 through 47.
-F keeps rows 44 through 45.
-The final F keeps the lower of the two, row 44.

-The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7).
-The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
-
-For example, consider just the last 3 characters of FBFBBFFRLR:
-
Start by considering the whole range, columns 0 through 7.
-R means to take the upper half, keeping columns 4 through 7.
-L means to take the lower half, keeping columns 4 through 5.
-The final R keeps the upper of the two, column 5.
-So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
-
-Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Approach:
-Parse the array and create the input array
-Create a find_seat function which returns a tuple in the format of (row, column)
-Create a calculate_seat_id function that takes in the tuple
-Loop through the input array and determine the highest seat_id
"""
def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        for line in lines:
            item = line.strip()
            input_numbers.append(item)
    return input_numbers

input_numbers = create_input_array()
# print(input_numbers)

def find_seat(code):
    back, front = 0, 127
    left, right = 0, 7
    
    front_back = code[0:7]
    left_right = code[7:]

    for dire in front_back:
        half = (front - back + 1) // 2
        if dire == 'F':
            front -= half
        else:
            back += half
    
    for dire in left_right:
        half = (right - left + 1) // 2
        if dire == 'R':
            left += half
        else:
            right -= half
    return (back, right)

def calculate_seat_id(row, col):
    return (row * 8) + col

current_highest_seat_id = 0
for dires in input_numbers:
    row, col = find_seat(dires)
    seat_id = calculate_seat_id(row, col)
    current_highest_seat_id = max(current_highest_seat_id, seat_id)
# Part One Answer
print(current_highest_seat_id)

"""
Part Two:
The plane is full except for the very front or back which are empty seats
Seat IDs that are your seat - 1 and your seat + 1 exist
Find your seat id

Approach:
-Create a seat_ids array
-Sort the list
-Iterate through the list and find where there are two seats next to each other that have a difference of 2
-Return the seat id by adding 1 to the smaller one or subtracting 1 from the bigger one
"""
# Store tuples (row, col)
seat_ids = []
for dires in input_numbers:
    row, col = find_seat(dires)
    seat_id = calculate_seat_id(row, col)
    seat_ids.append(seat_id)

seat_ids.sort()
for i in range(0,len(seat_ids)-1):
    seat_id = seat_ids[i]
    if seat_ids[i] + 2 == seat_ids[i+1]:
        # Part Two Answer
        print(seat_ids[i] + 1)
        return



