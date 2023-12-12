# Part One

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_2.txt"

game_ids     = []

R_constraint = 12
G_constraint = 13
B_constraint = 14

with open(input_file, "r") as f:
    for line in f:
        l1 = line.replace('\n','')
        
        game_id   = int(re.findall('Game (\d+):', l1)[0])
        
        # red (R)
        all_red   = re.findall('(\d+) red', l1)
        max_red   = max([int(n) for n in all_red])
        
        # green (G)
        all_green = re.findall('(\d+) green', l1)
        max_green = max([int(n) for n in all_green])
        
        # blue (B)
        all_blue  = re.findall('(\d+) blue', l1)
        max_blue  = max([int(n) for n in all_blue])
        
        #print(l1)
        #print(game_id, ':', max_red, max_green, max_blue)
        
        if max_red <= R_constraint and max_green <= G_constraint and max_blue <= B_constraint:
            #print(game_id, ':', max_red, max_green, max_blue)
            #game_ids.append(game_id)
            pass
            
        power_set = max_red * max_green * max_blue
        game_ids.append(power_set)
        
        #sets = l1.split(':')[1].split(';')
        
sum(game_ids)