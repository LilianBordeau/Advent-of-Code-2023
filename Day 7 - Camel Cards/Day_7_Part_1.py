# Get data

input_file = "C:/Users/Lilian/Desktop/Advent of Code 2023/input_day_7.txt"

hands = {}

with open(input_file, "r") as f:
    for line in f:
        hand = line[:5]
        bid  = int(line[6:-1])
        #print(hand,bid)
        hands[hand] = bid
        
labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

scores = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def get_hand_type(hand):
    
    counts = []
    
    for label in labels:
        count = hand.count(label)
        counts.append(count)
        
    counts = [c for c in sorted(counts, reverse=True) if c != 0]
    
    #print(counts)
    
    if counts[0] == 5:
        return 1 #'Five-of-a-kind'
    elif counts[0] == 4:
        return 2 #'Four-of-a-kind'
    elif counts[0] == 3 and counts[1] == 2:
        return 3 #'Full-house'
    elif counts[0] == 3 and counts[1] == 1 and counts[2] == 1:
        return 4 #'Three-of-a-kind'
    elif counts[0] == 2 and counts[1] == 2 and counts[2] == 1:
        return 5 #'Two-pair'
    elif counts[0] == 2 and counts[1] == 1 and counts[2] == 1 and counts[3] == 1:
        return 6 #'One-pair'
    else:
        return 7 #'High-card'
    
def compare_hands(hand1, hand2):
    
    ht1 = get_hand_type(hand1)
    ht2 = get_hand_type(hand2)
    
    #print(ht1, ht2)
    
    if ht1 < ht2:
    #    print('Type hand 1 > Type hand 2')
        return 1
    elif ht1 > ht2:
    #    print('Type hand 1 < Type hand 2')
        return 2
    else:
        for i in range(5):
            if scores[hand1[i]] > scores[hand2[i]]:
    #            print('Score hand 1 > Score hand 2')
                return 1
            elif scores[hand1[i]] < scores[hand2[i]]:
    #            print('Score hand 1 < Score hand 2')
                return 2
        
    #    print('Both hands equal')
        return 3
    
results = {k:[] for k in hands.keys()}
for hand1 in hands:
    #print(hand1, hand2)
    for hand2 in hands:
        res = compare_hands(hand1, hand2)
        results[hand1].append(res)
        
results_rank = {k:[] for k in hands.keys()}

for hand in hands.keys():
    results_rank[hand] = sum([1 if r == 1 else 0 for r in results[hand]]) + 1
    
results_rank = {k: v for k, v in sorted(results_rank.items(), key=lambda x: x[1])} 

scores = []

for hand, rank in results_rank.items():
    score = hands[hand] * rank
    scores.append(score)
    
sum(scores)