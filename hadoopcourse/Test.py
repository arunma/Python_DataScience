movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

xs = [i + 0.1 for i, _ in enumerate(movies)]

print (xs)

print 15.0 / 100

print 15.0 // 100

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10

print [decile(grade) for grade in grades]

import numpy

print numpy.random.random(100)