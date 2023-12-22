# Get data

input_file = "input_day_16.txt"

worldmap = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        worldmap.append(blocs)
        
energized = [['.' for v in row] for row in worldmap]
explored  = []

def explore(current_direction, current_x, current_y, i):
    
    if (current_x < 0) or\
       (current_x >= len(worldmap[0])) or\
       (current_y < 0) or\
       (current_y >= len(worldmap)):
        return False
    
    if (current_direction, current_x, current_y) in explored:
        return False
    else:
        explored.append((current_direction, current_x, current_y))
        
    if i == 10000:
        return False
    
    current_tile = worldmap[current_y][current_x]
    
    if current_tile == '\\':
        if current_direction == 'RIGHT':
            next_direction = 'DOWN'
            next_y         = current_y + 1
            explore(next_direction, current_x, next_y, i+1)
            
        elif current_direction == 'LEFT':
            next_direction = 'TOP'
            next_y         = current_y - 1
            explore(next_direction, current_x, next_y, i+1)
            
        elif current_direction == 'TOP':
            next_direction = 'LEFT'
            next_x         = current_x - 1
            explore(next_direction, next_x, current_y, i+1)
            
        elif current_direction == 'DOWN':
            next_direction = 'RIGHT'
            next_x         = current_x + 1
            explore(next_direction, next_x, current_y, i+1)
    
    if current_tile == '/':
        if current_direction == 'LEFT':
            next_direction = 'DOWN'
            next_y         = current_y + 1
            explore(next_direction, current_x, next_y, i+1)
        
        elif current_direction == 'RIGHT':
            next_direction = 'TOP'
            next_y         = current_y - 1
            explore(next_direction, current_x, next_y, i+1)
            
        elif current_direction == 'TOP':
            next_direction = 'RIGHT'
            next_x         = current_x + 1
            explore(next_direction, next_x, current_y, i+1)
            
        elif current_direction == 'DOWN':
            next_direction = 'LEFT'
            next_x         = current_x - 1
            explore(next_direction, next_x, current_y, i+1)
    
    if current_tile == '|':
        if current_direction == 'LEFT':
            
            next_direction = 'TOP'
            next_y_1       = current_y - 1
            explore(next_direction, current_x, next_y_1, i+1)
            
            next_direction = 'DOWN'
            next_y_2       = current_y + 1
            explore(next_direction, current_x, next_y_2, i+1)
        
        elif current_direction == 'RIGHT':
            next_direction = 'TOP'
            next_y_1       = current_y - 1
            explore(next_direction, current_x, next_y_1, i+1)
            
            next_direction = 'DOWN'
            next_y_2       = current_y + 1
            explore(next_direction, current_x, next_y_2, i+1)
            
        elif current_direction == 'TOP':
            next_y         = current_y - 1
            explore(current_direction, current_x, next_y, i+1)
            
        elif current_direction == 'DOWN':
            next_y         = current_y + 1
            explore(current_direction, current_x, next_y, i+1)
        
    if current_tile == '-':            
        if current_direction == 'TOP':
            next_direction = 'LEFT'
            next_x_1       = current_x - 1
            explore(next_direction, next_x_1, current_y, i+1)
            
            next_direction = 'RIGHT'
            next_x_2       = current_x + 1
            explore(next_direction, next_x_2, current_y, i+1)
        
        elif current_direction == 'DOWN':
            next_direction = 'LEFT'
            next_x_1       = current_x - 1
            explore(next_direction, next_x_1, current_y, i+1)
            
            next_direction = 'RIGHT'
            next_x_2       = current_x + 1
            explore(next_direction, next_x_2, current_y, i+1)
            
        elif current_direction == 'LEFT':
            next_x         = current_x - 1
            explore(current_direction, next_x, current_y, i+1)
            
        elif current_direction == 'RIGHT':
            next_x         = current_x + 1
            explore(current_direction, next_x, current_y, i+1)
            
    if current_tile == '.':
        if current_direction == 'LEFT' :
            next_x         = current_x - 1
            explore(current_direction, next_x, current_y, i+1)

        if current_direction == 'RIGHT':
            next_x         = current_x + 1
            explore(current_direction, next_x, current_y, i+1)

        if current_direction == 'TOP'  :
            next_y         = current_y - 1
            explore(current_direction, current_x, next_y, i+1)

        if current_direction == 'DOWN' :
            next_y         = current_y + 1
            explore(current_direction, current_x, next_y, i+1)

    energized[current_y][current_x] = 'X'
    

def explore_iterative(start_direction, start_x, start_y):
    stack = [(start_direction, start_x, start_y, 0)]

    while stack:
        current_direction, current_x, current_y, i = stack.pop()

        if (current_x < 0) or (current_x >= len(worldmap[0])) or\
           (current_y < 0) or (current_y >= len(worldmap)):
            continue

        if (current_direction, current_x, current_y) in explored:
            continue
        else:
            explored.append((current_direction, current_x, current_y))

        if i == 10000:
            continue

        current_tile = worldmap[current_y][current_x]

        if current_tile == '\\':
            if current_direction == 'RIGHT':
                stack.append(('DOWN', current_x, current_y + 1, i+1))
            elif current_direction == 'LEFT':
                stack.append(('TOP', current_x, current_y - 1, i+1))
            elif current_direction == 'TOP':
                stack.append(('LEFT', current_x - 1, current_y, i+1))
            elif current_direction == 'DOWN':
                stack.append(('RIGHT', current_x + 1, current_y, i+1))

        elif current_tile == '/':
            if current_direction == 'LEFT':
                stack.append(('DOWN', current_x, current_y + 1, i+1))
            elif current_direction == 'RIGHT':
                stack.append(('TOP', current_x, current_y - 1, i+1))
            elif current_direction == 'TOP':
                stack.append(('RIGHT', current_x + 1, current_y, i+1))
            elif current_direction == 'DOWN':
                stack.append(('LEFT', current_x - 1, current_y, i+1))

        elif current_tile == '|':
            if current_direction in ['LEFT', 'RIGHT']:
                stack.append(('TOP', current_x, current_y - 1, i+1))
                stack.append(('DOWN', current_x, current_y + 1, i+1))
            else:
                stack.append((current_direction, current_x, current_y + (1 if current_direction == 'DOWN' else -1), i+1))

        elif current_tile == '-':
            if current_direction in ['TOP', 'DOWN']:
                stack.append(('LEFT', current_x - 1, current_y, i+1))
                stack.append(('RIGHT', current_x + 1, current_y, i+1))
            else:
                stack.append((current_direction, current_x + (1 if current_direction == 'RIGHT' else -1), current_y, i+1))

        elif current_tile == '.':
            if current_direction == 'LEFT':
                stack.append(('LEFT', current_x - 1, current_y, i+1))
            elif current_direction == 'RIGHT':
                stack.append(('RIGHT', current_x + 1, current_y, i+1))
            elif current_direction == 'TOP':
                stack.append(('TOP', current_x, current_y - 1, i+1))
            elif current_direction == 'DOWN':
                stack.append(('DOWN', current_x, current_y + 1, i+1))

        energized[current_y][current_x] = 'X'

        
current_direction  = 'RIGHT'
current_x, current_y = 0, 0
current_tile = worldmap[0][0]

explore_iterative(current_direction, current_x, current_y)

print(sum([sum([1 if v == 'X' else 0 for v in row]) for row in energized]))

top_rows    = [('DOWN', x, 0) for x in range(len(worldmap[0]))]
right_rows  = [('LEFT', len(worldmap[0])-1, y) for y in range(len(worldmap))]
bottom_rows = [('TOP', x, len(worldmap)-1) for x in range(len(worldmap[0]))]
left_rows   = [('RIGHT', 0, y) for y in range(len(worldmap))]

all_rows = top_rows + right_rows + bottom_rows + left_rows
print(len(all_rows))

results = {}

for row in all_rows:
    print(row)
    energized = [['.' for v in row] for row in worldmap]
    explored = []
    explore_iterative(row[0], row[1], row[2])
    score = sum([sum([1 if v == 'X' else 0 for v in row]) for row in energized])
    results[row] = score
    
print(max(results.values()))