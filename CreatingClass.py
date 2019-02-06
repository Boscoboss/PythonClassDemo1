class Vehicle:
    RegNo="TN45BB6484"
    Wheels=2
    Litres=4
  
def main():
   v1= Vehicle()
   print(v1.Litres)
   print(v1.Wheels)
   v1.Wheels=4
   print(v1.Wheels)

if __name__=='__main__':main()