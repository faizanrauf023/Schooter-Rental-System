import datetime


class RentalPoint:

    def __init__(self, stock):

        self.stock = stock

    def display_(self):
        """
        Display number of scooters in stock 
        """

        print("Total number of avalaible scooters are: {}".format(self.stock))

    def issue_hourly(self, num):
        """
        1. Issue scooters on hourly basis
        2. Update inventory   
        """

        if num <= 0:
            print("Number of scooters should be positive")
        
        elif num > self.stock:
            print("We dont have enough scooters available")

        else:
            
            self.stock -= num
            print("Scooter: {} (Rented on hourly basis)".format(num))
            print("Fare: $5 / per hour")
            now = datetime.datetime.now()
            return now

    def issue_daily(self,num):
        """
        1. Issue scooters on daily basis
        2. Update inventory
        """

        if num <= 0:
            print("Number of scooters should be positive")
        
        elif num > self.stock:
            print("We dont have enough scooters available")

        else:
    
            self.stock -= num
            print("Schooter: {} (Rented on daily basis)".format(num))
            print("Fare: $20 / per day ")
            now = datetime.datetime.now()
            return now

    def accept_return(self, request):
        """
        1. Accept return and update inventory.
        2. Calculate and issue bill.
        """

        basis, issuetime, numofscooters = request
        bill = 0

        if basis and issuetime and numofscooters:
            self.stock += numofscooters
            now=datetime.datetime.now()
            rentaltime = now - issuetime
            
            # calculate bill on hourly basis and check for promotion
            if basis == 1:
                if rentaltime.seconds <= 1200:
                    bill = 0

                else:
                    bill = round(rentaltime.seconds / 3600) * 5 * numofscooters

            # calculate bill on daily basis
            elif basis == 2:
                bill = round(rentaltime.days) * 20 * numofscooters
            print("total bill: {}".format(bill))
            print("Rental time: {}".format(rentaltime))
                    
        else:
            print("Are you sure you rented with us")
                

class Customer:

    def __init__(self):
        
        self.time = 0
        self.basis = 0
        self.noofscooter = 0
        
    def request_obj(self):
        """
        Take request to issue scooters
        """

        num = int(input("Enter number of scooters: "))
        self.noofscooter = num
        return self.noofscooter

    def return_obj(self):
        """
        Check wheather scooters are issued and take request for return 
        """

        if self.basis and self.time and self.noofscooter:
            return self.basis,self.time,self.noofscooter

        else:
            return 0,0,0

        





