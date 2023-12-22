# Part 2

RANGE_MIN, RANGE_MAX =  1, 4000

BINF_OK, BINF_KO     = -1,  0
BSUP_OK, BSUP_KO     =  1,  0

RANGES = {'x': [RANGE_MIN,RANGE_MAX], 
          'm': [RANGE_MIN,RANGE_MAX], 
          'a': [RANGE_MIN,RANGE_MAX], 
          's': [RANGE_MIN,RANGE_MAX]}

def explore_rating_range(rating: dict, instruction: str, results: list) -> None:

    if instruction in ['A', 'R']:
        results.append((rating, instruction))
        return
    
    instruction_conds = instructions_conds[instruction]
    instruction_final = instructions_final[instruction]
    
    for cond in instruction_conds:
        
        new_rating_ok = {k: v[:] for k, v in rating.items()}
        new_rating_ko = {k: v[:] for k, v in rating.items()}
        
        if cond[1]   == '<':
            new_rating_ok[cond[0]][1] = int(cond[2]) + BINF_OK
            new_rating_ko[cond[0]][0] = int(cond[2]) + BINF_KO
        elif cond[1] == '>':
            new_rating_ok[cond[0]][0] = int(cond[2]) + BSUP_OK
            new_rating_ko[cond[0]][1] = int(cond[2]) + BSUP_KO
            
        explore_rating_range(new_rating_ok, cond[3], results)
        rating = {k: v[:] for k, v in new_rating_ko.items()}
    
    if instruction_final in ['A', 'R']:
        results.append((rating, instruction_final))
    else:
        explore_rating_range(rating, instruction_final, results)

results = []
explore_rating_range(RANGES, 'in', results)
results = [res for res in results if res[1] == 'A']
scores  = [reduce(operator.mul, [r[1] - r[0] + 1 for r in list(res[0].values())], 1) for res in results]
score   = sum(scores)
print(score)