class Dog():
#CLASS OBJECT ATTRIBUTE
#SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"


    def __init__(self,breed1,bite,name):
        self.breed = breed1
        self.bite = bite
        self.name = name
    def bark(self,number):
        print(f"Woof!!! My name is {self.name} and the number is {number}!")
my_dog = Dog("Lab","hard","sheru")
print(my_dog.breed,my_dog.bite,my_dog.name,my_dog.species)
my_dog.bark(12)


class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14
    def __init__(self,radius=1):
        self.radius = radius
    
    #Method
    def get_circumference(self):
        return self.radius * 2 * Circle.pi

my_circle = Circle(10)
print(my_circle.get_circumference())
my_circle2 = Circle(100)
print(my_circle2.get_circumference())