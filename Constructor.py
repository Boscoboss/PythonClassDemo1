class Vehicle:
    def __init__(self, regNo, litres, wheels):
        self._regNo=regNo
        self._litres=litres
        self._wheels=wheels

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
    v1= Vehicle("TN45BB7084", 4, 2)
    PrintVehicle(v1)
    

if __name__ == "__main__": main()