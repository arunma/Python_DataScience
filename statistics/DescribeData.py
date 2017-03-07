from __future__ import division
import random


random.seed(10)
num_friends=[random.randrange(10, 1000) for _ in range(10)]

print num_friends

print len(num_friends)

largest_value=max(num_friends)

smallest_value=min(num_friends)

sorted_values=sorted(num_friends)

print ("largest value", largest_value, "smallest value", smallest_value)

print ("Sorted values ", sorted_values)

#Central tendencies

def mean (x):
    return sum(x)/len(x)

print mean (num_friends)


def median(v):
    n=len(v)
    sorted_values=sorted(v)
    midpoint=n //2

    if n%2==1:
        return sorted_values[midpoint]
    else:
        lo=midpoint-1
        hi=midpoint
        return (sorted_values[lo]+sorted_values[hi])/2

print median(num_friends)

def quantile(xs, p):
    index=int(len(xs) * p)
    print (index)
    return sorted(xs)[index]

print quantile(num_friends, 0.10)
print quantile(num_friends, 0.25)
print quantile(num_friends, 0.50)
print quantile(num_friends, 0.75)
print quantile(num_friends, 0.90)


from collections import Counter

def mode(xs):
    """returns a list, might be more than one mode"""
    counts=Counter(xs)
    max_count=max(counts.values())
    return [xi for xi, count in counts.iteritems() if count==max_count]

print ("Mode", mode(num_friends))


def data_range(xs):
    return max(xs)-min(xs)

print data_range(num_friends)

def dot(v, w):
    dot=sum(vi * wi for vi, wi in zip(v, w))
    return dot

def sum_of_squares(xs):
    return dot (xs, xs)

def deviations_mean(xs):
    x_bar=mean(xs)
    return [xi-x_bar for xi in xs]

#Variance
def variance (xs):
    deviations=deviations_mean(xs)
    return sum_of_squares(deviations)/(len(xs)-1) #unbiased

#Khan academy https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/sample-standard-deviation/e/variance
gorilla_ages=[8,4,14,16,8]
#print ("variance", variance(gorilla_ages))

bear_ages=[5,4,6,39]

import math

def standard_deviation(xs):
    return math.sqrt(variance(xs))

#print ("standard deviation gorillas ", standard_deviation(gorilla_ages))
#print ("variance for bears", variance(bear_ages))
#print ("standard deviation bears", standard_deviation(bear_ages))

#lion_ages=[13,2,1,5,2,7]
#print ("Variance of lions", variance(lion_ages))

#lizards_ages=[1,2,2,1,3,3]
#print ("Variance of lizards", variance(lizards_ages))

#zebra_ages=[5,4,6,39]

#print ("variance of zebras", variance(zebra_ages))

sd_data=[13,2,1,5,2,7]

print ("standard deviation", standard_deviation(sd_data))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print ("inter quartile range", interquartile_range(sd_data))

def covariance(x,y):
    n=len(x)
    xdev=deviations_mean(x)
    ydev=deviations_mean(y)
    print ("XDeviations", xdev, "YDeviations", ydev)
    print ("Dot", dot(xdev,ydev))
    return dot(xdev, ydev) / (n-1)

print ("covariance, ",covariance([1,2,3],[2,4,6]))

def correlation(x,y):
    stdevx=standard_deviation(x)
    stdevy=standard_deviation(y)
    print ("Stddev x", stdevx, "Stddev y", stdevy)
    if stdevx >0 and stdevy>0:
        return covariance(x,y)/(stdevx*stdevy)
    else:
        return 0

print ("correlation, ",correlation([1,2,3],[2,4,6]))