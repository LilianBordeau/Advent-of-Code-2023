import heapq

# Get data

input_file = "input_day_17.txt"

worldmap = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        #strings = line.split(',')
        #strings.append(string)
        worldmap.append(blocs)
        #print(line)
        

current_x, current_y = 0, 0
end_x, end_y = len(worldmap) - 1, len(worldmap[0]) - 1

worldmap_e = [['.' for v in row] for row in worldmap]
explored   = {(x, y): False for x, row in enumerate(worldmap) for y, col in enumerate(row)}

distances = {(x, y): float('inf') for x, row in enumerate(worldmap) for y, col in enumerate(row)}
distances[(current_x, current_y)] = 0
min_heap = [(0, (current_x, current_y))]

while (current_x != end_x) and (current_y != end_y):
    
    explored[(current_x, current_y)] = True
    
    neighbours = {}
    
    # Left
    if (current_x - 1, current_y) in explored and explored[(current_x - 1, current_y)] is False:
        neighbours['left'] = worldmap[current_y][current_x - 1]
    
    # Top
    if (current_x, current_y - 1) in explored and explored[(current_x, current_y - 1)] is False:
        neighbours['top']  = worldmap[current_y - 1][current_x]
        
    # Right
    if (current_x + 1, current_y) in explored and explored[(current_x + 1, current_y)] is False:
        neighbours['right'] = worldmap[current_y][current_x + 1]
        
    # Bottom
    if (current_x, current_y + 1) in explored and explored[(current_x, current_y + 1)] is False:
        neighbours['bottom'] = worldmap[current_y + 1][current_x]
    
    min_dir = min(neighbours, key=neighbours.get)
    
    if min_dir == 'left':
        worldmap_e[current_y][current_x] = '<'
        current_x -= 1
    if min_dir == 'top':
        worldmap_e[current_y][current_x] = '^'
        current_y -= 1
    if min_dir == 'right':
        worldmap_e[current_y][current_x] = '>'
        current_x += 1
    if min_dir == 'bottom':
        worldmap_e[current_y][current_x] = 'v'
        current_y += 1
    
# Dijsktra

def find_shortest_path(worldmap):
    rows, cols = len(worldmap), len(worldmap[0])
    start, end = (0, 0), (rows - 1, cols - 1)
    directions  = ['up', 'down', 'left', 'right']
    dir_offsets = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    
    strait_line_counter = 0

    # Initialize distance and predecessor maps
    distances = {(x, y): float('inf') for x in range(rows) for y in range(cols)}
    distances[start] = 0
    predecessors = {}

    # Min heap for the nodes to be explored
    min_heap = [(0, start, None, 0)]

    while min_heap:
        dist, (current_x, current_y), current_dir, steps = heapq.heappop(min_heap)

        # Stop if we reach the end point
        if (current_x, current_y) == end:
            break

        # Explore neighbors
        for dir in directions:
            dy, dx = dir_offsets[dir]  # Left, Top, Right, Bottom
            next_x, next_y = current_x + dx, current_y + dy
            next_steps = steps + 1 if (dir == current_dir or dir == opposite_direction(current_dir)) else 1

            if 0 <= next_x < rows and 0 <= next_y < cols:
                if dir == opposite_direction(current_dir) or (next_steps >= 3):
                    continue
                    
                new_dist = dist + int(worldmap[next_x][next_y]) 
                
                #print(next_x, next_y, new_dist)
                
                if (new_dist < distances[(next_x, next_y)]):
                    distances   [(next_x, next_y)] = new_dist
                    predecessors[(next_x, next_y)] = (current_x, current_y)
                    heapq.heappush(min_heap, (new_dist, (next_x, next_y), dir, next_steps))

    #print(distances)
    # Reconstruct the path
    if end not in predecessors:
        return None  # Path not found

    path = []
    current = end
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()

    return path

# Run the function with the worldmap matrix
shortest_path = find_shortest_path(worldmap)


# A* 

def heuristic(a, b):
    """Calculate the heuristic distance between two points (Manhattan distance)."""
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def modified_heuristic(a, b):
    """Calculate a modified heuristic distance considering potential turns."""
    manhattan_distance = heuristic(a, b)
    x1, y1 = a
    x2, y2 = b
    # Estimating the number of turns needed (conservatively) and adding it to the heuristic
    estimated_turns = manhattan_distance
    return manhattan_distance + estimated_turns

def opposite_direction(direction):
    """Returns the opposite direction."""
    opposites = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
    return opposites.get(direction)

def a_star_search(city_map):
    rows, cols  = len(city_map), len(city_map[0])
    start, goal = (0, 0), (rows - 1, cols - 1)
    directions  = ['up', 'down', 'left', 'right']
    dir_offsets = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    open_set = []
    heapq.heappush(open_set, (0, start, 'down', 0))  # (cost, (x, y), direction, steps_in_current_direction)
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current, current_dir, steps = heapq.heappop(open_set)
        current_x, current_y = current

        if current == goal:
            break

        for dir in directions:
            dx, dy = dir_offsets[dir]
            next_x, next_y = current_x + dx, current_y + dy
            next_steps = steps + 1 if (dir == current_dir or dir == opposite_direction(current_dir)) else 1
            #print(next_steps)

            if 0 <= next_x < rows and 0 <= next_y < cols and next_steps <= 3:
                if dir == opposite_direction(current_dir): 
                    continue

                new_cost = cost_so_far[current] + int(city_map[next_x][next_y])
                if (next_x, next_y) not in cost_so_far or new_cost < cost_so_far[(next_x, next_y)]:
                    #print(next_x, next_y)
                    cost_so_far[(next_x, next_y)] = new_cost
                    priority = new_cost + modified_heuristic(goal, (next_x, next_y))
                    heapq.heappush(open_set, (priority, (next_x, next_y), dir, next_steps))
                    came_from[(next_x, next_y)] = current
                    
    #print(came_from)

    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path, cost_so_far[goal]

# Execute the A* search algorithm with the revised approach
shortest_path, total_cost = a_star_search(worldmap)
#found_path, total_cost


prev_x, prev_y = 0, 0
cons_x, cons_y = 0, 0
minc_x, minc_y = [], []

for (x,y) in shortest_path:
    #print(x,y)
    
    if x == prev_x:
        cons_x += 1
    else:
        minc_x.append(cons_x)
        cons_x = 0
        
    if y == prev_y:
        cons_y += 1
    else:
        minc_y.append(cons_y)
        cons_y = 0
        
    prev_x, prev_y = x, y
        
max(minc_x), max(minc_y)


worldmap_e = [['.' for v in row] for row in worldmap]

score = 0
for (x,y) in shortest_path:
    score += int(worldmap[x][y])
    worldmap_e[x][y] = '#'

print(score)
print_matrice(worldmap_e)
#score