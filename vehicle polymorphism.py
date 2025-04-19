class koenigsegg:
    def MS(self):
        print("The Max Speed of Koenigsegg is 500 km/h.")
        
    def FT(self):
        print("The Fuel Type of Koenigsegg is Petrol.")
        
    def P(self):
        print("The Price of Koenigsegg is $5M.")
        
class toyotasupra:
    def MS(self):
        print("The Max Speed of Toyata Supra is 300 km/h")
        
    def FT(self):
        print("The Fuel Type of Toyota Supra is Petrol")
        
    def P(self):
        print("The Price of Toyata Supra is $150k")
        
class lamborghini:
    def MS(self):
        print("The Max Speed of Lamborghini is 350 km/h")
        
    def FT(self):
        print("The Fuel Type of Lamborghini is Petrol")
        
    def P(self):
        print("The Price of Lamborghini is $2M")
        
objK = koenigsegg()
objT = toyotasupra()
objL = lamborghini()

for vehicle in (objK, objT, objL):
    vehicle.MS()
    vehicle.FT()
    vehicle.P()
    print()