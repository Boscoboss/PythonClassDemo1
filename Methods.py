class Vehicle:
#Constructor
    def __init__(self, **kwargs):
        self._regNo=kwargs['regNo'] if 'regNo' in kwargs else 'TN45AA0000'
        self._litres=kwargs['litres'] if 'litres' in kwargs else 2
        self._wheels=kwargs['wheels'] if 'wheels' in kwargs else 2
        
#Properties
    def regNo(self, r= None):
        if r: self._regNo=r
        return self._regNo

    def litres(self, l=None):
        if l: self._litres=l 
        return self._litres

    def wheels(self, w=None):
        if w: self._wheels=w
        return self._wheels

#Methods
    def FillAir(self):
        print(self._wheels*5)
    
    def FillFuel(self):
        print(self._litres*50)
    
    def PrintMe(self):
        print("Just a simple utility function")

#Utility Functions
def PrintVehicle(o):
    if not isinstance(o,Vehicle):
        print("Argument not of type Vehicle")
    else:
        print("{0} has filled air for {1} wheels and filled {2} litres of fuel".format(o.regNo(),o.wheels(),o.litres()))

def main():
    v1= Vehicle(regNo="TN45BB7084", litres=4, wheels=2)
    PrintVehicle(v1)
    v1.FillAir()
    v1.FillFuel()
    v1.litres(6)
    v1.wheels(4)
    PrintVehicle(v1)
    v1.FillAir()
    v1.FillFuel()
    v1.PrintMe()
 

    

if __name__ == "__main__": main()