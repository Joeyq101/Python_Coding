
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
        return print(details)

    def Travel(self, kilometers):
        self.range -= kilometers

    def GetRange(self):
        return print("Current Range is", self.Range)

class PetrolCar(Car):
    def __init__(self, make, model, rego, MaxRange, fuelType): #for line 39 when asking for petrol car info
        super().__init__(make, model, rego, MaxRange) #gives instructions to parent class, super(). means parent = car
        self.fuelType = fuelType  

    def Refuel(self):
        self.range = self.MaxRange
        return print("After refuelling, you have increased your range to",self.range, "kms")

class ElectricCar(Car):
    def __init__(self, make, model, rego, MaxRange): #for line 39 when asking for petrol car info
        super().__init__(make, model, rego, MaxRange) #gives instructions to parent class, super(). means parent = car

    def Recharge(self):
        self.range = self.MaxRange
        return print("After recharging, you have increased your range to",self.range, "kms")

dieselCar = PetrolCar("Deisel", "Holden", "Commodore", "ABC123", 600, "Petrol")
dieselCar.GetDetails()
dieselCar.Travel(50)
dieselCar.GetRange()
dieselCar.Refuel()

elecCar = ElectricCar("Tesla", "Sports", "117AA7", 700)
elecCar.GetDetails()
elecCar.Travel(50)
elecCar.GetRange()
elecCar.Recharge()
