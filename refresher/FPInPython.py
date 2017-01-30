def exp(base, power):
    return base ** power

from functools import partial

two_to_the=partial(exp, power=2)

print two_to_the(5) #25

xs=[1,2,3,4,5]

def double(x):
    return x*2

print [double(x) for x in xs]
#is the same as
print map(double, xs)

list_doubler=partial(map, double)
print list_doubler(xs)

def multiply(x,y):
    return x*y

print map(multiply,[1,2],[4,5]) #[4, 10]

def is_even(x):
    return (x%2)==0

print filter(is_even, xs) # [2,4]

#Enumeration
documents=["Arun doc", "Jason doc", "Daisy doc"]

#enumerate spits out (index, element)

for i, document in enumerate(documents):
    print (i, document)

#Zipping

a=[1,2,3]
b=["Arun",'Jason','Daisy']

print zip (a,b)

for index,value in zip (a,b):
    print (index, value)

#Unpacking
#Pairs
pairs=zip (a,b)
indices,names=zip(*pairs)
print ("Indices", indices)
print ("Names", names)

print zip (*(zip(a,b))) #[(1, 2, 3), ('Arun', 'Jason', 'Daisy')]

#Splatting is *
def add (a,b):
    return a+b

add (1,2)
#add ([1,2]) #throws error
print add (*[3,4]) #7





