"""
Day 10: Given an input array of chargers with jolts, you want to be able to connect every charger that you have.
Chargers can only be connected to one another if they have a jolt difference of 3 or less
If you were to connect all chargers, find the product of the number of chargers that have a 1 jolt difference and the number of chargers that have a 3 jolt difference

Approach:
-Sort the input because the connections between chargers will always be in sorted order
-Use a hash to keep track of all the differences between each number with the key as the jolt difference
-Iterate through sorted hash and compare current joltage to the next one
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
input_numbers.sort()

 

import collections

def find_voltages(arr):
    voltage_uses = collections.defaultdict(int)
    arr.sort()
    voltage_uses[arr[0]] += 1
    for i in range(len(arr)-1):
        voltage = arr[i+1] - arr[i]
        voltage_uses[voltage] += 1
    voltage_uses[3] += 1
    return voltage_uses[1] * voltage_uses[3]

# Part One Answer 
print(find_voltages(input_numbers))


"""
Part Two
Find the number of combinations to connect all the chargers

Approach:
-Use Tribonnacci
-A tabulated array will allow you to calculate how many ways to get to your current spot by checking the last three spots and seeing if the difference in jolts is 3 or less
-Return the last element in the tabulated array to see how many ways you can get to the end
-Add [0] and [3+max] to the array as they're included
"""

tab = [1] + [1] + [0] * (len(input_numbers) - 2)
def trib():
    if input_numbers[2] - input_numbers[1] <= 3:
        tab[2] += tab[1]
    if input_numbers[2] - input_numbers[0] <= 3:
        tab[2] += tab[0]
    for i in range(3, len(input_numbers)):
        if input_numbers[i] - input_numbers[i-1] <= 3:
            tab[i] += tab[i-1]
        if input_numbers[i] - input_numbers[i-2] <= 3:
            tab[i] += tab[i-2]
        if input_numbers[i] - input_numbers[i-3] <= 3:
            tab[i] += tab[i-3]
    return tab[-1]

# Part Two Answer   
print(trib())

            
