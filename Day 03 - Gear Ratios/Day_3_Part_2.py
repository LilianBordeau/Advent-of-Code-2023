# Part Two

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_3.txt"

matrice = []

# creation matrice
with open(input_file, "r") as f:
    for line in f:
        line = line.replace('\n','')
        chars = []
        for c in line: chars.append(c)
        matrice.append(chars)

max_i = len(matrice)    - 1
max_j = len(matrice[0]) - 1

print('taille matrice:', max_i, max_j)

gears = {}

for i, line in enumerate(matrice):
    
    tmp_number    = []
    tmp_adjacents = []
    local_gears   = []
    
    for j, char in enumerate(line):
        if char in '1234567890':
            
            # build adjacents matrix
            adjacents = []
            
            if i != 0 and i != max_i:
                
                if j != 0 and j != max_j:
                    adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == 0:
                    #adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    #adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    #adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == max_j:
                    adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    #adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    #adjacents.append((matrice[i  ][j+1], i  , j+1))
                    adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    #adjacents.append((matrice[i+1][j+1], i+1, j+1))
                
            elif i == 0:                
                if j != 0 and j != max_j:
                    #adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    #adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    #adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == 0:
                    #adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    #adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    #adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    #adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    #adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == max_j:
                    #adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    #adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    #adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    #adjacents.append((matrice[i  ][j+1], i  , j+1))
                    adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    #adjacents.append((matrice[i+1][j+1], i+1, j+1))
                    
            elif i == max_i:
                
                if j != 0 and j != max_j:
                    adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    #adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    #adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    #adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == 0:
                    #adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    #adjacents.append((matrice[i  ][j-1], i  , j-1))
                    adjacents.append((matrice[i  ][j+1], i  , j+1))
                    #adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    #adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    #adjacents.append((matrice[i+1][j+1], i+1, j+1))
                elif j == max_j:
                    adjacents.append((matrice[i-1][j-1], i-1, j-1))
                    adjacents.append((matrice[i-1][j  ], i-1, j  ))
                    #adjacents.append((matrice[i-1][j+1], i-1, j+1))
                    adjacents.append((matrice[i  ][j-1], i  , j-1))
                    #adjacents.append((matrice[i  ][j+1], i  , j+1))
                    #adjacents.append((matrice[i+1][j-1], i+1, j-1))
                    #adjacents.append((matrice[i+1][j  ], i+1, j  ))
                    #adjacents.append((matrice[i+1][j+1], i+1, j+1))  
            
            adjacent_gears = [(adj[1], adj[2]) for adj in adjacents if adj[0] == '*']
            
            if len(adjacent_gears) > 0:
                local_gears.append(adjacent_gears)
                
            
            #print(adjacents, adjacent_gears)
            
            is_adjacent_to_gear = any([True if adj[0] == '*' else False for adj in adjacents])
            
            tmp_number.append(char)
            tmp_adjacents.append(is_adjacent_to_gear)
            
            if j == max_j:
                if any(tmp_adjacents):
                    number      = int(''.join(tmp_number))
                    local_gears = [item for row in local_gears for item in row]
                    local_gears = list(set(local_gears))

                    for gear in local_gears:
                        if gear in gears:
                            gears[gear].append(number)
                        else:
                            gears[gear] = [number]
                            
                    tmp_number    = []
                    tmp_adjacents = []
                    local_gears   = []
            
        else:
            if any(tmp_adjacents):
                number      = int(''.join(tmp_number))
                local_gears = [item for row in local_gears for item in row]
                local_gears = list(set(local_gears))
                
                for gear in local_gears:
                    if gear in gears:
                        gears[gear].append(number)
                    else:
                        gears[gear] = [number]
            
            tmp_number    = []
            tmp_adjacents = []
            local_gears   = []
    
gears  = {k:v for k,v in gears.items() if len(v) == 2}
result = sum([v[0] * v[1] for k,v in gears.items()])
print('Résultat:', result)