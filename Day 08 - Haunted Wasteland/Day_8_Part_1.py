# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_8.txt"

hands = {}

network_map = {}

with open(input_file, "r") as f:
    for line in f:
        #print(line)
        
        if len(line) > 100:
            instructions = line[:-1]
        
        elif len(line) == 17:
            node = line[:3]
            left = line[7:10]
            rght = line[12:15]
            network_map[node] = (left, rght)
            
# Part One

def find_path(start_node, end_node, instructions, network_map):

    current_node = start_node
    dest_arrived = False
    i = 0 

    while not dest_arrived:
        instruction = instructions[i % len(instructions)]

        if instruction == 'L':
            next_node = network_map[current_node][0]
        elif instruction == 'R':
            next_node = network_map[current_node][1]

        if next_node == end_node:
            print('Arrived in', i, 'network passes.')
            dest_arrived = True
            break

        i += 1
        current_node = next_node