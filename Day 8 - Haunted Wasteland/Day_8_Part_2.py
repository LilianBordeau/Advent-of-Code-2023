# Part Two // Not working // Too long

current_nodes = starting_nodes = [k for k in network_map.keys() if k[-1] == 'A'][1:]
dest_arrived  = False
i = 0 

while not dest_arrived:
    instruction = instructions[i % len(instructions)]
    
    next_nodes  = []
    
    for current_node in current_nodes:
        if instruction == 'L':
            next_node = network_map[current_node][0]
        elif instruction == 'R':
            next_node = network_map[current_node][1]
            
        next_nodes.append(next_node)
        
    
    if all([True if n[-1] == 'Z' else False for n in next_nodes]):
        print('Arrived in', i, 'network passes.')
        dest_arrived = True
        break
    
    i += 1
    current_nodes = next_nodes

# Part Two // Using LCM

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

        #if next_node == end_node:
        if next_node[-1] == end_node[-1]:
            #print('Arrived in', i, 'network passes.')
            dest_arrived = True
            return i + 1
            #break

        i += 1
        current_node = next_node
        
passes = [find_path(k, 'ZZZ', instructions, network_map) for k in network_map.keys() if k[-1] == 'A']
math.lcm(*passes)