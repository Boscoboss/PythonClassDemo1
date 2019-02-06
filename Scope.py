class Vehicle:
 #mutable class variable   
    mutabletype=[1,2,3]
 #Immutable class variable
    rateperlitre=50
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
    v2= Vehicle(regNo="TN45BB7085", litres=4, wheels=2)
   
    print(v1.mutabletype)
    v2.mutabletype[0]=5
    print("****************")
    print(v1.mutabletype)
    print("****************")
    v1.mutabletype[1]=8
    print(v2.mutabletype)
    print("****************")
    print(v1.rateperlitre)
    Vehicle.rateperlitre=75
    print(v1.rateperlitre)
    print(v2.rateperlitre)
    print("****************")
    print(v1.rateperlitre)
    v1.rateperlitre=85
    print(v1.rateperlitre)
    print(v2.rateperlitre)
    print("****************")
    print(v1.rateperlitre)
    v2.rateperlitre=100
    print(v2.rateperlitre)
    print(v1.rateperlitre)


if __name__ == "__main__": main()