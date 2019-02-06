using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EncapsulationDemo1
{
    class Program
    {
        static void Main(string[] args)
        {
            Vehicle v1 = new Vehicle();
            Console.WriteLine("Enter Your Registration Number: ");
            v1.RegNo = Console.ReadLine();
            Console.WriteLine("Entert the number of Wheels: ");
            v1.NoOfWheels = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Entert the number of Litres: ");
            v1.NoOfLitres = Convert.ToInt32(Console.ReadLine());

            //Calculate Bill
            v1.CalculateBill();

            //Print Bill
            Console.WriteLine(v1.PrintBillDetails());
        }
    }

    class Vehicle
    {
        public static int costperlitre=50;
        public static int costperwheel=5;
        public static int minWheels=1;
        public static int maxWheels=20;
        public static int minLitres=1;
        public static int maxLitres=100;

        string _regNo;

        public string RegNo
        {
            get { return _regNo; }
            set { _regNo = value; }
        }
        int _noOfLitres;

        public int NoOfLitres
        {
            get { return _noOfLitres; }
            set {
                if (value >= minLitres && value <= maxLitres)
                {
                    _noOfLitres = value;
                }
            }
        }
        int _noOfWheels;

        public int NoOfWheels
        {
            get { return _noOfWheels; }
            set
            {
                if (value >= minWheels && value <= maxWheels)
                {
                    _noOfWheels = value;
                }
            }
        }

        int _totalCost;

        public int TotalCost
        {
          get { return _totalCost; }
          set { _totalCost = value; }
        }


        private int FillFuel() 
        {
            int temp = costperlitre * NoOfLitres;
            return temp;
        }

        private int FillAir()
        {
            int temp = costperwheel * NoOfWheels;
            return temp;
        }

        public void CalculateBill()
        {
            int costForAir = FillAir();
            int costForFuel = FillFuel();
            _totalCost = costForAir + costForFuel;
            
        }

        public string PrintBillDetails() 
        {
            string message = string.Format("Total amount to be paid by {0} is Rs.{1}", this.RegNo, this.TotalCost);
            return message;
        }



    }
}
