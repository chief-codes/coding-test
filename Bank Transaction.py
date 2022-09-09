

def transaction():
    balance = 100
    option = int
    
    while option != 4:
        option = int(input("\nEnter: \n (1) for Check Balance \n (2) for Deposit \
        \n (3) for Withdrawal \n (4) for Exit \n"))

        if option == 1:
            print(f"Your Balance is {balance}")

        elif option == 2:
            deposit_amount = int(input("Enter amount to deposit: "))
            balance = balance + deposit_amount  
            #print(f"Thank You for your Transaction....")

        elif option == 3:
            withdrawal_amount = int(input("Enter amount to withdraw: "))
            balance = balance - withdrawal_amount
            #print(f"Thank You for your Transaction....")

    else:
        print("THANK FOR YOUR TRANSACTION!!!!!!")


transaction()