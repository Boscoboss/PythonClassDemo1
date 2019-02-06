class Vehicle:
    def __init__(self, **kwargs):
        self._regNo=kwargs['regNo']
        self._litres=kwargs['litres']
        self._wheels=kwargs['wheels']
        

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
    

if __name__ == "__main__": main()