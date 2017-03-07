from collections import Counter
from matplotlib import pyplot as plt

grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile= lambda grade:(grade // 10 ) *10

histogram=Counter(decile(grade) for grade in grades) #Counter({80: 4, 70: 3, 0: 2, 90: 2, 100: 1, 60: 1})

print histogram


print [x-4 for x in histogram.keys()]

plt.bar([x-4 for x in histogram.keys()], histogram.values(),8) #left, height, width

plt.axis([-5,105,0,5]) # x axis from -5 to 105 and y axis from 0 to 5

plt.xticks([10*i for i in range (11)])

plt.xlabel("Decile")

plt.ylabel("# of Students")

plt.title("Distribution of Exam 1 Grades")

plt.show()