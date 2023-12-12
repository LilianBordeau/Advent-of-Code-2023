# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_11.txt"

galaxy     = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        galaxy.append(blocs)
        
print(len(galaxy[0]), len(galaxy))

expansion = 1000000

horizontal_empty_line = []
vertical_empty_line   = []

for i, ray in enumerate(galaxy):
    if all([v == '.' for v in ray]):
        horizontal_empty_line.append(i)

for i, ray in enumerate(list(map(list, zip(*galaxy)))):
    if all([v == '.' for v in ray]):
        vertical_empty_line.append(i)
        
print('Nb lignes horizontal vides:', len(horizontal_empty_line))
print('Nb lignes vertical vides:',   len(vertical_empty_line))
    
stars = []

for i, line in enumerate(galaxy):
    for j, c in enumerate(line):
        if c == '#': stars.append((i,j))
        
print(len(stars), 'étoiles.')

pairs = list(itertools.combinations(stars, 2))
print(len(pairs), 'paires.')

distances = {}

for i, (s1, s2) in enumerate(pairs):

    horizontal_empty_line_local = [line for line in horizontal_empty_line if min(s1[0], s2[0]) < line < max(s1[0], s2[0])]
    vertical_empty_line_local   = [line for line in vertical_empty_line   if min(s1[1], s2[1]) < line < max(s1[1], s2[1])]
    
    distance_x          = (max(s1[0], s2[0]) - min(s1[0], s2[0])) + len(vertical_empty_line_local)   * (expansion-1)
    distance_y          = (max(s1[1], s2[1]) - min(s1[1], s2[1])) + len(horizontal_empty_line_local) * (expansion-1)
    distance            = distance_x + distance_y
    distances[(s1, s2)] = distance
        
sum([v for v in distances.values()])