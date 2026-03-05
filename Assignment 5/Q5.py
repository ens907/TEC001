import random

points = int(input("How many random points to generate? "))

inside_circle = 0

for i in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        inside_circle = inside_circle + 1

pi_approximation = 4 * inside_circle / points
print("Approximation of pi:", pi_approximation)
 