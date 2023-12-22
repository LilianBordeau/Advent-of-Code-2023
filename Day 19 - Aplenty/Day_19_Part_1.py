# Get data // parse input

input_file = "input_day_19.txt"

firstPart = True

instructions_conds = {}
instructions_final = {}

ratings = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        
        if firstPart:
            part        = line.split('{')[ 0]
            conds       = line.split('{')[-1].split('}')[0].split(',')[:-1]
            conds_split = []
            
            for cond in conds:
                cond_part = cond.split('<')[0] if '<' in cond else cond.split('>')[0]
                cond_cond = '<' if '<' in cond else '>'
                cond_numb = cond.split('<')[-1].split(':')[ 0] if '<' in cond else cond.split('>')[-1].split(':')[ 0]
                cond_land = cond.split('<')[-1].split(':')[-1] if '<' in cond else cond.split('>')[-1].split(':')[-1]
                #print(cond_part, cond_cond, cond_numb, cond_land)
                conds_split.append((cond_part, cond_cond, cond_numb, cond_land))
            
            final                    = line.split('{')[-1].split('}')[0].split(',')[-1]
            instructions_conds[part] = conds_split
            instructions_final[part] = final
        else:
            rating = {}
            vals   = line[1:-1].split(',')
            for val in vals: rating[val.split('=')[0]] = val.split('=')[-1]
            ratings.append(rating)
            
        if line == '':
            firstPart = not firstPart
            
instructions_conds = {k:v for k,v in instructions_conds.items() if k != ''}
instructions_final = {k:v for k,v in instructions_final.items() if k != ''}

# Part 1

def sort_rating(rating: dict, instruction: str) -> str:
    
    instruction_conds = instructions_conds[instruction]
    instruction_final = instructions_final[instruction]
    
    for cond in instruction_conds:
        if cond[1] == '<':
            if int(rating[cond[0]]) < int(cond[2]):
                return cond[3] if cond[3] in ['A', 'R'] else sort_rating(rating, cond[3])
        elif cond[1] == '>':
            if int(rating[cond[0]]) > int(cond[2]):
                return cond[3] if cond[3] in ['A', 'R'] else sort_rating(rating, cond[3])
    
    return instruction_final if instruction_final in ['A', 'R'] else sort_rating(rating, instruction_final)
    
scores = []

for rating in ratings:
    res = sort_rating(rating, 'in')
    if res == 'A':
        score = sum([int(v) for v in rating.values()])
        scores.append(score)
        
print(sum(scores))