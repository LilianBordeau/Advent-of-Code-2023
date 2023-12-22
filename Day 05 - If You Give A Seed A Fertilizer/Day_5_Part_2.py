# Part Two

# 1
# seed        :         |____|
# source      :  |________|
# destination :                                |________|

# 2
# seed        :         |____________|
# source      :            |_______|
# destination :                                |________|

# 3
# seed        :         |_______|
# source      :           |_______|
# destination :                                |________|

# 4
# seed        :         |____|
# source      :      |_________|
# destination :                               |________|

# 5
# seed        :         |____|
# source      :  |____|
# destination :                                |________|

# 6
# seed        :         |____|
# source      :                |____|
# destination :                               |________|

results = {}

minimum_locations = []

#for start_seed_range, lenght_seed_range in [(2740196667, 3683286274)]:
for start_seed_range, lenght_seed_range in zip(seeds[0::2], seeds[1::2]):
    
    r_seed_min = start_seed_range
    r_seed_max = start_seed_range + lenght_seed_range
    
    src_ranges = [(r_seed_min, r_seed_max)]
    
    for map_type, maps in mapping.items():
        
        maps        = sorted(maps, key=lambda x: x[1])
        
        new_ranges  = []
        
        for (range_seed_min, range_seed_max) in src_ranges:

            intersect = False
            
            tmp_seed_min = 0
            tmp_seed_max = 0
            
            for ranges in maps:

                range_src_min = ranges[1]
                range_src_max = ranges[1] + ranges[2]

                range_dst_min = ranges[0]
                range_dst_max = ranges[0] + ranges[2]
                
                case      = 'not found'
                
                if   range_src_min <= range_seed_min <= range_src_max <= range_seed_max:
                    case = '1'
                    new_source_min = range_dst_max - (range_src_max - range_seed_min)
                    new_source_max = range_dst_max
                    new_ranges.append((new_source_min, new_source_max))
                    tmp_seed_min = range_dst_max
                    intersect = True
                elif range_seed_min <= range_src_min <= range_src_max <= range_seed_max:
                    case = '2'
                    new_source_min = range_dst_min
                    new_source_max = range_dst_max
                    new_ranges.append((new_source_min, new_source_max))
                    tmp_seed_min = range_dst_max
                    intersect = True
                elif range_seed_min <= range_src_min <= range_seed_max <= range_src_max:
                    case = '3'
                    new_source_min = range_dst_min
                    new_source_max = range_dst_min + (range_seed_max - range_src_min)
                    new_ranges.append((new_source_min, new_source_max))
                    intersect = True
                    #break
                elif range_src_min <= range_seed_min <= range_seed_max <= range_src_max:
                    case = '4'
                    new_source_min = range_dst_min + (range_seed_min - range_src_min)
                    new_source_max = range_dst_max - (range_src_max  - range_seed_max)
                    new_ranges.append((new_source_min, new_source_max))
                    intersect = True
                    #break
                                        
                #print('\t', range_seed_min, range_seed_max, '=>', range_src_min, range_src_max, case)
                last_case = case
                
            if not intersect:
                new_ranges.append((range_seed_min, range_seed_max))
                
        src_ranges = new_ranges
        #minimum_location = min([v[0] for v in src_ranges])
        #print(minimum_location)
    
    minimum_location = min([v[0] for v in src_ranges])
    minimum_locations.append(minimum_location)
    
    print('Minimum location of range ['+str(r_seed_min)+','+str(r_seed_max)+'] ==>', minimum_location)
    
result = min(minimum_locations)
print('Minimum destination found:', result)

# Adjusting the find_minimum_location function to handle potential empty lines or malformed data in mappings

def find_minimum_location_robust(seeds, mapping):
    results = {}

    for start_seed_range, length_seed_range in zip(seeds[0::2], seeds[1::2]):
        
        r_seed_min = start_seed_range
        r_seed_max = start_seed_range + length_seed_range
        
        src_ranges = [(r_seed_min, r_seed_max)]
        
        for map_type, maps in mapping.items():
            
            new_ranges = []
            
            for (range_seed_min, range_seed_max) in src_ranges:

                for ranges in maps:
                    # Skip any line that does not have exactly three elements
                    if len(ranges) != 3:
                        continue

                    range_dst_min, range_src_min, length = ranges
                    range_src_max = range_src_min + length
                    range_dst_max = range_dst_min + length

                    if range_src_min <= range_seed_min < range_src_max:
                        # Seed range starts within the source range
                        if range_seed_max <= range_src_max:
                            # Entire seed range is within the source range
                            new_source_min = range_dst_min + (range_seed_min - range_src_min)
                            new_source_max = new_source_min + (range_seed_max - range_seed_min)
                        else:
                            # Seed range extends beyond the source range
                            new_source_min = range_dst_min + (range_seed_min - range_src_min)
                            new_source_max = range_dst_max
                        new_ranges.append((new_source_min, new_source_max))
                    elif range_seed_min < range_src_min < range_seed_max:
                        # Source range starts within the seed range
                        if range_seed_max <= range_src_max:
                            # Source range ends within the seed range
                            new_source_min = range_dst_min
                            new_source_max = range_dst_min + (range_seed_max - range_src_min)
                        else:
                            # Source range extends beyond the seed range
                            new_source_min = range_dst_min
                            new_source_max = range_dst_max
                        new_ranges.append((new_source_min, new_source_max))

            if new_ranges:
                src_ranges = new_ranges
            else:
                # If no new ranges are added, it means that the seed range does not map to any source range
                # In this case, the seed number maps to itself
                src_ranges = [(range_seed_min, range_seed_max) for range_seed_min, range_seed_max in src_ranges]

        minimum_location = min([v[0] for v in src_ranges])
        
        results[(r_seed_min, r_seed_max)] = minimum_location
    
    result = min(list(results.values()))
    return result

# Find the minimum location with the new input data using the robust function
minimum_location_robust = find_minimum_location_robust(seeds, mapping)
minimum_location_robust