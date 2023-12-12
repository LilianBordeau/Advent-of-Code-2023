# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_10.txt"

labyrinth  = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        #print(line, '==> START') if 'S' in line else print(line)
        blocs = list(line)
        labyrinth.append(blocs)
        
for i, blocs in enumerate(labyrinth):
    #print(''.join(blocs))
    start_y = i
    if 'S' in blocs:
        #print('STOP')
        start_x = blocs.index('S')
        break

print('Start coordinates:', start_x, start_y)

# Explore (part 1)

current_pos_x = start_x
current_pos_y = start_y
current_tile  = labyrinth[current_pos_y][current_pos_x]

#print(current_pos_x, current_pos_y, current_tile)

history = {}

for i in range(20000):
    
    #print(current_pos_y, current_pos_x, '==>', current_tile)
    
    #if current_tile != 'S':
    #    labyrinth[current_pos_y][current_pos_x] = '■'
    
       
    if current_pos_x == start_x and current_pos_y == start_y and i > 0: 
        print('ARRIVED')
        break
    
    
    # Start position
    if current_tile == 'S':
        labyrinth[current_pos_y][current_pos_x] = 'J'
        prvious_pos_x = current_pos_x
        prvious_pos_y = current_pos_y
        history[(current_pos_y, current_pos_x)] = 'D'
        current_pos_x -= 1
    
    # Down or Right
    elif current_tile == 'F':
        labyrinth[current_pos_y][current_pos_x] = '┏'
        if prvious_pos_x == current_pos_x + 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_y += 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_x += 1
    
    # Up or Right
    elif current_tile == 'L':
        labyrinth[current_pos_y][current_pos_x] = '┖'
        if prvious_pos_x == current_pos_x + 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_y -= 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_x += 1
        
    # Down or Left
    elif current_tile == '7':
        labyrinth[current_pos_y][current_pos_x] = '┓'
        if prvious_pos_x == current_pos_x - 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_y += 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_x -= 1
        
    # Up or Left
    elif current_tile == 'J':
        labyrinth[current_pos_y][current_pos_x] = '┛'
        if prvious_pos_x == current_pos_x - 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_y -= 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_x -= 1
        
    # Left or Right
    elif current_tile == '-':
        labyrinth[current_pos_y][current_pos_x] = '━'
        if prvious_pos_x == current_pos_x - 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_x += 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'P'
            current_pos_x -= 1
        
    # Up or Down
    elif current_tile == '|': 
        labyrinth[current_pos_y][current_pos_x] = '┃'
        if prvious_pos_y == current_pos_y - 1:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_y += 1
        else:
            prvious_pos_x = current_pos_x
            prvious_pos_y = current_pos_y
            history[(current_pos_y, current_pos_x)] = 'D'
            current_pos_y -= 1
    
    current_tile = labyrinth[current_pos_y][current_pos_x]
    
print(i, len(history))