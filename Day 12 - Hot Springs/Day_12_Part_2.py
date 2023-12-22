@cache
def poss(springs, counts, hashes=0, require=None):

    if require == '#' and (springs == '' or springs[0] == '.'): return 0

    firstgrp = 0
    for i, char in enumerate(springs+'X'):
        if char != '#':
            firstgrp = i
            break

    if require == '.' and firstgrp:
        assert hashes == 0
        return 0

    if counts == ():
        if '#' in springs:
            return 0
        return 1

    tail = springs[firstgrp:]

    # If we start with some hashes
    if firstgrp != 0:
        if counts == ():
            return 0

        # The right amount
        if hashes+firstgrp == counts[0]:
            return poss(tail, counts[1:], hashes=0, require='.')

        # Not enough
        if hashes+firstgrp < counts[0]:
            a = poss(tail, counts, hashes=hashes+firstgrp, require='#')
            return a

        # Too many
        if hashes+firstgrp > counts[0]:
            return 0

    if springs == '':
        assert counts != ()
        return 0

    head, tail = springs[0], springs[1:]

    # If we start with dot
    if head == '.':
        return poss(tail, counts)

    # With qmark
    if head == '?':
        a = poss('#'+tail, counts, hashes=hashes, require=require)
        b = poss('.'+tail, counts, hashes=hashes, require=require)
        return a + b

extended_springs = []

for encoded_string, arrangements in springs:
    new_encoded_string = ((encoded_string + '?') * 5)[:-1]
    new_arrangements   = arrangements * 5
    
    extended_springs.append((new_encoded_string, new_arrangements))
    
possibles = []

for encoded_string, arrangements in extended_springs:
    nb =  poss(encoded_string, tuple(arrangements))
    possibles.append(nb)
    
print(sum(possibles))