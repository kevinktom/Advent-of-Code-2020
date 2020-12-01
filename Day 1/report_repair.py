"""
Given an input.txt file with a ton of numbers, return the value of two numbers multiplied which add up to 2020. ex. 1721 * 299

Approach:
    -Download the input text
    -Parse the text and place all the numbers into an array
    -Create a set and add the number subtracted from 2020 to store all complements
    -If the complement is found, return the number and it's complement multiplied
"""

filepath = 'input.txt'
input_numbers = []
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       input_numbers.append(int(line.strip()))
       line = fp.readline()
       cnt += 1

seen = set()

for num in input_numbers:
    complement = 2020 - num
    if complement in seen:
        print(num * complement)
        # return
    else:
        seen.add(num)

"""
Part Two:
    return the value of three numbers multiplied which add up to 2020. ex. 979 * 366 * 675

Approach:
    Nested for loop through each number and the numbers after it
    Keep track of the complement of the two numbers added
    if the complement was seen and the indices for all three numbers are different then print the numbers multiplied
    Can keep track of all numbers seen in the nested for loop

Refactor: creating a separate initial for loop to store the number in the seen dictionary to avoid constantly executing redundant lines within the nested loop (lines 56 & 57)
"""
import collections

seen = collections.defaultdict()

for i, num in enumerate(input_numbers):
    seen[num] = i

for i, num in enumerate(input_numbers):
    for j in range(i+1, len(input_numbers)):
        complement = 2020 - (num + input_numbers[j])
        if complement in seen and seen[complement] != i and seen[complement] != j:
            print(complement * num * input_numbers[j])
            break
    #     seen[input_numbers[j]] = j
    # seen[num] = i
        


