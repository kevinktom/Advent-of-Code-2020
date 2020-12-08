"""
Day 8:
Given an input file, each line represents some action
-acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
-jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
-nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
The program runs in an infinite loop
Return the accumulator right before the second loop starts again

Approach:
-Parse the lines and separate them into action and quantity
-Use a while loop and a seen set to keep track of seen indices
-If an indice is seen, break out of the loop and return the accumulator
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

def parse_action(action):
    act = action[0:3]
    net = action[4]
    quantity = int(action[5:])
    if net == '-':
        quantity = -(quantity)
    return (act, quantity)


def perform_action(action, current_idx, accumulator):
    act, quantity = parse_action(action)
    if act == 'acc':
        accumulator += quantity
        current_idx += 1
    elif act == 'nop':
        current_idx += 1
    else:
        current_idx += quantity
    return(current_idx, accumulator)

def perform_all_actions():
    seen = set()
    current_idx = 0
    accumulator = 0
    while True:
        if current_idx in seen:
            break
        action = input_numbers[current_idx]
        seen.add(current_idx)
        (new_idx, new_accumulator) = perform_action(action, current_idx, accumulator)
        current_idx = new_idx
        accumulator = new_accumulator
        
    return accumulator
# Part One Answer
print(perform_all_actions())


"""
Part Two:
-One of the actions that contains 'nop' or 'jmp' can be changed to 'jmp' or 'nop' respectively.
-When this is done, the infinite loop will break as the index goes past the actions list
-Return the accumulator when the last action is performed

Approach:
-Create deep copies of the input array and for loop to change one action that is either 'jmp' or 'nop'
-Go through the actions and if it isn't an infinite loop (seen set), return the accumulator
-Not the most efficient (brute force), but gets the job done
"""
def perform_all_actions(input_array):
    seen = set()
    current_idx = 0
    accumulator = 0
    while current_idx < len(input_array):
        if current_idx in seen:
            return False
        action = input_array[current_idx]
        seen.add(current_idx)
        (new_idx, new_accumulator) = perform_action(action, current_idx, accumulator)
        current_idx = new_idx
        accumulator = new_accumulator
    return accumulator

import copy
def change_one_action(input_array):
    temp_input = copy.deepcopy(input_array)
    for i in range(len(temp_input)):
        action = temp_input[i]
        if action[0:3] == 'nop':
            temp_input[i] = 'jmp' + temp_input[i][3:]
        elif action[0:3] == 'jmp':
            temp_input[i] = 'nop' + temp_input[i][3:]
        answer = perform_all_actions(temp_input)
        if answer != False:
            return answer
        temp_input = copy.deepcopy(input_array)
    return False

# Part Two Answer 
print(change_one_action(input_numbers))



    