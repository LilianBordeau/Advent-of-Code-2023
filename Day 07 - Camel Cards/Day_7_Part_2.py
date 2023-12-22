# Part 2

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

scores = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def get_hand_type(hand):
    
    counts = []
    
    for label in labels:
        count = hand.count(label)
        counts.append(count)
    
    nb_of_J   = counts[3]
    counts[3] = 0
    
    counts = [c for c in sorted(counts, reverse=True) if c != 0]
    
    #print(counts)
    
    if len(counts) == 0:
        return 1
    
    if   counts[0] + nb_of_J == 5:
        return 1 #'Five-of-a-kind'
    elif counts[0] + nb_of_J == 4:
        return 2 #'Four-of-a-kind'
    elif (counts[0] + nb_of_J == 3 and counts[1] == 2) or (counts[0] == 3 and counts[1] + nb_of_J == 2):
        return 3 #'Full-house'
    elif counts[0] + nb_of_J == 3 and counts[1] == 1 and counts[2] == 1:
        return 4 #'Three-of-a-kind'
    elif counts[0] + nb_of_J == 2 and counts[1] == 2 and counts[2] == 1:
        return 5 #'Two-pair'
    elif counts[0] + nb_of_J == 2 and counts[1] == 1 and counts[2] == 1 and counts[3] == 1:
        return 6 #'One-pair'
    else:
        return 7 #'High-card'