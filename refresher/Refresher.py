#Function
def double(x):
    return x *2

print (double(2))

#Passing function as values
def applyfn(f):
    return f(5)


print (applyfn(double))
#Passing lambda as an argument
print (applyfn(lambda x: x*2))

#Exception
def exception_fn():
    try:
        print(0/0)
    except ZeroDivisionError:
        print("cannot divide by zero")

exception_fn()

#List
integer_list=[1,2,3]
hetero_list=["string", 0.1, True]
lists_of_lists=[integer_list, hetero_list]

list_sum=sum(integer_list)
print(list_sum)

x=range(10)
print(x)

print(x[0])
print(x[1:3])
print(x[:5])
print(x[5:7])

#Concat list
#integer_list.extend(x) #MUTATION
conc=integer_list + x
print(conc)

#Append
integer_list.append(100)
print(integer_list)

#Unpacking
x,y=range(2) #[0,1]
print("%s and %s" %(x,y))

#Skipping values during unpacking
_,z=[1,2]


#Tuples
tuple=(1,2)
#Cannot modify a tuple
try:
    tuple[1]=3
except TypeError:
    print("Cannot modify a tuple")

#Swap is crazy
x,y=y,x

#Dictionaries
empty_dict={}
empty_dict2=dict()
grades={"Arun":80, "Jason":90}
print(grades["Arun"])

#No key would result in a key error (whoaa!)
try:
    grades["Hello"]
except KeyError:
    print("No value for Hello")

#Python's get is getOrElse in Scala
print(grades.get("Hello",-1))

#Strange that the "default" value could be of any type
print(grades.get("Hello","NoStudentByThatName"))

#Mutation in a dictionary
grades["Arun"]=100
print(grades.get("Arun",0))

#Use dictionaries to represent structured data because they are heterogenous (??!!)
tweet={
    "user":"arunma",
    "text":"Programmer",
    "retweet_count":101,
    "hashtags":["#scala", "#python"]
}

print(tweet["user"])

#print(dir(tweet))
print("keys %s"%tweet.keys())
print("values %s"%tweet.values())
print("items %s"%tweet.items())

#defaultdict - fix default value for nonexistent keys
from collections import defaultdict
wordcounts=defaultdict(int) #value is a 0
document=["hello", "world","hello","danger"]
for word in document:
    wordcounts[word]+=1

#Other default dict parameter types
#list as defaultdict
dd_list=defaultdict(list)
dd_list[1].append(100)
print(dd_list) # {1:[100]}

dd_dict=defaultdict(dict) #Map as the type
dd_dict["Arun"]["City"]="Singapore"

print(dd_dict)

#Parameter is a lambda (woww. this is sweet)
dd_pair=defaultdict(lambda:[0,0])
dd_pair[1][1]=100 #{1:[0,100]}
print(dd_pair)



#Counter
from collections import Counter
c=Counter([0,1,3,0]) #Constucts a histogram of index to count (as entered)

#Word counts could be solved simply by doing a
word_counts_counter=Counter(document)

#most_common function
for word, count in word_counts_counter.most_common(4):
    print (word, count)

#Set

s=set()
s.add(1)

2 in s #False
print(1 in s)

li=[1,2,3,4,4,5]
#convert from list to set
print(set(li))
nset=set(li)

#convert from set to list
print(list(nset))

#if-elif-else

if (1>2):
    message="if only 1 were greater than two"
elif 1>3:
    message="elif stands for else if"
else:
    message="when all else fails use else"

#ternary

"even" if (x %2==0) else "odd"

#for loop
for x in range(10):
    print x, "is less than 10"

#continue statement
for x in range(10):
    if (x==3):
        continue
    if (x==5):
        break
    print(x)

#prints 0,1,2,4

#None==null in Java

x=None
print(x is None) #None check

print all([]) #???!!!

#Sorted vs sort function
in_sort=[1,42,5,34,2,23,4]
in_sort.sort()
print("insort", in_sort)

out_sort=[1,42,5,34,2,23,4]
out_sor_sorted=sorted(out_sort, reverse=True)
print("outsorted", out_sor_sorted)

#Sort key (Nice !!!!)
document1=["hello", "world","hello","danger", "bye","hello","world"]
for word in document1:
    wordcounts[word]+=1

print(wordcounts)

ordered_wc=sorted(wordcounts.items(), key=lambda (word, count): count, reverse=True)

print("Reverse ordered word count: ", ordered_wc)

#List comprehensions

#map
squares_set={x*x for x in integer_list} #returns a set
print ("squares :", squares_set)

squares_list=[x*x for x in integer_list] #returns a list
print ("squares list, ", squares_list)

#map and filter
squares_if_less_than_100={x*x for x in integer_list if x <100}
print ("squares less than 100", squares_if_less_than_100)

#convert list to dictionary
square_dic={x:x*x for x in integer_list}
print ("square dic", square_dic)

increasing_pairs=[(x,y)
                  for x in range (10)
                  for y in range (x+1, 10)
                  ]
print("Increasing pairs", increasing_pairs)
