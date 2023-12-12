# Part One

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_4.txt"

wins = []

with open(input_file, "r") as f:
    for line in f:
        score   = 0
        numbers = line.replace('\n','').split(':')[1]
        
        winning_numbers   = sorted([int(n) for n in re.findall('\d+', numbers.split('|')[0])])
        scratched_numbers = sorted([int(n) for n in re.findall('\d+', numbers.split('|')[1])])
        
        actual_wins = set(winning_numbers).intersection(set(scratched_numbers))
        num_of_wins = len(actual_wins)
        
        if num_of_wins > 0:
            score = 2 ** (num_of_wins - 1)
            wins.append(score)
            #print(winning_numbers, scratched_numbers, actual_wins, num_of_wins, score)
            
        #print(numbers, '==>', score)
            
result = sum(wins)
print('Score:', result)