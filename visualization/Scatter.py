from matplotlib import pyplot as plt
import string

friends=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]

labels=[x for x in string.ascii_lowercase[0:9]]

print (labels)

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip (labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5,-5),
                 textcoords='offset points'
                 )
plt.title("Daily minutes vs Number of friends")
plt.xlabel("Number of friends")
plt.ylabel("Daily minutes spent on the site")



plt.show()