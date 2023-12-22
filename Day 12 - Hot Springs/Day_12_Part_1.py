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