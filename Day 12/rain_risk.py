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

def direction_move(x, y, dire, amount):
    if dire == 0:
        return(x, y+amount)
    elif dire == 90:
        return(x+amount, y)
    elif dire == 180:
        return(x, y-amount)
    else:
        return(x-amount, y)

def move_once(move, x, y, dire):
    action = move[0]
    amount = int(move[1:])
    new_x, new_y, new_dire = x, y, dire
    if action == 'F':
        new_x, new_y = direction_move(x, y, dire, amount)
    elif action == 'N':
        new_x, new_y = direction_move(x, y, 0, amount)
    elif action == 'E':
        new_x, new_y = direction_move(x, y, 90, amount)
    elif action == 'S':
        new_x, new_y = direction_move(x, y, 180, amount)
    elif action == 'W':
        new_x, new_y = direction_move(x, y, 270, amount)
    elif action == 'R':
        new_dire = (dire + amount + 360) % 360
    elif action == 'L':
        new_dire = (dire - amount + 360) % 360
    return (new_x, new_y, new_dire)

def find_manhattan_distance():
    x = 0
    y = 0
    dire = 90
    for move in input_numbers:
        (x, y, dire) = move_once(move, x, y, dire)
    return abs(x) + abs(y)

# Part One Answer
# print(find_manhattan_distance())

"""
Part Two
"""

def direction_move2(x, y, dire, amount):
    if dire == 0:
        return(x, y+amount)
    elif dire == 90:
        return(x+amount, y)
    elif dire == 180:
        return(x, y-amount)
    else:
        return(x-amount, y)

def rotate_waypoint(waypoint_x, waypoint_y, amount, action):
    while amount > 0:
        if action == 'R':
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            amount -= 90
        elif action == 'L':
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            amount -= 90
    return (waypoint_x, waypoint_y)

def move_once2(move, x, y, waypoint_x, waypoint_y, dire):
    action = move[0]
    amount = int(move[1:])
    new_x, new_y, new_dire, new_waypoint_x, new_waypoint_y = x, y, dire, waypoint_x, waypoint_y
    if action == 'F':
        new_x, new_y = (x + (waypoint_x * amount)), (y + (waypoint_y * amount))
    elif action == 'N':
        new_waypoint_x, new_waypoint_y = direction_move2(new_waypoint_x, new_waypoint_y, 0, amount)
    elif action == 'E':
        new_waypoint_x, new_waypoint_y = direction_move2(new_waypoint_x, new_waypoint_y, 90, amount)
    elif action == 'S':
        new_waypoint_x, new_waypoint_y = direction_move2(new_waypoint_x, new_waypoint_y, 180, amount)
    elif action == 'W':
        new_waypoint_x, new_waypoint_y = direction_move2(new_waypoint_x, new_waypoint_y, 270, amount)
    elif action == 'R':
        new_waypoint_x, new_waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, amount, 'R')
    elif action == 'L':
        new_waypoint_x, new_waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, amount, 'L')
    return (new_x, new_y, new_waypoint_x, new_waypoint_y, new_dire)

def find_manhattan_distance2():
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1
    dire = 90
    for move in input_numbers:
        (x, y, waypoint_x, waypoint_y, dire) = move_once2(move, x, y, waypoint_x, waypoint_y, dire)
    return abs(x) + abs(y)

# Part Two Answer
print(find_manhattan_distance2())
        
