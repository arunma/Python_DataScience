class Animal (object):
    def __init__(self):
        print ("Animal created")

    def whoAmI(self):
        print ("Animal")

    def eat(self):
        print ("Eating")

class Dog(Animal):
    species="mammals"
    def __init__(self, breed):
        Animal.__init__(self)
        print ("dog created")
        self.breed=breed

    def whoAmI(self):
        print ("Dog")

    def bark(self):
        print ("Woof !")

sam=Dog(breed="Labrador")
frank=Dog (breed="Huskie")


print (sam.breed)

print (frank.breed)

print (sam.species)

Dog.species="dogs"
print (sam.species)

sam.species="man's best friend"
print (sam.species)


sam.bark()



## Book

class Book (object):
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title=title
        self.author=author
        self.pages=pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return "Title %s, author %s, pages %s" % (self.title, self.author, self.pages)

    def __del__(self):
        print ("A book is destroyed")

book=Book("Python is Awesome ", "Arun", 160)

print (book)

print (len (book))

del (book)
