"""
Day Six
Part One:
The whole plane is filling out customs forms and only answer yes on the questions applicable
The groups of people are separated by blank white spaces with each line being represented as a single person's answers
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Approach:
    -Parse the input and create an array of groups
    -For each group, go through each person's answers and put them in a set
    -Return the length of the set
    -Add up all groups length of sets
"""

def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        group = []
        for line in lines:
            if line == "\n" and group:
                input_numbers.append(group)
                group = []
                continue
            item = line.strip()
            group += item.split()
        input_numbers.append(group)
    return input_numbers

input_numbers = create_input_array()

def find_group_unique_answers(group):
    answer_questions = set()
    for person in group:
        answer_questions = answer_questions | set(person)
    return len(answer_questions)

def find_total_sum(all_groups):
    total = 0
    for group in all_groups:
        total += find_group_unique_answers(group)
    return total

# Part One Answer
print(find_total_sum(input_numbers))

"""
Part Two:
Same as above except now, only count the questions that every person in a group answered

Approach:
-Go through each group and create a counter via dictionary
-Create another dictionary for all the key value pairs that the value equal to the size of the group
-Go through all groups and add them up
"""
import collections
def find_group_all_answered(group):
    all_answers = collections.defaultdict(int)
    for person in group:
        for question in person:
            all_answers[question] += 1
    return len({k: v for k, v in all_answers.items() if v == len(group)})

def find_all_groups_answers(all_groups):
    total = 0
    for group in all_groups:
        total += find_group_all_answered(group)
    return total

# Part Two Answer
print(find_all_groups_answers(input_numbers))