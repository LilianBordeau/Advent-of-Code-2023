# Part One

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

selected_numbers = []

for i, line in enumerate(matrice):
    
    tmp_number     = []
    tmp_adjacents  = []
    selecteds_line = []
    
    for j, char in enumerate(line):
        if char in '1234567890':
            
            # build adjacents matrix
            adjacents = []
            
            if i != 0 and i != max_i:
                
                if j != 0 and j != max_j:
                    adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    adjacents.append(matrice[i+1][j+1])
                elif j == 0:
                    #adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    adjacents.append(matrice[i-1][j+1])
                    #adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    #adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    adjacents.append(matrice[i+1][j+1])
                elif j == max_j:
                    adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    #adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    #adjacents.append(matrice[i][j+1])
                    adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    #adjacents.append(matrice[i+1][j+1])
                
            elif i == 0:                
                if j != 0 and j != max_j:
                    #adjacents.append(matrice[i-1][j-1])
                    #adjacents.append(matrice[i-1][j])
                    #adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    adjacents.append(matrice[i+1][j+1])
                elif j == 0:
                    #adjacents.append(matrice[i-1][j-1])
                    #adjacents.append(matrice[i-1][j])
                    #adjacents.append(matrice[i-1][j+1])
                    #adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    #adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    adjacents.append(matrice[i+1][j+1])
                elif j == max_j:
                    #adjacents.append(matrice[i-1][j-1])
                    #adjacents.append(matrice[i-1][j])
                    #adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    #adjacents.append(matrice[i][j+1])
                    adjacents.append(matrice[i+1][j-1])
                    adjacents.append(matrice[i+1][j])
                    #adjacents.append(matrice[i+1][j+1])
                    
            elif i == max_i:
                
                if j != 0 and j != max_j:
                    adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    #adjacents.append(matrice[i+1][j-1])
                    #adjacents.append(matrice[i+1][j])
                    #adjacents.append(matrice[i+1][j+1])
                elif j == 0:
                    #adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    adjacents.append(matrice[i-1][j+1])
                    #adjacents.append(matrice[i][j-1])
                    adjacents.append(matrice[i][j+1])
                    #adjacents.append(matrice[i+1][j-1])
                    #adjacents.append(matrice[i+1][j])
                    #adjacents.append(matrice[i+1][j+1])
                elif j == max_j:
                    adjacents.append(matrice[i-1][j-1])
                    adjacents.append(matrice[i-1][j])
                    #adjacents.append(matrice[i-1][j+1])
                    adjacents.append(matrice[i][j-1])
                    #adjacents.append(matrice[i][j+1])
                    #adjacents.append(matrice[i+1][j-1])
                    #adjacents.append(matrice[i+1][j])
                    #adjacents.append(matrice[i+1][j+1])       
            
            is_adjacent_to_symbol = any([True  if adj not in '.0123456789' else False for adj in adjacents])
            
            tmp_number.append(char)
            tmp_adjacents.append(is_adjacent_to_symbol)
            
            if j == max_j:
                if any(tmp_adjacents):
                    selected = int(''.join(tmp_number))
                    selecteds_line.append(selected)
                    tmp_number    = []
                    tmp_adjacents = []
            
        else:
            
            if any(tmp_adjacents):
                selected = int(''.join(tmp_number))
                selecteds_line.append(selected)
            
            tmp_number    = []
            tmp_adjacents = []
    
    #print(i,': ',selecteds_line)
    selected_numbers.append(selecteds_line)

result = sum([sum(line) for line in selected_numbers])
print('Résultat:', result)