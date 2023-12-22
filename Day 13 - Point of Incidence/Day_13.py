def print_matrice(matrice):
    for ligne in matrice:
        for elem in ligne:
            print(elem, end='')
        print()
        
def transpose_matrice(matrice):
    return list(map(list, zip(*matrice)))

# Get data

input_file = "input_day_13.txt"

terrains = []
terrain  = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        blocs = list(line)
        
        if line == '':
            terrains.append(terrain)
            terrain = []
        else:
            terrain.append(blocs)
            
    terrains.append(terrain)
    
def detect_reflections_similarity(matrix):
    tmp_line    = matrix[0]
    
    reflections = []
    
    for i in range(1,len(matrix)):
        diff = sum([0 if l1 == l2 else 1 for l1, l2 in zip(matrix[i], tmp_line)])
        if diff == 1:
            reflections.append((i-1,i))
        tmp_line = matrix[i]
                    
    return reflections

def get_pattern_note(matrix, v=False):
    
    height = len(matrix)
    length = len(matrix[0])
    
    t_matrix = transpose_matrice(matrix)
    t_height = len(t_matrix)
    t_length = len(t_matrix[0])
    
    horizontal_symetries = detect_reflections(matrix)
    vertical_symetries   = detect_reflections(t_matrix)
    
    res = 0
    
    print(horizontal_symetries, vertical_symetries)
    
    for sym in horizontal_symetries:
        is_perfect = is_perfect_reflection(matrix, sym)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('perfect h =>', sym, sym_length)
            res += (sym_length * 100)
        else:
            sym_length = sym[1]
            #sym_length = get_reflection_length(matrix, sym)
            if v: print('flawed  h =>', sym, sym_length)
            #res += (sym_length * 100)
        
    for sym in vertical_symetries:
        is_perfect = is_perfect_reflection(t_matrix, sym)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('perfect v =>', sym, sym_length)
            res += sym_length
        else:
            sym_length = get_reflection_length(t_matrix, sym)
            if v: print('flawed  v =>', sym, sym_length)
        
    if (len(horizontal_symetries) == 0) and (len(vertical_symetries) == 0):
        if v: print('No symetry detected.')
        return -1
        
    return res

def is_perfect_reflection(matrice, sym):
    
    is_perfect = True
    
    top   = sym[0]
    under = len(matrice)-sym[1]
    
    #print(top,under)
    
    i_max      = min(sym[0], len(matrice)-sym[1]-1) 
    
    #print(i_max)
    
    for i in range(1, i_max+1):
        #print(i, sym[0]-i, sym[1]+i)
        if matrice[sym[0]-i] != matrice[sym[1]+i]:
            is_perfect = False
    
    return is_perfect

def get_reflection_length(matrice, sym):
    
    length     = 1
    
    i_max      = min(sym[0], len(matrice)-sym[1]-1) 
    
    for i in range(1, i_max+1):
        #print(i, sym[0]-i, sym[1]+i)
        if matrice[sym[0]-i] != matrice[sym[1]+i]:
            break
        else:
            length += 1
    
    return length

def summarize_pattern_notes(matrices, v=False):
    
    notes = []

    for i, matrice in enumerate(matrices):

        if v: print_matrice(matrice)

        note = get_pattern_note(matrice, v)

        if v: print('==>', note)

        if note != -1:
            notes.append(note)

        if v: print()

    return sum(notes)

def is_perfect_reflection_similarity(matrice, sym, char_rplcd=False):
    
    is_perfect = True
    char_rplcd = char_rplcd
    
    i_max      = min(sym[0], len(matrice)-sym[1]-1) 
    
    for i in range(1, i_max+1):
        
        diff = sum([0 if r1 == r2 else 1 for r1, r2 in zip(matrice[sym[0]-i] , matrice[sym[1]+i])])
        
        if diff > 1:
            is_perfect = False
            break
        if diff == 1:
            if char_rplcd:
                is_perfect = False
                break
            else:
                char_rplcd = True
    
    return is_perfect

def get_pattern_note_similarity(matrix, v=False):
    
    height = len(matrix)
    length = len(matrix[0])
    
    t_matrix = transpose_matrice(matrix)
    t_height = len(t_matrix)
    t_length = len(t_matrix[0])
    
    horizontal_symetries = detect_reflections(matrix)
    vertical_symetries   = detect_reflections(t_matrix)
    
    candidates_horizontal_symetries = detect_reflections_similarity(matrix)
    candidates_vertical_symetries   = detect_reflections_similarity(t_matrix)
    
    res = 0
    
    #print(horizontal_symetries, vertical_symetries)
    
    for sym in horizontal_symetries:
        is_perfect_already = is_perfect_reflection_similarity(matrix, sym, True)
        if is_perfect_already:
            #if v: print('perfect already h =>', sym)
            continue
        
        is_perfect = is_perfect_reflection_similarity(matrix, sym, False)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('new perfect h =>', sym, sym_length)
            res += (sym_length * 100)
        else:
            sym_length = sym[1]
            #if v: print('new flawed  h =>', sym, sym_length)
            
    for sym in candidates_horizontal_symetries:
        is_perfect = is_perfect_reflection_similarity(matrix, sym, True)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('new consecutive perfect h =>', sym)
            res += (sym_length * 100)
        else:
            sym_length = sym[1]
            #if v: print('new consecutive flawed  h =>', sym, sym_length)
        
        
    for sym in vertical_symetries:
        is_perfect_already = is_perfect_reflection_similarity(t_matrix, sym, True)
        if is_perfect_already:
            #if v: print('perfect already v =>', sym)
            continue
        
        is_perfect = is_perfect_reflection_similarity(t_matrix, sym, False)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('new perfect v =>', sym, sym_length)
            res += sym_length
        else:
            sym_length = get_reflection_length(t_matrix, sym)
            #if v: print('new flawed  v =>', sym, sym_length)
            
    for sym in candidates_vertical_symetries:
        is_perfect = is_perfect_reflection_similarity(t_matrix, sym, True)
        
        if is_perfect:
            sym_length = sym[1]
            if v: print('new consecutive perfect v =>', sym, sym_length)
            res += sym_length
        else:
            sym_length = get_reflection_length(t_matrix, sym)
            #if v: print('new consecutive flawed  v =>', sym, sym_length)
        
    if (len(horizontal_symetries) == 0) and (len(vertical_symetries) == 0):
        if v: print('No symetry detected.')
        return -1
        
    return res

def summarize_pattern_notes_similarity(matrices, v=False):
    
    notes = []

    for i, matrice in enumerate(matrices):

        if v: print(i)
        if v: print_matrice(matrice)

        note = get_pattern_note_similarity(matrice, v)

        if v: print('==>', note)

        if note != -1:
            notes.append(note)

        if v: print()

    return sum(notes)

final_note = summarize_pattern_notes_similarity(terrains, False)
final_note