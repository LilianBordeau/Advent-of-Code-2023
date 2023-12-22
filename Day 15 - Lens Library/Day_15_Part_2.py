hashmap = {}

for i in range(256):
    hashmap[i] = []

for string in strings:
    
    if '-' in string:
        label = string.split('-')[0]
        boxnb = get_hash_from_string(label)
        hashmap[boxnb] = [(l,f) for l,f in hashmap[boxnb] if l != label]
        #if label in hashmap[boxnb]:
    
    if '=' in string:
        label = string.split('=')[0]
        focal = int(string.split('=')[-1])
        boxnb = get_hash_from_string(label)
        
        is_in = any([True if l == label else False for l,f in hashmap[boxnb]])
        
        if is_in:
            hashmap[boxnb] = [(label, focal) if l == label else (l,f) for l,f in hashmap[boxnb]]
        else:
            hashmap[boxnb].append((label,focal))

hashmap = {k:v for k,v in hashmap.items() if len(v) > 0}
score   = sum([sum([(k + 1) * (i + 1) * f for i, (l,f) in enumerate(v)]) for k,v in hashmap.items()])
print(score)