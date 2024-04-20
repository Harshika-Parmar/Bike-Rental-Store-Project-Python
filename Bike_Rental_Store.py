class Bike:
    def displayBikes(self):
        print("Name of Bike = NS 200,  Quantity = 10")
        print("Name of Bike = Duke 250,  Quantity = 12")
        print("Name of Bike = Bullet 200 Classic,  Quantity = 15")
        print("Name of Bike = Access 125,  Quantity = 20")
        print("Name of Bike = Ola Electric,  Quantity = 17")
    def placeOrder(self):
        amount=0
        Type_of_Bikes = int(input("Enter the Different Type of Bikes you require : "))
        Total_no_of_Bikes = int(input("Enter the Total Number of Bikes : "))
        for i in range(0,Type_of_Bikes):
            if Total_no_of_Bikes>0:
                Name_of_Bike = input("Enter the Name of Bike : ")
                Quantity = int(input("Enter the Quantity of Bike : "))
                Total_no_of_Bikes=Total_no_of_Bikes-Quantity
                if(Name_of_Bike=="NS 200"):
                    NS_qty=10
                    if Quantity<=0 or Quantity>NS_qty:
                        print("Insufficient Stock")
                    else:
                        basis = input("Enter Hourly/Daily/Weekly Basis : ")
                        num = int(input("Enter Number of Hours/Days/Weeks : "))
                        if basis=="Hourly":
                            amount1=5*num*Quantity
                        elif basis=="Daily":
                            amount1=20*num*Quantity
                        elif basis=="Weekly":
                            amount1=60*num*Quantity
                        else:
                            amount1=0
                    amount=amount + amount1
                elif(Name_of_Bike=="Duke 250"):
                    NS_qty=12
                    if Quantity<=0 or Quantity>NS_qty:
                        print("Insufficient Stock")
                    else:
                        basis = input("Enter Hourly/Daily/Weekly Basis : ")
                        num = int(input("Enter Number of Hours/Days/Weeks : "))
                        if basis=="Hourly":
                            amount2=5*num*Quantity
                        elif basis=="Daily":
                            amount2=20*num*Quantity
                        elif basis=="Weekly":
                            amount2=60*num*Quantity
                        else:
                            amount2=0
                    amount=amount + amount2
                elif(Name_of_Bike=="Bullet 200 Classic"):
                    NS_qty=15
                    if Quantity<=0 or Quantity>NS_qty:
                        print("Insufficient Stock")
                    else:
                        basis = input("Enter Hourly/Daily/Weekly Basis : ")
                        num = int(input("Enter Number of Hours/Days/Weeks : "))
                        if basis=="Hourly":
                            amount3=5*num*Quantity
                        elif basis=="Daily":
                            amount3=20*num*Quantity
                        elif basis=="Weekly":
                            amount3=60*num*Quantity
                        else:
                            amount3=0
                    amount=amount + amount3
                elif(Name_of_Bike=="Access 125"):
                    NS_qty=20
                    if Quantity<=0 or Quantity>NS_qty:
                        print("Insufficient Stock")
                    else:
                        basis = input("Enter Hourly/Daily/Weekly Basis : ")
                        num = int(input("Enter Number of Hours/Days/Weeks : "))
                        if basis=="Hourly":
                            amount4=5*num*Quantity
                        elif basis=="Daily":
                            amount4=20*num*Quantity
                        elif basis=="Weekly":
                            amount4=60*num*Quantity
                        else:
                            amount4=0
                    amount=amount+amount4
                elif(Name_of_Bike=="Ola Electric"):
                    NS_qty=17
                    if Quantity<=0 or Quantity>NS_qty:
                        print("Insufficient Stock")
                    else:
                        basis = input("Enter Hourly/Daily/Weekly Basis : ")
                        num = int(input("Enter Number of Hours/Days/Weeks : "))
                        if basis=="Hourly":
                            amount5=5*num*Quantity
                        elif basis=="Daily":
                            amount5=20*num*Quantity
                        elif basis=="Weekly":
                            amount5=60*num*Quantity
                        else:
                            amount5=0
                    amount=amount+amount5
        return amount
    def returnBikes(self,Amount):
        print("Total Bill is $",Amount)
C1=Bike()
C1.displayBikes()
Amount=C1.placeOrder()
C1.returnBikes(Amount)


