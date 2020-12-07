"""
Part One:
Given the input, the first bag contains the rest of the bags
Determine how many unique bags contain a shiny gold bag

Approach:
-Parse the bag rule and create an adjacency list with they key as the bag and the value as all the bags that that bag contains
-DFS on the graph and if a shiny gold bag is found, return true
-Loop through all bag rules and if the dfs of the bag rule is true, increment counter
-Return counter
-Use a memo to store seen bag rules and to avoid loops
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

import collections
bag_graph = collections.defaultdict(list)

def separate_bag_rule(bag_rule):
    # Removes period at end
    words = bag_rule[0:-1].split()
    key_bag = words[0] + words[1] + 'bag'
    current_bag = ''
    for i in range(5, len(words)):
        word = words[i]
        if word.isdigit():
            continue
        if word == 'other':
            bag_graph[key_bag] = []
            return
        if word == 'bag' or word == 'bags' or word == 'bag,' or word == 'bags,':
            bag_graph[key_bag] += [current_bag + 'bag']
            current_bag = ''
            continue
        current_bag += word

def create_bag_graph():
    for bag_rule in input_numbers:
        separate_bag_rule(bag_rule)
create_bag_graph()

def graph_dfs(key_bag, memo = None):
    if memo == None:
        memo = {}
    if key_bag == 'shinygoldbag':
        return True
    if key_bag in memo:
        return memo[key_bag]
    for child_bag in bag_graph[key_bag]:
        gold_seen = graph_dfs(child_bag, memo)
        if gold_seen:
            memo[key_bag] = True
            return True
    memo[key_bag] = False
    return False
def check_every_bag():
    count = 0
    for k,v in list(bag_graph.items()):
        if graph_dfs(k) and k != 'shinygoldbag':
            count += 1
    return count
# Part One Answer
print(check_every_bag())

"""
Part Two:
Now calculate the total number of bags that the shiny gold bag contains
Approach:
-Parse through the input the same way as above except now also pass in the number of bags
-Create the adjacency list and use dfs
-Initialize the total to 1 to include the bag itself, then loop through the nested bags
-Increment the total by the dfs of the nested bags multiplied by the number of bags
-Subtract one from the total to exclude the shiny gold bag
-Memoize
"""
bag_graph = collections.defaultdict(list)
def separate_bag_rule(bag_rule):
    words = bag_rule[0:-1].split()
    key_bag = words[0] + words[1] + 'bag'
    current_bag = ''
    for i in range(4, len(words)):
        word = words[i]
        if word.isdigit():
            current_bag += word
            continue
        if word == 'other':
            bag_graph[key_bag] = []
            return
        if word == 'bag' or word == 'bags' or word == 'bag,' or word == 'bags,':
            bag_graph[key_bag] += [current_bag + 'bag']
            current_bag = ''
            continue
        current_bag += word

def create_bag_graph():
    for bag_rule in input_numbers:
        separate_bag_rule(bag_rule)
create_bag_graph()

def graph_dfs(key_bag, memo = None):
    if memo is None:
        memo = {}
    if key_bag in memo:
        return memo[key_bag]
    total = 1
    for child_bag in bag_graph[key_bag]:
        amount = int(child_bag[0])
        total += (amount * graph_dfs(child_bag[1:], memo))
    memo[key_bag] = total
    return total
# Part Two Answer
print(graph_dfs("shinygoldbag"))