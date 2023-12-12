# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_11.txt"

galaxy     = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        galaxy.append(blocs)
        
print(len(galaxy[0]), len(galaxy))

empty_line = ['.'] * len(galaxy[0])

to_insert_horizontal = []

for i, ray in enumerate(galaxy):
    if all([v == '.' for v in ray]):
        to_insert_horizontal.append(i)

shift = 0
for i in to_insert_horizontal:
    galaxy = galaxy[:i+shift] + ([empty_line] * expansion) + galaxy[i+shift:]
    shift  += expansion
    
print(len(galaxy[0]), len(galaxy))

empty_line = ['.'] * len(galaxy_transpose[0])

to_insert_vertical = []

for i, ray in enumerate(galaxy_transpose):
    if all([v == '.' for v in ray]):
        to_insert_vertical.append(i)

shift = 0
for i in to_insert_vertical:
    galaxy_transpose = galaxy_transpose[:i+shift] + ([empty_line] * expansion) + galaxy_transpose[i+shift:]
    shift            += expansion
    
stars = []

for i, line in enumerate(galaxy):
    for j, c in enumerate(line):
        if c == '#': stars.append((i,j))
        
print(len(stars), 'étoiles.')

pairs = list(itertools.combinations(stars, 2))
print(len(pairs), 'paires.')

distances = {}

for i, (s1, s2) in enumerate(pairs):
    
    distance_x          = (max(s1[0], s2[0]) - min(s1[0], s2[0])) + len(vertical_empty_line_local)   * (expansion-1)
    distance_y          = (max(s1[1], s2[1]) - min(s1[1], s2[1])) + len(horizontal_empty_line_local) * (expansion-1)
    distance            = distance_x + distance_y
    distances[(s1, s2)] = distance
        
sum([v for v in distances.values()])