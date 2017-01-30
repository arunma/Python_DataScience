#Lazy ranges
def lazy_range(n):
    i=0
    while (i<n):
        yield i
        i+=1

for i in lazy_range(10):
    print (i)

print("Lazy range", lazy_range(10))

for x in xrange(10):
    print (x)

#Iter items in dictionary

grades={"Arun":80, "Jason":90}

for (key, value) in grades.iteritems():
    print (key, value)

#Check membership in a map
print "Arun" in grades

#Random numbers
import random
for x in range (10):
    print (random.random())

#OR - create a list out of it

print([random.random() for _ in range(10)])

#pseudo - set seed
random.seed(100)
print(random.random())
random.seed(100)
print(random.random())

#choose random within a range
print([random.randrange(0,5) for _ in range(10)])


#shuffle a list randomly
alist=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(alist)
print alist


favorites=["Jason","Arun","Daisy"]

print random.choice(favorites)

print [random.choice(favorites) for _ in range(10)]



