def create_input_array():
    filepath = 'input.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        for i in range(2):
            if i == 0:
                time_stamp = lines[i].strip()
            if i == 1:
                buses = lines[i].strip().split(',')
    return (int(time_stamp), buses)

time_stamp, buses = create_input_array()

def find_bus_arrival(bus_id, current_time):
    pre_arrival = 0
    arrival = pre_arrival + bus_id
    while not (pre_arrival < current_time <= arrival):
        pre_arrival += bus_id
        arrival += bus_id
    return arrival

def find_earliest_bus(all_buses, arrival_time):
    earliest_bus_id = None
    earliest_arrival = float('inf')
    for bus_id in all_buses:
        if bus_id == 'x':
            continue
        else:
            bus_arrival = find_bus_arrival(int(bus_id), arrival_time)
            if bus_arrival < earliest_arrival:
                earliest_bus_id = bus_id
                earliest_arrival = bus_arrival
    return int(earliest_bus_id) * (earliest_arrival - arrival_time)

# Part One Answer
print(find_earliest_bus(buses, time_stamp))


"""
Part Two
"""
# buses = ['7', '13', 'x', 'x', '59', 'x', '31', '19']
def populate_all_stops(all_buses):
    current_timestamp = 0
    lcm = int(all_buses[0])
    for i in range(1,len(all_buses)):
        bus_id = all_buses[i]
        if bus_id == 'x':
            continue
        else:
            bus_id = int(bus_id)
            while (current_timestamp+i) % bus_id != 0:
                current_timestamp += lcm
            lcm *= bus_id
    return current_timestamp

# Part Two Answer
print(populate_all_stops(buses))

