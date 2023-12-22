# Get data

input_file = "input_day_18.txt"

instructions = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        d = line.split(' ')[0]
        m = line.split(' ')[1]
        c = line.split(' ')[2][1:-1]
        instructions.append((d,m,c))
        
# Create coordinates from instructions

cur_x, cur_y, cur_c = 0, 0, '┏'
coordinates  = [(cur_y, cur_x, cur_c)]

for i, instruction in enumerate(instructions):
    #print(instruction)
    
    if instruction[0] == 'R':
        cur_c = '>'
        for _ in range(1, int(instruction[1])):
            cur_x += 1
            coordinates.append((cur_y, cur_x, cur_c))
            
        if i < len(instructions) - 1:
            cur_x += 1
            if instructions[i+1][0] == 'D':
                cur_c = '┓'
                coordinates.append((cur_y, cur_x, cur_c))
            elif instructions[i+1][0] == 'U':
                cur_c = '┛'
                coordinates.append((cur_y, cur_x, cur_c))
        
    elif instruction[0] == 'L':
        cur_c = '<'
        for _ in range(1, int(instruction[1])):
            cur_x -= 1
            coordinates.append((cur_y, cur_x, cur_c))
            
        if i < len(instructions) - 1:
            cur_x -= 1
            if instructions[i+1][0] == 'D':
                cur_c = '┏'
                coordinates.append((cur_y, cur_x, cur_c))
            elif instructions[i+1][0] == 'U':
                cur_c = '┖'
                coordinates.append((cur_y, cur_x, cur_c))
        
    elif instruction[0] == 'D':
        cur_c = 'v'
        for _ in range(1, int(instruction[1])):
            cur_y += 1
            coordinates.append((cur_y, cur_x, cur_c))
            
        if i < len(instructions) - 1:
            cur_y += 1
            if instructions[i+1][0] == 'R':
                cur_c = '┖'
                coordinates.append((cur_y, cur_x, cur_c))
            elif instructions[i+1][0] == 'L':
                cur_c = '┛'
                coordinates.append((cur_y, cur_x, cur_c))
        
    elif instruction[0] == 'U':
        cur_c = '^'
        for _ in range(1, int(instruction[1])):
            cur_y -= 1
            coordinates.append((cur_y, cur_x, cur_c))
            
        if i < len(instructions) - 1:
            cur_y -= 1
            if instructions  [i+1][0] == 'R':
                cur_c = '┏'
                coordinates.append((cur_y, cur_x, cur_c))
            elif instructions[i+1][0] == 'L':
                cur_c = '┓'
                coordinates.append((cur_y, cur_x, cur_c))
                
# Shift coordinates to account for negatives values

min_y = min([coord[0] for coord in coordinates])
min_x = min([coord[1] for coord in coordinates])
max_y = max([coord[0] for coord in coordinates])
max_x = max([coord[1] for coord in coordinates])

coordinates_shifted = [(y + abs(min_y) + 1, x + abs(min_x) + 1, c) for (y, x, c) in coordinates]

min_y_shifted = min([coord[0] for coord in coordinates_shifted])
min_x_shifted = min([coord[1] for coord in coordinates_shifted])
max_y_shifted = max([coord[0] for coord in coordinates_shifted])
max_x_shifted = max([coord[1] for coord in coordinates_shifted])

print(min_y, max_y, min_x, max_x, '-->', min_y_shifted, max_y_shifted, min_x_shifted, max_x_shifted)

# Create matrix from coordinates

coords_dict = {(y,x): c for (y,x,c) in coordinates_shifted}
worldmap = [[coords_dict[(y,x)] if (y,x) in coords_dict else '.' for x in range(max_x_shifted+1)] for y in range(max_y_shifted+1)]
print(len(worldmap[0]), len(worldmap))

# Count all elements inside the loop 

insideLoop = False
counter    = 0
inside     = {}

for y, blocs in enumerate(worldmap):
    for x, bloc in enumerate(blocs):
        if bloc in ['┛','┖', '^', 'v'] :
            insideLoop = not insideLoop
        else:
            if insideLoop:
                inside[(y,x)] = bloc
                
worldmap_filled = [['#' if (y,x) in inside or c != '.' else '.' for x, c in enumerate(row)] for y, row in enumerate(worldmap)]
count_filled    = sum([sum([1 if c == '#' else 0 for c in row]) for row in worldmap_filled])
count_filled