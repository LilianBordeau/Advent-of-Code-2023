# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_6.txt"

wins = []

with open(input_file, "r") as f:
    for line in f:
        print(line)
        if 'Time' in line:
            times     = [int(n) for n in re.findall('\d+', line)]
        if 'Distance' in line:
            distances = [int(n) for n in re.findall('\d+', line)]
            
print(times, distances)

# Part One

results = {}

for time, distance in zip(times,distances):
    #print(time, distance)

    distances_traveled = []

    for i in range(1, time):
    
        distance_traveled = i * (time - i)
        #print('\t', i, distance_traveled)
        
        if distance_traveled > distance:
            distances_traveled.append(distance)
    
    results[str(time)+'-'+str(distance)] = len(distances_traveled)
    
result = reduce(lambda x, y: x*y, list(results.values()))
result

