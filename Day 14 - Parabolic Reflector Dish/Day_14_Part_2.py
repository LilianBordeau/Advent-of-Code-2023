@cache
def cycle_rolls_matrice(matrice, nb_cycle = 1):
    
    for i in range(nb_cycle):
    
        # North
        matrice = rotate_matrice_clockwise(matrice)
        matrice = let_rocks_roll(matrice)

        # West
        matrice = rotate_matrice_clockwise(matrice)
        matrice = let_rocks_roll(matrice)

        # South
        matrice = rotate_matrice_clockwise(matrice)
        matrice = let_rocks_roll(matrice)

        # Est
        matrice = rotate_matrice_clockwise(matrice)
        matrice = let_rocks_roll(matrice)
    
    return tuple(tuple(row) for row in matrice)


%%time

scores = []

for i in range(10000):
    r_platform = cycle_rolls_matrice(r_platform, 1)
    score      = get_score_from_rocks(r_platform)
    scores.append(score)