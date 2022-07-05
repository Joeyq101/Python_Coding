# a person class
class Person: #init is a constructor
    def __init__(self, name, age): 
        print("Hey! I'm in the __init__")
        self.name = name
        self.age = age

    def calcYOB(self): # Operation to calculate year of birth
        return 2022 - self.age

j1 = Person("Jan", 21)
m1= Person("Mary", 51)

print(j1.name)
print(m1.age)
print("Year of birth: ", m1.calcYOB())