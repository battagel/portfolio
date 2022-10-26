import random

# This is the code to calculate an estimate of pi when given a UNIFORM random number generator between 0 and 1

# This works by using the random numbers given to plot many points on a graph. The result will form a 
# square where next you can plot a unit circle and count up the number of points in the circle vs the 
# total number of points

def calc_pi(p):
    # Initialise variables
    in_circle = 0

    for _ in range(p):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            in_circle += 1

    # The return value is pi because the area of pi (pi*r^2) divided by the area of the square ((2*r)*2) can be used to give: pi = 4 * in_circle / p
    return 4 * in_circle/p

