class Vehicle:
    rateperlitre=50
    rateperwheel=5
#Constructor
    def __init__(self, **kwargs):
        self._regNo=kwargs['regNo'] if 'regNo' in kwargs else 'TN45AA0000'
        self._litres=kwargs['litres'] if 'litres' in kwargs else 2
        self._wheels=kwargs['wheels'] if 'wheels' in kwargs else 2
        self._totalCost=kwargs['totalCost'] if 'totalCost' in kwargs else 0
        
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

    def totalCost(self, t=None):
        if t: self._totalCost=t
        return self._totalCost

#Methods
    def FillAir(self):
        return self._wheels*self.rateperwheel
    
    def FillFuel(self):
        return self._litres*self.rateperlitre
    
    def CalculateBill(self):
        temp= self.FillAir()+self.FillFuel()
        self.totalCost(temp)
    
    def PrintBillDetails(self):
        message= "Total cost to be paid by {0} is Rs.{1}".format(self.regNo(), self.totalCost())
        return message

#Utility Functions
def PrintVehicle(o):
    if not isinstance(o,Vehicle):
        print("Argument not of type Vehicle")
    else:
        print("{0} has filled air for {1} wheels and filled {2} litres of fuel".format(o.regNo(),o.wheels(),o.litres()))

def main():
    v1= Vehicle(regNo="TN45BB7084", litres=4, wheels=2)
    PrintVehicle(v1)
    v1.CalculateBill()
    print(v1.PrintBillDetails())
 
if __name__ == "__main__": main()