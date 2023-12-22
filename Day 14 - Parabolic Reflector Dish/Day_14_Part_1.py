# Get data

input_file = "input_day_14.txt"

platform = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        platform.append(blocs)
        
platform = tuple(tuple(row) for row in platform)

def rotate_matrice_clockwise(matrice):
     #list(map(list, zip(*matrice)))
    return list(map(list, zip(*reversed(matrice))))

def rotate_tuple_matrice_clockwise(matrice):
     #list(map(list, zip(*matrice)))
    return tuple(map(tuple, zip(*reversed(matrice))))

@cache
def get_score_from_rocks(matrice):
    
    score = 0
    
    for i, row in enumerate(matrice):
        score += (len(matrice) - i) * sum([1 for c in row if c == 'O'])
    
    return score


def let_rocks_roll(matrice):
    for row in matrice:
        index_further = -1

        for i in range(len(row) - 1, -1, -1):
            #print(i)
            if row[i] == '.':
                if index_further == -1:
                    index_further = i

            if row[i] == 'O':
                if index_further != -1:
                    row[index_further] = 'O'
                    row[i]             = '.'
                    index_further      -= 1

            if row[i] == '#':
                if index_further != -1:
                    index_further = -1
                    
    return matrice

t_platform = rotate_matrice_clockwise(platform)
t_platform = let_rocks_roll(t_platform)
t_platform = rotate_matrice_clockwise(t_platform)
t_platform = rotate_matrice_clockwise(t_platform)
t_platform = rotate_matrice_clockwise(t_platform)
get_score_from_rocks(t_platform)