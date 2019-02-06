class Vehicle:
    def __init__(self, **kwargs):
        self._regNo=kwargs['regNo'] if 'regNo' in kwargs else 'TN45AA0000'
        self._litres=kwargs['litres'] if 'litres' in kwargs else 2
        self._wheels=kwargs['wheels'] if 'wheels' in kwargs else 2
        

    def regNo(self):
        return self._regNo

    def litres(self):
        return self._litres

    def wheels(self):
        return self._wheels

def PrintVehicle(o):
    if not isinstance(o,Vehicle):
        print("Argument not of type Vehicle")
    else:
        print("{0} has filled air for {1} wheels and filled {2} litres of fuel".format(o.regNo(),o.wheels(),o.litres()))

def main():
    v1= Vehicle(regNo="TN45BB7084", litres=4, wheels=2)
    PrintVehicle(v1)
    v2= Vehicle()
    PrintVehicle(v2)
   
    

if __name__ == "__main__": main()