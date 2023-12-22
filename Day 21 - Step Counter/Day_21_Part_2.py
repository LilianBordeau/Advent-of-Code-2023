# Part 2 // Create increased worldmap size to compute further

extraworldmap = []

for i in range(len(worldmap * 5)):
    #print(i, i % len(worldmap))
    line = worldmap[i % len(worldmap)] * 5
    #print(len(line))
    extraworldmap.append(line)
    
print(len(extraworldmap), len(extraworldmap[0]))


# Part 2 // Quadratic fit 

points = [(i, results[(65 + (i * len(worldmap)) - 1)]) for i in range(3)]

def evaluate_quadratic_equation(points, x):
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result       = np.polyval(coefficients, x)
    return round(result)

def predict(x):
    return (14861 * x * x) + (14994 * x) + 3791

evaluate_quadratic_equation(points, 202300)