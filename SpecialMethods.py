class Vehicle:
    def __init__(self, **kwargs):
        self._regNo=kwargs['regNo'] if 'regNo' in kwargs else 'TN45AA0000'
        self._litres=kwargs['litres'] if 'litres' in kwargs else 2
        self._wheels=kwargs['wheels'] if 'wheels' in kwargs else 2
        

    def regNo(self, r= None):
        if r: self._regNo=r
        return self._regNo

    def litres(self, l=None):
        if l: self._litres=l 
        return self._litres

    def wheels(self, w=None):
        if w: self._wheels=w
        return self._wheels

#Special Methods
    def __str__(self):
        return "{0} has filled air for {1} wheels and filled {2} litres of fuel".format(self.regNo(),self.wheels(),self.litres())

#Documentation for Special Methods
#https://docs.python.org/3/reference/datamodel.html#special-method-names

def main():
    v1= Vehicle(regNo="TN45BB7084", litres=4, wheels=2)
    print(v1)
    v1.litres(6)
    print(v1)
    
if __name__ == "__main__": main()