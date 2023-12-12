# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_9.txt"

sensors = []

with open(input_file, "r") as f:
    for line in f:
        numbers = [int(n) for n in re.findall('-*\d+',line)]
        sensors.append(numbers)
        
def get_liste_differences(liste):
    return [j-i for i, j in zip(liste[:-1], liste[1:])]

def get_liste_sequences(liste):
    level        = 1
    sequences    = {}
    sequences[0] = liste

    while not all([v == 0 for v in liste]):
        liste = get_liste_differences(liste)
        sequences[level] = liste
        level += 1
        
    return sequences, level

def extrapolate_forward_from_sequences(sequences):
    
    n_sequences = sequences.copy()
    
    last_val = 0

    for lvl in reversed(range(len(n_sequences)-1)):
        new_val   = n_sequences[lvl][-1] + last_val
        n_sequences[lvl].append(new_val)
        last_val = new_val
        
    return n_sequences

def process_sensor_history_forward(history):
    
    sequences, level    = get_liste_sequences(history)
    
    #print(level)
    
    extrapolates = extrapolate_forward_from_sequences(sequences)
    
    return extrapolates[0]

# Part 1

new_sensors = []

for history in sensors:
    new_history = process_sensor_history_forward(history)
    new_sensors.append(new_history)
    
sum([history[-1] for history in new_sensors])