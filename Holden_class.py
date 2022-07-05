
# Build the following class
# make e.g. Holden
# model e.g. Commodore
# rego e.g ABC123
# MaxRange e.g. 600 . the distance the car can go when it is full of either fuel or electricity
# range e.g. 200 the distance the car is currently able to travel without refuel / recharging
# Car: constructor, takes and assigns make, model, rego, max raange 
#       * when created in the constructor, the car is created with a range equal to the maxrange
# GetDetails(): returns a string of the cars make, model and rego (in a single line)
# Travel(int). e.g Travel(50).  reduces the cars current range by the number of km's travelled.
# GetRange(). prints to screen "Current Range is  XX kms"

class Car:
    def __init__(self, make, model, rego, MaxRange): #, MaxRange, range
        self.make = make
        self.model = model
        self.rego = rego
        self.MaxRange = MaxRange
        self.Range = MaxRange

    def GetDetails(self): 
        #returns a string of the cars make, model and rego (in a single line)
        details = (self.make, self.model, self.rego)
        return details

    def Travel(self, kilometers):
        self.Range -= kilometers

    def GetRange(self):
        return print("Current Range is", self.Range)

mycar = Car("Holden", "Commodore", "ABC123", 600)
mycar.GetDetails()
mycar.Travel(50) #50 is input of kms travelled, it can change
mycar.GetRange()