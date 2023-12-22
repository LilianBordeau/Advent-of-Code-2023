# Get data

input_file = "input_day_12.txt"

springs = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        #print(line)
        encoded_spring = line.split(' ')[0]
        arrangements   = [int(n) for n in line.split(' ')[1].split(',')]
        springs.append((encoded_spring, arrangements))
        
@cache
def poss(springs, counts, hashes=0, require=None):

    if require == '#' and (springs == '' or springs[0] == '.'): return 0

    firstgrp = 0
    for i, char in enumerate(springs+'X'):
        if char != '#':
            firstgrp = i
            break

    if require == '.' and firstgrp:
        assert hashes == 0
        return 0

    if counts == ():
        if '#' in springs:
            return 0
        return 1

    tail = springs[firstgrp:]

    # If we start with some hashes
    if firstgrp != 0:
        if counts == ():
            return 0

        # The right amount
        if hashes+firstgrp == counts[0]:
            return poss(tail, counts[1:], hashes=0, require='.')

        # Not enough
        if hashes+firstgrp < counts[0]:
            a = poss(tail, counts, hashes=hashes+firstgrp, require='#')
            return a

        # Too many
        if hashes+firstgrp > counts[0]:
            return 0

    if springs == '':
        assert counts != ()
        return 0

    head, tail = springs[0], springs[1:]

    # If we start with dot
    if head == '.':
        return poss(tail, counts)

    # With qmark
    if head == '?':
        a = poss('#'+tail, counts, hashes=hashes, require=require)
        b = poss('.'+tail, counts, hashes=hashes, require=require)
        return a + b
    
def get_all_permutations_dynamic(encoded_string, arrangements):
    count_joker = encoded_string.count('?')
    count_sprng = encoded_string.count('#')
    needed = sum(arrangements) - count_sprng
    
    indexes = []
    
    for i, c in enumerate(encoded_string):
        if c == '?':
            indexes.append(i)
            
    possibles_replacements = list(itertools.combinations(indexes, needed))
    
    new_strings = []
            
    for possible_replacement in possibles_replacements:
        new_string = encoded_string
        for i in possible_replacement:
            new_string = new_string[:i]+'#'+new_string[i+1:]
        
        new_string = new_string.replace('?', '.')
        new_strings.append(new_string)
            
    return new_strings
    
def get_all_permutations(encoded_string, arrangements):
    count_joker = encoded_string.count('?')
    count_sprng = encoded_string.count('#')
    needed = sum(arrangements) - count_sprng
    
    indexes = []
    
    for i, c in enumerate(encoded_string):
        if c == '?':
            indexes.append(i)
            
    possibles_replacements = list(itertools.combinations(indexes, needed))
    
    new_strings = []
            
    for possible_replacement in possibles_replacements:
        new_string = encoded_string
        for i in possible_replacement:
            new_string = new_string[:i]+'#'+new_string[i+1:]
        
        new_string = new_string.replace('?', '.')
        new_strings.append(new_string)
            
    return new_strings

def return_arrangement_from_strings(encoded_string):
    
    count_local = 0
    arrangement = []

    for c in encoded_string:
        #print(c)
        if c == '#':
            count_local += 1
        else:
            if count_local > 0:
                arrangement.append(count_local)
                count_local = 0

    if encoded_string[-1] == '#':
        arrangement.append(count_local)

    return arrangement

def find_arrangements_number(encoded_string, arrangements):
    
    permutations = get_all_permutations(encoded_string, arrangements)
    
    is_valid = 0
    
    for permutation in permutations:
        arrangement = return_arrangement_from_strings(permutation)
        if arrangement == arrangements:
            is_valid += 1
            
    return is_valid

possibles = []

for encoded_string, arrangements in springs:
    
    nb = find_arrangements_number(encoded_string, arrangements)
    
    possibles.append(nb)
    
print(sum(possibles))