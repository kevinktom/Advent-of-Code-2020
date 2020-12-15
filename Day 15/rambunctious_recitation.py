"""
Day 15: Input is as given: [9,3,1,0,8,4]
The input are the numbers that are spoken first
With each number spoken starting with the last element, the next spoken word will be determined by the following:
-If that was the first time the number has been spoken, the current player says 0.
-Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
Determine the 2020th spoken number

Part Two:
Determine the 30000000th spoken number

Approach:
-Use a dictionary to keep track of seen numbers and the idx at which they were last spoken
-First put in all the elements except for the last, and then starting with the last we can determine the next spoken number
-Return the last next spoken number
"""

input = [9,3,1,0,8,4]
import collections

def find_nth_number(input, nth_spoken_num):
    spoken_nums = collections.defaultdict(int)
    for i in range(len(input) - 1):
        spoken_nums[input[i]] = i
    
    next_num_spoken = input[-1]
    for i in range(len(input)-1, nth_spoken_num-1):
        if next_num_spoken in spoken_nums:
            new_next_num = i - spoken_nums[next_num_spoken]
        else:
            new_next_num = 0
        spoken_nums[next_num_spoken] = i
        next_num_spoken = new_next_num
    return next_num_spoken

# Part One Answer
print(find_nth_number(input, 2020))

# Part Two Answer
print(find_nth_number(input, 29999999))