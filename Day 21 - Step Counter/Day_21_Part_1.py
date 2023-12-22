input_file  = "input_day_21.txt"

worldmap = []

with open(input_file, "r") as f:

    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        worldmap.append(blocs)
        
def find_and_replace_start(worldmap):
    for y, row in enumerate(worldmap):
        for x, char in enumerate(row):
            if char == 'S':
                start_x = x
                start_y = y
                worldmap[y][x] = '.'
                break
    return (start_x, start_y)

start_x, start_y = find_and_replace_start(worldmap)
print(start_x, start_y)

#@cache
def expand(worldmap, positions):
    
    positions      = list(positions)
    next_positions = []
    
    height = len(worldmap)    - 1
    width  = len(worldmap[0]) - 1
    
    oobs   = []
    
    for (pos_y, pos_x) in positions:
        
        top = bottom = left = right = False
        
        if (pos_y >      0) : top    = True if worldmap[pos_y - 1][pos_x    ] == '.' else False
        if (pos_y < height) : bottom = True if worldmap[pos_y + 1][pos_x    ] == '.' else False
        if (pos_x >      0) : left   = True if worldmap[pos_y    ][pos_x - 1] == '.' else False
        if (pos_x <  width) : right  = True if worldmap[pos_y    ][pos_x + 1] == '.' else False

        if top    : next_positions.append((pos_y - 1, pos_x    ))
        if bottom : next_positions.append((pos_y + 1, pos_x    ))
        if left   : next_positions.append((pos_y    , pos_x - 1))
        if right  : next_positions.append((pos_y    , pos_x + 1))
    
    next_positions = tuple(v for v in (set(tuple(t) for t in next_positions)))
    
    return next_positions

(start_y, start_x) = 327, 327

positions = ((start_y, start_x), (start_y, start_x))
NB_STEPS  = 500

results   = []

oobs = ()

for i in range(1, NB_STEPS + 1):
    
    #print(len(positions), positions)
    
    positions = expand(positions)
    results.append(len(positions))
    
    #print('Step', i, '==>', len(positions), 'garden plots reached.')

print()
print('Step', i, '==>', len(positions), 'garden plots reached.')