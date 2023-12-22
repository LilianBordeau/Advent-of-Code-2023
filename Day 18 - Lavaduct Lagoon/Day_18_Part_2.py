# Create coordinates from instructions

cur_x, cur_y = 0, 0
coordinates  = []

for i, instruction in enumerate(instructions):
    hexa_range = instruction[-1][1:-1]
    deca_direc = instruction[-1][-1]
    
    deca_range = int(hexa_range, 16)
    currnt_dir = {'0':'R', '1':'D', '2':'L', '3':'U'}[deca_direc]
    
    if currnt_dir == 'R':
        cur_x += deca_range
        coordinates.append((cur_x, cur_y))
        
    elif currnt_dir == 'L':
        cur_x -= deca_range
        coordinates.append((cur_x, cur_y))
        
    elif currnt_dir == 'D':
        cur_y += deca_range
        coordinates.append((cur_x, cur_y))
        
    elif currnt_dir == 'U':
        cur_y -= deca_range
        coordinates.append((cur_x, cur_y))
        
#print(coordinates)

area = 0

for coord1, coord2 in zip(coordinates, coordinates[1:]):
    #print(coord1, coord2)
    determinant = (coord1[0] * coord2[1]) - (coord1[1] * coord2[0])
    area += determinant + (max(coord1[0], coord2[0]) - min(coord1[0], coord2[0])) + (max(coord1[1], coord2[1]) - min(coord1[1], coord2[1]))
    #print(coord1, coord2, determinant, area)

for coord1, coord2 in zip(coordinates[-1:], coordinates[0:]):
    #print(coord1, coord2)
    determinant = (coord1[0] * coord2[1]) - (coord1[1] * coord2[0])
    area += determinant + (max(coord1[0], coord2[0]) - min(coord1[0], coord2[0])) + (max(coord1[1], coord2[1]) - min(coord1[1], coord2[1]))
    #print(coord1, coord2, determinant, area)
    
area = (area // 2) + 1
print(area)