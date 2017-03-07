import random
from linalg import Vectors

def step(vector, direction, step_size):
    return [v_i + step_size * direction_i for v_i, direction_i in zip (vector, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


v=[random.randint(-10, 10) for i in range(3)]

tolerance=0.000001

while True:
    gradient=sum_of_squares_gradient(v)
    next_v=step(v,gradient,-0.01)
    if (Vectors.distance(next_v,v))<tolerance:
        break
    v=next_v

print ("Final vector : ",v)



