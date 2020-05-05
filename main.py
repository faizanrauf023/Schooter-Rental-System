from rental import RentalPoint, Customer

    
def main():

    point = RentalPoint(10)
    customer = Customer()

    while True:

        print("""
        ********** Schooter Rental Shop **********
        PROMOTION : Enjoy first 20 minutes FREE

        1. Display available schooters.
        2. Rent Schooter on hourly basis at $5 per hour.
        3. Rent Schooter on daily basis at $20 per day.
        4. Return SChooter.
        5. close.
        """)
    
        choice = int(input("Enter your choice: "))

        if choice == 1:
            point.display_()

        elif choice == 2:
            customer.time = point.issue_hourly(customer.request_obj())
            customer.basis = 1

        elif choice == 3:
            Customer.time = point.issue_daily(customer.request_obj())
            customer.basis= 2

        elif choice == 4:
            point.accept_return(customer.return_obj())

        elif choice == 5:
            break

        else:
            print("Please enter number between 1 to 5")
    print("Thanks for Using Our rental services")


if __name__=="__main__":
    main()







