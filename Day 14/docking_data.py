import collections

def create_input_array():
    filepath = 'input.txt'
    masks_to_mems = collections.defaultdict(list)
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        current_mask = None
        for line in lines:
            item = line.strip()
            if item[0:4] == 'mask':
                current_mask = item[7:]
            else:
                idx = None
                val = None
                for i in range(len(item)):
                    char = item[i]
                    if char == '=':
                        idx = int(item[4:i-2])
                        val = int(item[i+2:])
                masks_to_mems[current_mask].append((idx, val))
    return masks_to_mems



input_numbers = create_input_array()
# print(input_numbers)


def convert_int_list_to_binary(int_list):
    return "".join([str(c) for c in int_list])

def convert_binary_to_int(binary_number):
    return int((binary_number), 2)

def convert_int_to_binary_list(number):
    return [int(d) for d in str(bin(number))[2:]]

def convert_binary_list_to_int(binary_list):
    binary_number = convert_int_list_to_binary(binary_list)
    return convert_binary_to_int(binary_number)

# def mask_binary_values(binary_list, mask):
#     for i in range(len(binary_list)):
#         if mask[i].isdigit():
#             binary_list[i] = int(mask[i])
#     return binary_list

def mask_binary_values(binary_list, mask):
    for i in range(len(binary_list)):
        if mask[i] != 0:
            binary_list[i] = 1
    return binary_list

# input_numbers = {'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X': [(8, 11), (7,101), (8, 0)]}
def written_values(masks_and_values):
    written = {}
    for mask, values in masks_and_values.items():
        for idx_number in values:
            idx = idx_number[0]
            number = idx_number[1]
            number_binary_list = convert_int_to_binary_list(number)
            additional_spaces = len(mask) - len(number_binary_list)
            num_list = [0] * additional_spaces + convert_int_to_binary_list(number)
            masked_number_list = mask_binary_values(num_list, mask)
            masked_number = convert_binary_list_to_int(masked_number_list)
            written[idx] = masked_number
    return sum(written.values())

# Part One Answer
print(written_values(input_numbers))
# print(convert_binary_list_to_int([0,0,0,1,0,1,1]))

"""
Part Two
"""

def list_to_str(arr):
    string_version = ''
    for char in arr:
        string_version += str(char)
    return string_version

def mask_binary_values2(binary_list, mask):
    for i in range(len(binary_list)):
        if mask[i] == '1':
            binary_list[i] = 1
        elif mask[i] == 'X':
            binary_list[i] = 'X'
    return binary_list

def create_memory_addresses(idx_binary):
    addresses = set()
    def permutations(idx_binary, seen = None):
        if seen is None:
            seen = set()
        if 'X' not in idx_binary:
            addresses.add(convert_binary_list_to_int(idx_binary))
        string_idx_binary = list_to_str(idx_binary)
        if string_idx_binary in seen:
            return 
        for i in range(len(idx_binary)):
            char = idx_binary[i]
            if char == 'X':
                for j in range(2):
                    permutations(idx_binary[0:i] + [j] + idx_binary[i+1:], seen)
        seen.add(string_idx_binary)
        
    permutations(idx_binary)
    return addresses

# print(create_memory_addresses([0,0,0,0,1,'X',0,'X','X']))
def written_values2(masks_and_values):
    written = {}
    counter = 0
    for mask, values in masks_and_values.items():
        print(mask, counter)
        for idx_number in values:
            idx = idx_number[0]
            number = idx_number[1]
            memory_binary_list = convert_int_to_binary_list(idx)
            additional_spaces = len(mask) - len(memory_binary_list)
            memory_list = [0] * additional_spaces + memory_binary_list

            masked_memory = mask_binary_values2(memory_list, mask)
            addresses = create_memory_addresses(masked_memory)
            for address in addresses:
                written[address] = number
        counter += 1
    return sum(written.values())

# Part Two Answer
print(written_values2(input_numbers))
