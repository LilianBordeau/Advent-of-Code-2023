# Part One

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_5.txt"

wins  = {}

seeds = []

seeds_to_soil           = []
soil_to_fertilizer      = []
fertilizer_to_water     = []
water_to_light          = []
light_to_temperature    = []
temperature_to_humidity = []
humidity_to_location    = []

status = 'init'

with open(input_file, "r") as f:
    for line in f:
        
        #print(line)
        
        if 'seeds' in line:
            seeds = re.findall('\d+', line)
            seeds = [int(n) for n in seeds]
            #seeds = sorted([int(n) for n in seeds])
            continue
            
        elif 'seed-to-soil map'            in line: status = 'seed-to-soil map'
        elif 'soil-to-fertilizer map'      in line: status = 'soil-to-fertilizer map'
        elif 'fertilizer-to-water map'     in line: status = 'fertilizer-to-water map'
        elif 'water-to-light map'          in line: status = 'water-to-light map'
        elif 'light-to-temperature map'    in line: status = 'light-to-temperature map'
        elif 'temperature-to-humidity map' in line: status = 'temperature-to-humidity map'
        elif 'humidity-to-location map'    in line: status = 'humidity-to-location map'
        
        values = re.findall('\d+', line)
        
        if len(values) > 0:
        
            values = tuple([int(n) for n in values])
            #print(values)
        
            if   status == 'seed-to-soil map':
                seeds_to_soil.append(values)
            elif status == 'soil-to-fertilizer map':
                soil_to_fertilizer.append(values)
            elif status == 'fertilizer-to-water map':
                fertilizer_to_water.append(values)
            elif status == 'water-to-light map':
                water_to_light.append(values)
            elif status == 'light-to-temperature map':
                light_to_temperature.append(values)
            elif status == 'temperature-to-humidity map':
                temperature_to_humidity.append(values)
            elif status == 'humidity-to-location map':
                humidity_to_location.append(values)
                
mapping = {
    'seed-to-soil'           : seeds_to_soil,
    'soil-to-fertilizer'     : soil_to_fertilizer,
    'fertilizer-to-water'    : fertilizer_to_water,
    'water-to-light'         : water_to_light,
    'light-to-temperature'   : light_to_temperature,
    'temperature-to-humidity': temperature_to_humidity,
    'humidity-to-location'   : humidity_to_location
}

results = {}

for seed in seeds:
    
    source = seed
    
    print(seed, end = ' ')
    
    for map_type, maps in mapping.items():

        #print(map_type)

        found       = False
        destination = source

        for ranges in maps:

            range_dst_min = ranges[0]
            range_dst_max = ranges[0] + ranges[2]
            range_src_min = ranges[1]
            range_src_max = ranges[1] + ranges[2]

            #print(ranges)

            #print('Range source:', range_src_min, range_src_max)
            #print('Range destination:', range_dst_min, range_dst_max)

            if source >= range_src_min and source <= range_src_max:
                destination = range_dst_min + (source - range_src_min)
                #print(ranges, '==> OK ==> ', destination)
                found       = True
                break
        
        source = destination
        print('==>', destination, found, end = ' ')
        
    results[seed] = destination
    print()
    
result = min(list(results.values()))
print('Minimum destination found:', result)

def find_minimum_location(seed):
    
    source = seed
    
    #print(seed, end = ' ')
    
    for map_type, maps in mapping.items():

        #print(map_type)

        found       = False
        destination = source

        for ranges in maps:

            range_dst_min = ranges[0]
            range_dst_max = ranges[0] + ranges[2]
            range_src_min = ranges[1]
            range_src_max = ranges[1] + ranges[2]

            if source >= range_src_min and source <= range_src_max:
                destination = range_dst_min + (source - range_src_min)
                found       = True
                break
        
        source = destination
        
    return destination

def find_seed_from_location(location):
    
    destination = location

    for map_type, maps in reversed(mapping.items()):
        #print(map_type)

        found  = False
        source = destination

        for ranges in maps:

            range_dst_min = ranges[0]
            range_dst_max = ranges[0] + ranges[2]
            range_src_min = ranges[1]
            range_src_max = ranges[1] + ranges[2]

            if destination >= range_dst_min and destination <= range_dst_max:
                source = range_src_min + (destination - range_dst_min)
                found  = True
                break

        destination = source
        
    return source

for location in range(31599214, 31599215):
    seed = find_seed_from_location(location)
    
    found = False
    state = 'FAILURE'
    
    for start_seed_range, lenght_seed_range in zip(seeds[0::2], seeds[1::2]):
    
        r_seed_min = start_seed_range
        r_seed_max = start_seed_range + lenght_seed_range
        
        if r_seed_min <= seed <= r_seed_max:
            print('SUCCESS:', location, seed, '==>', r_seed_min, r_seed_max)
            state = 'SUCCESS'
            found = True
            break
        #else:
        #    print('FAILURE')
            
    #print(seed, location, state)