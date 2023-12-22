# Get data

input_file = "input_day_15.txt"

strings = []

with open(input_file, "r") as f:
    for line in f:
        line  = line.replace('\n', '')
        strings = line.split(',')

def get_hash_from_string(string: str):
    current_val = 0
    
    for c in string:
        current_val += ord(c)
        current_val *= 17
        current_val %= 256
        
    return current_val

hashes = []

for string in strings:
    hashed = get_hash_from_string(string)
    hashes.append(hashed)
    
print(sum(hashes))