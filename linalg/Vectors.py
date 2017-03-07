from __future__ import division
def vector_add(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


def vector_subtract(v, w):
    return [vi - wi for vi, wi in zip(v, w)]


def vector_sum(vectors):
    result = vectors[0]
    for vect in vectors[1:]:
        result = vector_add(result, vect)
    return result


def vector_sum_fp(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(s, vector):
    return [s * vi for vi in vector]

def vector_mean(vectors):
    n=len(vectors)
    #import future division
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
    #vi_1*wi_1 + vi_2*wi*2...
    return sum (vi*wi for vi, wi in zip (v,w))

def sum_of_squares(v):
    return dot(v,v)

import math

def magnitude(v): #Length
    return math.sqrt(sum_of_squares(v))

#squared distance
def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

def distance_comb(v,w):
    return magnitude(vector_subtract(v,w))

print ("Vector addition ", vector_add([1, 2], [3, 4]))

print ("Vector subtraction ", vector_subtract([1, 2], [4, 8]))

print ("Vector sum ", vector_sum([[1, 2], [3, 4], [5, 6]]))

print ("Vector sum fp ", vector_sum_fp([[1, 2], [3, 4], [5, 6]]))

print ("Vector-Scalar multiply ", scalar_multiply(10, [3, 4]))

print ("Vector mean ", vector_mean([[1, 2], [3, 4], [5, 6]]))

print ("Vector dot product ", dot([1,2],[3,4]))

print ("Sum of squares ", sum_of_squares([2,3]))

print ("Magnitude", magnitude([2,3]))


print ("Squared distance ", squared_distance([1,2],[3,4]))

print ("distance between two vectors ", distance([1,2],[3,4]))



