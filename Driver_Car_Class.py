

    
class Driver:
    def __init__(self, name, licenceNo):
        self.name = name
        self.licenceNo = licenceNo
    
    def GetDetails(self):
        return print(self.name, "is my driver")

class Car:
    def __init__(self, make, model, rego, MaxRange, Driver):
        self.make = make
        self.model = model
        self.rego = rego
        self.MaxRange = MaxRange
        self.range = MaxRange
        self.Driver = Driver

    def GetDetails(self): 
        details = (self.make, self.model, self.rego)
        return details

    def Travel(self, kilometers):
        self.range -= kilometers

    def GetRange(self):
        return print("Current Range is", self.range)

#    def ChangeDriver(self, Driver):
#        self.Driver = Driver
#        return print(Driver, "is my new driver")

myDriver = Driver("Joanna", 12345678)
myDriver.GetDetails()

myCar = Car("Holden", "Commodore", "ABC123", 600, myDriver)
myCar.GetDetails()
myCar.Travel(50)
myCar.GetRange()
#myCar.ChangeDriver("Harry")

print(myCar.Driver.licenceNo) #only prints licenceNo





