"""
Part One: Input file of numbers. First 25 numbers are a preamble, with the 26th number and onwards being the sum of any of the two previous 25 numbers before it
The 27th element can only be the sum of two numbers between the 1st and the 26th element. Cannot use the same element twice
Find the number in the array that does not follow the above rule

Approach:
-Find all sums and if none of the previous 25 numbers add up to the current, return the number
"""
def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        for line in lines:
            item = line.strip()
            input_numbers.append(int(item))
    return input_numbers

input_numbers = create_input_array()

def sum_two(start_idx, end_idx):
    for i in range(start_idx, end_idx):
        for j in range(start_idx+1, end_idx):
            if input_numbers[i] + input_numbers[j] == input_numbers[end_idx]:
                return False
    return input_numbers[end_idx]

def check_all_nums():
    for i in range(25, len(input_numbers)):
        result = sum_two(i-25, i)
        if result:
            return result
    return False

# Part One Answer
print(check_all_nums())

"""
Part Two: Contiguous subarray within input array will add to the odd number from part one. Add the min and max of the contiguous subarray
Approach: Sliding window O(n)
"""
# Finds index of Part One answer
def sum_two_idx(start_idx, end_idx):
    for i in range(start_idx, end_idx):
        for j in range(start_idx+1, end_idx):
            if input_numbers[i] + input_numbers[j] == input_numbers[end_idx]:
                return False
    return end_idx

def check_all_nums_idx():
    for i in range(25, len(input_numbers)):
        result = sum_two_idx(i-25, i)
        if result:
            return result
    return False

idx = check_all_nums_idx()

def sliding_window():
    left = 0
    current = 0
    for i in range(idx):
        if current == input_numbers[idx]:
            return (left, i)
        current += input_numbers[i]
        while current > input_numbers[idx]:
            current -= input_numbers[left]
            left += 1
(start, end) = sliding_window()
sub_array = input_numbers[start:end]
# Part Two Answer
print(min(sub_array) + max(sub_array))
