def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 0
        group = []
        for line in lines:
            if line == "\n" and group:
                input_numbers.append(group)
                group = []
                continue
            item = line.strip()
            group.append(item.split())
            # group += item.split()
        input_numbers.append(group)
    return input_numbers

input_numbers = create_input_array()
# print(input_numbers[2])

import collections
# def reformat_input_array(input_numbers):
#     input_object = collections.defaultdict(list)
#     # Fields
#     for i in range(len(input_numbers[0])):
#         field = input_numbers[0][i]
#         first_interval = field[-3].split('-')
#         first_interval[0] = int(first_interval[0])
#         first_interval[1] = int(first_interval[1])
#         second_interval = field[-1].split('-')
#         second_interval[0] = int(second_interval[0])
#         second_interval[1] = int(second_interval[1])
#         input_object['fields'].append(first_interval)
#         input_object['fields'].append(second_interval)
#     input_object['fields'] = sorted(input_object['fields'], key = lambda x: (x[0], x[1]))
#     input_object['fields'] = merge_intervals(input_object['fields'])

#     # your_ticket
#     your_ticket_numbers = input_numbers[1][1][0].split(',')
#     your_ticket_numbers = list_elements_to_int(your_ticket_numbers)
#     input_object['your_ticket'] = your_ticket_numbers

#     # nearby_tickets
#     nearby_tickets = []
#     for i in range(1, len(input_numbers[2])):
#         arr = input_numbers[2][i][0].split(',')
#         arr = list_elements_to_int(arr)
#         nearby_tickets += arr
#     input_object['nearby_tickets'] = nearby_tickets

#     return input_object

# Part Two reformat
def reformat_input_array(input_numbers):
    input_object = collections.defaultdict(list)
    # Fields
    for i in range(len(input_numbers[0])):
        field = input_numbers[0][i]
        first_interval = field[-3].split('-')
        first_interval[0] = int(first_interval[0])
        first_interval[1] = int(first_interval[1])
        second_interval = field[-1].split('-')
        second_interval[0] = int(second_interval[0])
        second_interval[1] = int(second_interval[1])
        both_intervals = sorted([first_interval, second_interval], key = lambda x: (x[0], x[1]))
        both_intervals = merge_intervals(both_intervals)
        input_object['fields'].append(both_intervals)

    # your_ticket
    your_ticket_numbers = input_numbers[1][1][0].split(',')
    your_ticket_numbers = list_elements_to_int(your_ticket_numbers)
    input_object['your_ticket'] = your_ticket_numbers

    # nearby_tickets
    nearby_tickets = []
    for i in range(1, len(input_numbers[2])):
        arr = input_numbers[2][i][0].split(',')
        arr = list_elements_to_int(arr)
        nearby_tickets.append(arr)
    input_object['nearby_tickets'] = nearby_tickets
    # print(input_object['nearby_tickets'])

    return input_object

def list_elements_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr

def merge_intervals(intervals):
    merged = []
    for interval in intervals:
        if not merged:
            merged.append(interval)
        else:
            prev = merged[-1]
            if interval[0] > prev[1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], prev[1])
    return merged

# print(reformat_input_array(input_numbers))

# print(reformat_input_array(input_numbers)['fields'])
# test = (reformat_input_array(input_numbers))
# print(merge_intervals(test['fields']))

def within_interval(intervals, num):
    for interval in intervals:
        left = interval[0]
        right = interval[1]
        if left <= num <= right:
            return True
    return False


def find_ticket_scanning_error_rate(input_numbers):
    input_object = reformat_input_array(input_numbers)
    # input_object = {'fields': [[[0, 1], [4,19]], [[0,5], [8,19]], [[0,13], [16,19]]],
    #                 'nearby_tickets': [[3,9,18], [15,1,5], [5,14,9]]
    #                 }
    field_idx_to_ticket_idx = {}
    all_intervals = input_object['fields']
    all_tickets = input_object['nearby_tickets']
    # your_ticket = input_object['your_ticket']
    # print(your_ticket)
    for i in range(len(all_intervals)):
        intervals = all_intervals[i]
        for col in range(len(all_tickets[0])):
            not_in_this_col = False
            for row in range(len(all_tickets)):
                # print(row, col)
                # if all_tickets[row][col] == 9:
                #     print(all_tickets[row][col], all_intervals[i])
                if not within_interval(all_intervals[i], all_tickets[row][col]):
                    # print(all_intervals[i], all_tickets[row][col])
                    # print(within_interval(all_intervals[i], all_tickets[row][col]))
                    not_in_this_col = True
                    break
            if not_in_this_col:
                continue
            else:
                field_idx_to_ticket_idx[i] = col
                break
    
    return field_idx_to_ticket_idx



    # intervals = input_object['fields']
    # nearby_tickets = input_object['nearby_tickets']
    # ticket_scanning_error_rate = 0
    # for ticket_num in nearby_tickets:
    #     in_interval = within_interval(intervals, ticket_num)
    #     if not in_interval:
    #         ticket_scanning_error_rate += ticket_num
    # return ticket_scanning_error_rate

print(find_ticket_scanning_error_rate(input_numbers))
