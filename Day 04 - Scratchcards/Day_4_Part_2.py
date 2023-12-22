# Part Two

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_4.txt"

wins = {}

with open(input_file, "r") as f:
    for line in f:
        score   = 0
        
        #print(line)
        
        card_id = int(re.findall('Card *(\d+)', line)[0])
        
        numbers = line.replace('\n','').split(':')[1]
        
        winning_numbers   = sorted([int(n) for n in re.findall('\d+', numbers.split('|')[0])])
        scratched_numbers = sorted([int(n) for n in re.findall('\d+', numbers.split('|')[1])])
        
        actual_wins = set(winning_numbers).intersection(set(scratched_numbers))
        num_of_wins = len(actual_wins)
        
        wins[card_id] = num_of_wins

#store result
winning_streak = {}

for i in range(1, len(wins)+1):
    winning_streak[i] = 1
    
# compute
for carte, nb_de_cartes in winning_streak.items():
    
    #print(carte, nb_de_cartes, wins[carte])
    
    for _ in range(nb_de_cartes):
        for i in range(1, wins[carte]+1):
            winning_streak[carte+i] += 1
            
result = sum(list(winning_streak.values()))

print('Score:', result)