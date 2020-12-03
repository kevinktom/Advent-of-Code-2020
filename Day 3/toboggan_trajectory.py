
"""
Part 1:
Given an input of characters representing a map/ biome, find how many trees you encounter if you traverse 1 down 3 right once you reach the bottom
The rows repeat themselves if past index
'.' = empty space
'#' = tree

Approach:
Parse file and store each row into an array
Define is_tree function to determine if location is a tree and make sure the y coordinate is modulod by the length of one row
If it is a tree, add to counter and keep going until you get to the bottom (map_height)
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

start = (0,0)
map_width = len(input_numbers[0])
map_height = len(input_numbers)
def is_tree(x,y):
    new_y = y % map_width
    return input_numbers[x][new_y] == '#'

tree_count = 0
while start[0] < map_height:
    if is_tree(start[0], start[1]):
        tree_count += 1
    start = (start[0] + 1, start[1] + 3)
print(tree_count)


"""
Part Two:
Find how many trees you encounter for each of the slopes: (1,1), (1,3), (1,5), (1,7), (2,1) with the first number representing going down and second number representing going right
Essentially do the same as part one, then multiply all the number of trees

Approach:
Create a find_trees function which takes in a slope and places the number in a dictionary with the key as the slope
Get all the values and multiply them
"""
import collections

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
trees_for_slopes = collections.defaultdict(int)
def find_trees(slope):
    start2 = (0,0)
    while start2[0] < map_height:
        if is_tree(start2[0], start2[1]):
            trees_for_slopes[slope] += 1
        start2 = (start2[0] + slope[0], start2[1] + slope[1])

find_trees(slopes[0])
find_trees(slopes[1])
find_trees(slopes[2])
find_trees(slopes[3])
find_trees(slopes[4])

def prod(arr):
    current = 1
    for num in arr:
        current *= num
    return current

print(prod(trees_for_slopes.values()))